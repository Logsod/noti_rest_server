import falcon
from flask import json
import web_db
from uuid import uuid4
from pathlib import Path
import cgi
import webAnswers.utils


class WebMain:
    def __init__(self):
        self.utils = webAnswers.utils.WebUtils()

    def on_get(self, req, resp):
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        resp.headers['Cache-Control'] = 'public, max-age=0'

        """handle get request"""
        html = Path('http_template/main.html').read_text(encoding="utf-8")
        html = html.replace("<app_menu>", self.utils.get_html_menu())
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        resp.text = html

    def on_post(self, req, resp):
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        resp.headers['Cache-Control'] = 'public, max-age=0'

        param = req.media
        print(param)
        if param['action'] == "1":
            resp.set_cookie("token", "", max_age=0)
            raise falcon.HTTPMovedPermanently("/")
