import falcon
from flask import json
import db


class PrinterModel:
    def on_post(self, req, resp):
        """handle post"""

        param = req.media
        if "printerModelName" in param:
            data = db.Db()
            print("add printer" + param["printerModelName"])
            newId = data.addPrinterModel(param["printerModelName"])
            json.dumps({"printerModelName": param["printerModelName"], "id": newId})
        # do your job
        # print(json.dumps(param))

    def on_get(self, req, resp):
        """handle get request"""
        queryString = falcon.uri.parse_query_string(req.query_string)
        data = db.Db()
        result = data.getAllPrinterModel()
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = result

    def on_put(self, req, resp):
        """handle put request"""
        param = req.media
        if "id" in param and "model" in param:
            data = db.Db()
            result = data.updatePrinterModelName(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        else:
            resp.status = falcon.HTTP_400
            resp.content_type = falcon.MEDIA_TEXT

    def on_delete(self, req, resp, id=-1):
        """handle delete request"""
        if id != -1:
            data = db.Db()
            print("delete")
            result = data.deletePrinterModel(id)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        else:
            resp.status = falcon.HTTP_400
            resp.content_type = falcon.MEDIA_TEXT
