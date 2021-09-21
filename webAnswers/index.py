import sys

import falcon
from flask import json
import web_db
from uuid import uuid4
from pathlib import Path
import cgi


class WebIndex:
    def on_get(self, req, resp):
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        resp.headers['Cache-Control'] = 'public, max-age=0'

        """handle get request"""
        cookies = req.cookies
        if "token" in cookies:
            data = web_db.Db()
            if data.checkToken(cookies['token']):
                raise falcon.HTTPMovedPermanently("/main")

        html = Path('http_template/index.html').read_text()
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        resp.text = html
        queryString = falcon.uri.parse_query_string(req.query_string)
        #        print("query string" + queryString)
        # if not queryString or not "password" in queryString or not "login" in queryString:
        #     resp.text = json.dumps({"message": "password or login is empty", "token": "", "success": False})
        # else:
        #     data = db.Db()
        #     user = data.signIn(queryString["login"], queryString["password"])
        #     if user is not False:
        #         rand_token = uuid4().hex
        #         data.addToken(rand_token, user["id"])
        #         resp.status = falcon.HTTP_200
        #         resp.content_type = falcon.MEDIA_TEXT
        #         resp.text = json.dumps({"message": "test", "token": rand_token, "success": True})
        #     else:
        #         resp.status = falcon.HTTP_200
        #         resp.content_type = falcon.MEDIA_TEXT
        #         resp.text = json.dumps({"message": "user not found", "token": "", "success": False})

    def on_post(self, req, resp):
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        resp.headers['Cache-Control'] = 'public, max-age=0'

        param = req.media
        data = web_db.Db()

        html = Path('http_template/index.html').read_text()
        resp.content_type = 'text/html'
        user = data.signIn(param["login"], param["password"])
        if user is not False:
            rand_token = uuid4().hex
            data.addToken(rand_token, user["id"])
            resp.status = falcon.HTTP_200
            resp.set_cookie("token", rand_token, max_age=2147483647)
            # resp.text = json.dumps({"message": "test", "token": rand_token, "success": True})
            raise falcon.HTTPMovedPermanently("/main")
        else:
            html = html.replace('<error_message>', 'неправильный логин или пароль')
            resp.status = falcon.HTTP_200
            resp.text = html
