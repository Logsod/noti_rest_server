import falcon
from flask import json
import db


class CartridgeModel:
    def on_post(self, req, resp):
        """handle post"""

        param = req.media
        if "cartridgeModelName" in param:
            data = db.Db()
            newId = data.addCartdrigeModel(param["cartridgeModelName"])
            resp.text = json.dumps({"id": newId, "model": param["cartridgeModelName"], "depString": ""})
        # do your job
        # print(json.dumps(param))

    def on_get(self, req, resp):
        """handle get request"""
        queryString = falcon.uri.parse_query_string(req.query_string)
        data = db.Db()
        result = data.getAllCartdrigeModel()
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = result

    def on_put(self, req, resp):
        """handle put request"""
        param = req.media
        if "delete" in param:
            data = db.Db()
            result = data.deleteCartdrigeModel(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        elif "id" in param and "model" in param:
            data = db.Db()
            result = data.updateCartdrigeModelName(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        else:
            resp.status = falcon.HTTP_400
            resp.content_type = falcon.MEDIA_TEXT

