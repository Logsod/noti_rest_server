import falcon
from flask import json
import db


class CartridgeBaseState:
    def on_post(self, req, resp):
        """handle post"""
        param = req.media
        action = int(param['action'])
        data = db.Db()
        if action == 0:  # add
            if "cartridge_id" in param and "amount" in param:
                result = data.addCartridgesToBaseState(param)
                resp.status = falcon.HTTP_200
                resp.content_type = falcon.MEDIA_TEXT
                resp.text = result
        elif action == 1:  # change amount
            data.changeBaseStateCartridgeAmount(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        elif action == 2:  # take one cartridge (insert into state table list and set status to 1) 1 equal work status
            data.takeOneCartridge(param)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
        elif action == 3:  # delete
            data.deleteCartridgeFromBaseState(param['id'])
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT

    def on_get(self, req, resp):
        data = db.Db()
        result = data.getAllBaseStateCartridges()
        print(result)
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = result
