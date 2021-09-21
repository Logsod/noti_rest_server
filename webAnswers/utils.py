from pathlib import Path

import web_db
from const import SERVER_HOST


class WebUtils:
    def get_state_list(self):
        data = web_db.Db()
        result = []
        status_html = ""
        status_html_template = """<a href={host}state/{state_id}>{state_name}</a> &nbsp"""

        html = ""
        rows = data.getStateListLabels()
        for row in rows:
            status_html = status_html_template
            status_html = status_html.replace("{host}", SERVER_HOST)
            status_html = status_html.replace("{state_id}", str(row['id']))
            status_html = status_html.replace("{state_name}", row['state_name'])
            html += status_html
        return html

    def get_html_menu(self):
        html = Path('http_template/menu_template.html').read_text(encoding="utf-8")
        html = html.replace("{host}", SERVER_HOST)
        html = html.replace("{state_list}", self.get_state_list())
        return html

    def check_cookie_token(self, cookies):
        data = web_db.Db()
        if "token" in cookies:
            return data.checkToken(cookies['token'])

        else:
            return False
