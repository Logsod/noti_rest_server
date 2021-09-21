import falcon
from flask import json
import db
from uuid import uuid4


class SignIn:
    def on_get(self, req, resp):
        """handle get request"""
        queryString = falcon.uri.parse_query_string(req.query_string)
        #        print("query string" + queryString)
        if not queryString or not "password" in queryString or not "login" in queryString:
            resp.text = json.dumps({"message": "password or login is empty", "token": "", "success": False})
        else:
            data = db.Db()
            user = data.signIn(queryString["login"], queryString["password"])
            if user is not False:
                rand_token = uuid4().hex
                data.addToken(rand_token, user["id"])
                resp.status = falcon.HTTP_200
                resp.content_type = falcon.MEDIA_TEXT
                resp.text = json.dumps({"message": "test", "token": rand_token, "success": True})
            else:
                resp.status = falcon.HTTP_200
                resp.content_type = falcon.MEDIA_TEXT
                resp.text = json.dumps({"message": "user not found", "token": "", "success": False})

    def on_post(self, req, resp):
        param = req.media
        data = db.Db()
        data.deleteToken(param['token'])
