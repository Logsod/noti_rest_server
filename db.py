import collections
import itertools

import mysql.connector
from mysql.connector import Error
from flask import json
import const

class Db:
    """constructor"""

    def __init__(self):
        """db connect"""
        try:
            self.connection = mysql.connector.connect(host=const.MYSQL_HOST,
                                                      database=const.MYSQL_DATABASE,
                                                      user=const.MYSQL_USER,
                                                      password=const.MYSQL_PASSWORD)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor(dictionary=True)
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                # print("You're connected to database: ", record)

                # self.cursor.execute("SELECT * FROM test")
                row = self.cursor.fetchone()
                # while row is not None:
                #     print(row)
                #     row = self.cursor.fetchone()

        except Error as e:
            print("Error while connecting to MySQL", e)

    def signIn(self, login, password):
        """sign in"""
        print("search:" + login + " " + password)
        # param = '{}'.format(login)
        query = """select * from users where login like %s and password like %s"""
        self.cursor.execute(query, (login, password))
        # self.cursor.fetchall()
        row = self.cursor.fetchone()
        if self.cursor.rowcount == 1:
            return row
        else:
            return False
        # print(self.cursor.rowcount)

    def addToken(self, token, owner):
        query = """INSERT INTO tokens (token, owner) VALUES (%s, %s)"""
        self.cursor.execute(query, (token, owner))
        self.connection.commit()

    def deleteToken(self, token):
        query = """delete from tokens where token like %s"""
        self.cursor.execute(query, (token,))
        self.connection.commit()

    def checkToken(self, token):
        query = """select id from tokens where token like %s"""
        self.cursor.execute(query, (token,))
        row = self.cursor.fetchone()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False

    def convertToJson(self):
        row_headers = [x[0] for x in self.cursor.description]  # this will extract row headers
        rv = self.cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    #############################################################
    ############printer models
    #############################################################
    def addPrinterModel(self, printerName):
        query = """INSERT INTO printer_model (model) values (%s)"""
        self.cursor.execute(query, (printerName,))
        self.connection.commit()
        return self.cursor.lastrowid

    def getAllPrinterModel(self):
        query = """SELECT * FROM printer_model where 1"""
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        model_list = []
        for row in data:
            d = collections.OrderedDict()
            d['id'] = row['id']
            d['model'] = row['model']
            model_list.append(d)
        result = json.dumps(model_list)
        return result
        # print(result)
        # result = self.convertToJson()
        # print(result)

    def updatePrinterModelName(self, param):
        query = """update printer_model set model = %s where id = %s"""
        self.cursor.execute(query, (param['model'], param['id']))
        self.connection.commit()

    def deletePrinterModel(self, row_id):
        query = """delete from printer_model where id = %s"""
        self.cursor.execute(query, (row_id,))
        self.connection.commit()

    #############################################################
    ############printer list
    #############################################################
    def addPrinter(self, param):
        query = """insert into printer (model_id, comment) values ( %s , %s )"""
        self.cursor.execute(query, (param['model_id'], param['comment']))
        self.connection.commit()

        lastId = self.cursor.lastrowid
        query = """select model from printer_model where id = %s"""
        self.cursor.execute(query, (param['model_id'],))
        result = self.cursor.fetchone()
        model = result['model']
        print(model)
        return json.dumps({"id": lastId, "comment": param['comment'], "model": model})

    def getAllPrinter(self):
        query = """select printer.id, printer.comment, printer_model.model
                    from printer
                    inner join printer_model on printer_model.id = printer.model_id 
                    ORDER BY printer.id ASC;
                """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        printer_list = []
        for row in data:
            d = collections.OrderedDict()
            d['id'] = row['id']
            d['comment'] = row['comment']
            d['model'] = row['model']
            printer_list.append(d)
        result = json.dumps(printer_list)
        return result

    def updatePrinterComment(self, param):
        query = """update printer set comment = %s where id = %s"""
        self.cursor.execute(query, (param['comment'], param['id']))
        self.connection.commit()

    def deletePrinter(self, row_id):
        query = """delete from printer where id = %s"""
        self.cursor.execute(query, (row_id,))
        self.connection.commit()

    #############################################################
    ############cartdrige models
    #############################################################
    def addCartdrigeModel(self, printerName):
        query = """INSERT INTO cartridge_model (model) values (%s)"""
        self.cursor.execute(query, (printerName,))
        self.connection.commit()
        return self.cursor.lastrowid

    def getAllCartdrigeModel(self):
        query = """SELECT * FROM cartridge_model where 1"""
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        model_list = []
        for row in data:
            d = collections.OrderedDict()
            d['id'] = row['id']
            d['model'] = row['model']
            d['depString'] = row['depString']
            model_list.append(d)
        result = json.dumps(model_list)
        return result
        # print(result)
        # result = self.convertToJson()
        # print(result)

    def updateCartdrigeModelName(self, param):
        query = """update cartridge_model set model = %s where id = %s"""
        self.cursor.execute(query, (param['model'], param['id']))
        self.connection.commit()

    def deleteCartdrigeModel(self, param):
        for printer_id in param['printer_id']:
            query = """delete from cartridge_model where id = %s"""
            self.cursor.execute(query, (printer_id,))
            self.connection.commit()
            query = """delete from cartridge_dep where cartridge_id = %s"""
            self.cursor.execute(query, (printer_id,))
            self.connection.commit()

    def clearCartridgesDep(self, param):
        for cartridge_id in param['cartridges_id']:
            query = """delete from cartridge_dep where cartridge_id = %s"""
            self.cursor.execute(query, (cartridge_id,))
            self.connection.commit()
            self.updateCartridgeDepString(cartridge_id)
        return self.getAllCartdrigeModel()

    def updateCartridgeModelDep(self, param):
        for cartridge_id in param['cartridges_id']:
            updated = False
            for printer_id in param['printers_id']:
                query = """select * from cartridge_dep where cartridge_id = %s and printer_id = %s"""
                self.cursor.execute(query, (cartridge_id, printer_id))
                self.cursor.fetchone()
                print(self.cursor.rowcount)
                if self.cursor.rowcount <= 0:
                    updated = True
                    query = """insert into cartridge_dep (cartridge_id, printer_id) values (%s, %s)"""
                    self.cursor.execute(query, (cartridge_id, printer_id))
                    self.connection.commit()

            if updated:
                self.updateCartridgeDepString(cartridge_id)

        return self.getAllCartdrigeModel()

    def updateCartridgeDepString(self, cartridge_id):
        query = """select * from cartridge_dep where cartridge_id = %s"""
        self.cursor.execute(query, (cartridge_id,))
        data = self.cursor.fetchall()
        depString = ""
        step = 0
        for row in data:
            query = """select * from printer_model where id = %s """
            self.cursor.execute(query, (row['printer_id'],))
            printerRow = self.cursor.fetchone()
            if step != 0:
                depString += "\n"
            depString += printerRow['model']
            step += 1
        query = """update cartridge_model set depString = %s where id = %s"""
        self.cursor.execute(query, (depString, cartridge_id))
        self.connection.commit()

    def getCartridgesFromPrinterDep(self, printer_id):
        query = """select * from cartridge_dep where printer_id = %s"""
        self.cursor.execute(query, (printer_id,))
        data = self.cursor.fetchall()
        result = []
        for row in data:
            query = """select * from cartridge_model where id = %s"""
            self.cursor.execute(query, (row['cartridge_id'],))
            cart_data = self.cursor.fetchall()
            for cart_row in cart_data:
                d = collections.OrderedDict()
                d['id'] = cart_row['id']
                d['model'] = cart_row['model']
                d['depString'] = cart_row['depString']
                result.append(d)
        return json.dumps(result)

    #############################################################
    ############base state
    #############################################################
    def addCartridgesToBaseState(self, param):
        query = """insert into base_state (cartridge_id ,amount) values (%s, %s)"""
        self.cursor.execute(query, (param['cartridge_id'], param['amount']))
        self.connection.commit()
        query = """select model from cartridge_model where id = %s"""
        self.cursor.execute(query, (param['cartridge_id'],))
        data = self.cursor.fetchone()
        return json.dumps({"id": self.cursor.lastrowid, "amount": param['amount'], "model": data['model']})

    def getAllBaseStateCartridges(self):
        query = """SELECT base_state.id, base_state.cartridge_id, cartridge_model.model, base_state.amount
                    FROM base_state 
                    INNER JOIN cartridge_model ON base_state.cartridge_id = cartridge_model.id
                """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        result = []
        for row in data:
            d = collections.OrderedDict()
            d['id'] = row['id']
            d['cartridge_id'] = row['cartridge_id']
            d['model'] = row['model']
            d['amount'] = row['amount']
            result.append(d)
        return json.dumps(result)

    def changeBaseStateCartridgeAmount(self, param):
        query = """update base_state set amount = %s where id = %s"""
        self.cursor.execute(query, (param['amount'], param['id']))
        self.connection.commit()

    def deleteCartridgeFromBaseState(self, id):
        query = """delete from base_state where id = %s"""
        self.cursor.execute(query, (id,))
        self.connection.commit()

    #############################################################
    ############cartridge state list
    #############################################################
    def getStateListLabels(self):
        query = """select * from state"""
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        result = []
        for row in data:
            d = collections.OrderedDict()
            d['id'] = row['id']
            d['state_name'] = row['state_name']
            result.append(d)
        return json.dumps(result)

    def takeOneCartridge(self, param):
        print(param)
        query = """insert into cartridge_state (cartridge_id, state) values (%s, %s)"""
        self.cursor.execute(query, (param['cartridge_id'], 1))
        self.connection.commit()
        query = """update base_state set amount = amount - 1 where id = %s"""
        self.cursor.execute(query, (param['id'],))
        self.connection.commit()

    #############################################################
    ############cartridge state
    #############################################################
    def getCartridgesByState(self, state_id):

        query = """SELECT 
            cartridge_state.id AS row_state_id,
            cartridge_state.cartridge_id as cartridge_id,
            cartridge_model.model
            FROM cartridge_state 
            INNER JOIN cartridge_model ON cartridge_state.cartridge_id = cartridge_model.id
            WHERE cartridge_state.state = %s"""
        self.cursor.execute(query, (state_id,))
        data = self.cursor.fetchall()
        result = []
        for row in data:
            d = collections.OrderedDict()
            d['row_state_id'] = row['row_state_id']
            d['cartridge_id'] = row['cartridge_id']
            d['model'] = row['model']
            result.append(d)
        return json.dumps(result)

    def changeCartridgeState(self, param):
        query = """update cartridge_state set state = %s where id = %s"""
        self.cursor.execute(query, (param['state'], param['row_state_id']))
        self.connection.commit()

    def deleteCartridgeState(self, param):
        query = """delete from cartridge_state where id = %s"""
        self.cursor.execute(query, (param['row_state_id'],))
        self.connection.commit()
