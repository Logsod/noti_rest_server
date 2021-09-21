import falcon
from flask import json
import db


class Printer:
    def on_post(self, req, resp):
        param = req.media
        if "model_id" in param:
            data = db.Db()
            result = data.addPrinter(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
            resp.text = result
        else:
            resp.status = falcon.HTTP_400
            resp.content_type = falcon.MEDIA_TEXT

    def on_get(self, req, resp):
        data = db.Db()
        result = data.getAllPrinter()
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = result
        print(result)

    def on_put(self, req, resp):
        param = req.media
        if "id" in param:
            data = db.Db()
            result = data.updatePrinterComment(param)
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
            result = data.deletePrinter(id)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        else:
            resp.status = falcon.HTTP_400
            resp.content_type = falcon.MEDIA_TEXT