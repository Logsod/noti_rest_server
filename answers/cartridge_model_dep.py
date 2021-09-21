import falcon
from flask import json
import db


class CartridgeModelDep:
    def on_get(self, req, resp):
        queryString = falcon.uri.parse_query_string(req.query_string)
        data = db.Db()
        result = data.getCartridgesFromPrinterDep(queryString['id'])
        resp.text = result
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT

    def on_put(self, req, resp):
        """handle put request"""
        param = req.media
        if "cartridges_id" in param and "printers_id" in param:
            if param['clear']:
                data = db.Db()
                print(param)
                result = data.clearCartridgesDep(param)
                resp.text = result
                resp.status = falcon.HTTP_200
                resp.content_type = falcon.MEDIA_TEXT
            else:
                data = db.Db()
                result = data.updateCartridgeModelDep(param)
                resp.text = result
                resp.status = falcon.HTTP_200
                resp.content_type = falcon.MEDIA_TEXT
        else:
            resp.status = falcon.HTTP_400
            resp.content_type = falcon.MEDIA_TEXT
