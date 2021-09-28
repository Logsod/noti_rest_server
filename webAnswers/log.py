import falcon
from flask import json
import web_db
from uuid import uuid4
from pathlib import Path
import cgi
import webAnswers.utils


class WebLog:
    def __init__(self):
        self.utils = webAnswers.utils.WebUtils()

    def on_get(self, req, resp):
        data = web_db.Db()
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        resp.headers['Cache-Control'] = 'public, max-age=0'

        """handle get request"""
        html = Path('http_template/log.html').read_text(encoding="utf-8")
        html = html.replace("<app_menu>", self.utils.get_html_menu())

        log_list = ""
        log_list_template = """<tr>
        <td>{action}</td>
        <td>{timestamp}</td>
        </tr>"""
        records = data.getAllLogRecords()
        for row in records:
            html_row = log_list_template
            html_row = html_row.replace("{action}", row['action'])
            html_row = html_row.replace("{timestamp}", str(row['timestamp']))
            log_list += html_row
        html = html.replace("<log>", log_list)

        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        resp.text = html
