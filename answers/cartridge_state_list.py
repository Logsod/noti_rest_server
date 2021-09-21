import falcon
from flask import json
import db


class CartridgeStateList:

    def on_get(self, req, resp):
        """handle get request"""
        print("stttate")
        data = db.Db()
        result = data.getStateListLabels()
        print(result)
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = result
