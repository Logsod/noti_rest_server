import falcon
from flask import json
import db


class CheckToken:
    def on_get(self, req, resp):
        """handle get request"""
        queryString = falcon.uri.parse_query_string(req.query_string)
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        if not "token" in queryString:
            resp.text = json.dumps({"tokenIsValid": False})
        else:
            data = db.Db()
            result = data.checkToken(queryString["token"])
            resp.text = json.dumps({"tokenIsValid": result})
