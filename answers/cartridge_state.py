import falcon
from flask import json
import db


class CartridgeState:

    def on_get(self, req, resp, state_id):
        """handle get request"""
        data = db.Db()
        result = data.getCartridgesByState(state_id)
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = result

    def on_post(self, req, resp):
        """handle post"""
        param = req.media
        action = int(param['action'])
        data = db.Db()
        if action == 0:  # change status
            result = data.changeCartridgeState(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        if action == 1: # delete
            result = data.deleteCartridgeState(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT

