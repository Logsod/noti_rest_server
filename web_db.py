import collections
import itertools

import mysql.connector
from mysql.connector import Error

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

    def addToken(self, token, owner):
        query = """INSERT INTO tokens (token, owner) VALUES (%s, %s)"""
        self.cursor.execute(query, (token, owner))
        self.connection.commit()

    def checkToken(self, token):
        query = """select id from tokens where token like %s"""
        self.cursor.execute(query, (token,))
        row = self.cursor.fetchone()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False

    def getAllPrinterModel(self):
        query = """SELECT * FROM printer_model where 1"""
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def addPrinterModel(self, printerName):
        query = """INSERT INTO printer_model (model) values (%s)"""
        self.cursor.execute(query, (printerName,))
        self.connection.commit()
        return self.cursor.lastrowid

    def deletePrinterModel(self, row_id):
        query = """delete from printer_model where id = %s"""
        self.cursor.execute(query, (row_id,))
        self.connection.commit()

    def getAllPrinter(self):
        query = """select printer.id, printer.comment, printer_model.model
                    from printer
                    inner join printer_model on printer_model.id = printer.model_id 
                    ORDER BY printer.id ASC;
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def addPrinter(self, param):
        query = """insert into printer (model_id, comment) values ( %s , %s )"""
        self.cursor.execute(query, (param['model_id'], param['comment']))
        self.connection.commit()

    def updatePrinterComment(self, param):
        query = """update printer set comment = %s where id = %s"""
        self.cursor.execute(query, (param['comment'], param['id']))
        self.connection.commit()

    def getPrinterComment(self, row_id):
        query = """select comment from printer where id = %s"""
        self.cursor.execute(query, (row_id,))
        row = self.cursor.fetchone()
        return row['comment']

    def deletePrinter(self, row_id):
        query = """delete from printer where id = %s"""
        self.cursor.execute(query, (row_id,))
        self.connection.commit()

    def getAllCartdrigeModel(self):
        query = """SELECT * FROM cartridge_model where 1"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def addCartdrigeModel(self, printerName):
        query = """INSERT INTO cartridge_model (model) values (%s)"""
        self.cursor.execute(query, (printerName,))
        self.connection.commit()
        return self.cursor.lastrowid

    def getCartridgeModelByCartridgeId(self, row_id):
        query = """select model from cartridge_model where id = %s"""
        self.cursor.execute(query, (row_id,))
        data = self.cursor.fetchone()
        return data['model']

    def getCartridgeModelByBaseStateId(self, row_id):
        query = """select base_state.cartridge_id, cartridge_model.model from base_state 
INNER JOIN cartridge_model ON base_state.cartridge_id = cartridge_model.id
where base_state.id = %s"""
        self.cursor.execute(query, (row_id,))
        data = self.cursor.fetchone()
        return data['model']

    # todo check in android app
    def deleteCartdrigeModel(self, cartridge_id):
        query = """delete from cartridge_model where id = %s"""
        self.cursor.execute(query, (cartridge_id,))
        self.connection.commit()
        query = """delete from cartridge_dep where cartridge_id = %s"""
        self.cursor.execute(query, (cartridge_id,))
        self.connection.commit()

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

    def clearCartridgesDep(self, param):
        for cartridge_id in param['cartridges_id']:
            query = """delete from cartridge_dep where cartridge_id = %s"""
            self.cursor.execute(query, (cartridge_id,))
            self.connection.commit()
            self.updateCartridgeDepString(cartridge_id)
        return self.getAllCartdrigeModel()

    def getAllBaseStateCartridges(self):
        query = """SELECT base_state.id, base_state.cartridge_id, cartridge_model.model, base_state.amount
                     FROM base_state 
                     INNER JOIN cartridge_model ON base_state.cartridge_id = cartridge_model.id
                 """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def changeBaseStateCartridgeAmount(self, row_id, amount):
        query = """update base_state set amount = %s where id = %s"""
        self.cursor.execute(query, (amount, row_id))
        self.connection.commit()

    def deleteCartridgeFromBaseState(self, id):
        query = """delete from base_state where id = %s"""
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def addCartridgesToBaseState(self, cartridge_id, amount):
        query = """select amount from base_state where cartridge_id = %s"""
        self.cursor.execute(query, (cartridge_id,))
        row = self.cursor.fetchone()
        if self.cursor.rowcount != -1:
            query = """update base_state set amount = amount + %s where cartridge_id = %s"""
            self.cursor.execute(query, (amount, cartridge_id))
            self.connection.commit()
        else:
            query = """insert into base_state (cartridge_id ,amount) values (%s, %s)"""
            self.cursor.execute(query, (cartridge_id, amount))
            self.connection.commit()

    def takeOneCartridge(self, row_id):
        query = """select * from base_state where id = %s"""
        self.cursor.execute(query, (row_id,))
        data = self.cursor.fetchall()
        for row in data:
            if row['amount'] > 0:
                query = """insert into cartridge_state (cartridge_id, state) values (%s, %s)"""
                self.cursor.execute(query, (row['cartridge_id'], 1))
                self.connection.commit()
                query = """update base_state set amount = amount - 1 where id = %s"""
                self.cursor.execute(query, (row_id,))
                self.connection.commit()
            else:
                return False

    def takeCartridges(self, row_id, amount):
        query = """select * from base_state where id = %s"""
        self.cursor.execute(query, (row_id,))
        row = self.cursor.fetchone()
        # print("amount:"+str(row['cartridge_id']))
        # return
        for i in range(int(amount)):
            query = """insert into cartridge_state (cartridge_id, state) values (%s, %s)"""
            self.cursor.execute(query, (str(row['cartridge_id']), 1))
            self.connection.commit()
        query = """update base_state set amount = amount - %s where id = %s"""
        self.cursor.execute(query, (amount, row_id,))
        self.connection.commit()

    def getStateListLabels(self):
        query = """select * from state"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getCurrentCartridgeStateLabel(self, row_id):
        query = """select state.state_name from cartridge_state 
                INNER JOIN state ON state.id = cartridge_state.state
                where cartridge_state.id = %s"""
        self.cursor.execute(query, (row_id,))
        data = self.cursor.fetchone()
        return data['state_name']

    def getStateLabelById(self, row_id):
        query = """select * from state where id = %s"""
        self.cursor.execute(query, (row_id,))
        data = self.cursor.fetchone()
        return data['state_name']

    def getCartridgesByStateGrouped(self, state_id):
        query = """SET sql_mode = '';"""
        self.cursor.execute(query)

        query = """SELECT 
            count(cartridge_state.id ) AS amount,
            cartridge_state.cartridge_id as cartridge_id,
            cartridge_model.model
            FROM cartridge_state 
            INNER JOIN cartridge_model ON cartridge_state.cartridge_id = cartridge_model.id
            WHERE state = %s GROUP BY cartridge_id"""

        self.cursor.execute(query, (state_id,))
        return self.cursor.fetchall()

    def getCartridgesByStateAndCartridge(self, state_id, cartridge_id):

        query = """SELECT 
            cartridge_state.id AS row_state_id,
            cartridge_state.cartridge_id as cartridge_id,
            cartridge_model.model
            FROM cartridge_state 
            INNER JOIN cartridge_model ON cartridge_state.cartridge_id = cartridge_model.id
            WHERE cartridge_state.state = %s AND cartridge_state.cartridge_id = %s"""
        self.cursor.execute(query, (state_id, cartridge_id))
        return self.cursor.fetchall()

    def getCartridgesByState(self, state_id):

        query = """SELECT 
            cartridge_state.id AS row_state_id,
            cartridge_state.cartridge_id as cartridge_id,
            cartridge_model.model
            FROM cartridge_state 
            INNER JOIN cartridge_model ON cartridge_state.cartridge_id = cartridge_model.id
            WHERE cartridge_state.state = %s"""
        self.cursor.execute(query, (state_id,))
        return self.cursor.fetchall()

    def changeCartridgeState(self, new_state, row_state_id):
        query = """update cartridge_state set state = %s where id = %s"""
        self.cursor.execute(query, (new_state, row_state_id))
        self.connection.commit()

    def deleteCartridgeState(self, row_state_id):
        query = """delete from cartridge_state where id = %s"""
        self.cursor.execute(query, (row_state_id,))
        self.connection.commit()

    def writeToLog(self, action):
        query = """insert into log (action,timestamp) values (%s, CURRENT_TIMESTAMP  )"""
        self.cursor.execute(query, (action,))
        self.connection.commit()

    def getAllLogRecords(self):
        query = """select * from log where 1"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
