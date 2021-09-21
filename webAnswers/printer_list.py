from pathlib import Path

import falcon

import webAnswers.utils
import web_db
from const import SERVER_HOST


class WebPrinterList:
    def get_basic_html(self):
        utils = webAnswers.utils.WebUtils()
        data = web_db.Db()
        html = Path('http_template/printer_list.html').read_text(encoding="utf-8")
        html = html.replace("<app_menu>", utils.get_html_menu())
        html = html.replace("{host}", SERVER_HOST)

        printer_model_list_html = ""
        printer_model_list_html_template = """<option value="{printer_model_id}">{printer_name}</option>"""
        rows = data.getAllPrinterModel()
        for row in rows:
            html_row = printer_model_list_html_template
            html_row = html_row.replace('{printer_model_id}', str(row['id']))
            html_row = html_row.replace('{printer_name}', row['model'])
            printer_model_list_html += html_row

        html = html.replace("<printer_models>", printer_model_list_html)

        printer_model_list_html = ""
        printer_model_list_html_template = """<tr><td>{model}</td><td>{comment}</td>
        <td><a href='{host}printer_list/0/{edit_id}'>Изменить коментарий</a></td>
        <td><a href='{host}printer_list/1/{edit_id}' onclick="return confirm('Удалить?')">Удалить</a></td>
        </tr>"""
        printer_list = data.getAllPrinter()
        for row in printer_list:
            html_row = printer_model_list_html_template

            html_row = html_row.replace("{host}", SERVER_HOST)
            html_row = html_row.replace("{model}", row['model'])
            html_row = html_row.replace("{comment}", row['comment'])
            html_row = html_row.replace("{edit_id}", str(row['id']))

            printer_model_list_html += html_row

        html = html.replace("<printer_list>", printer_model_list_html)
        return html

    def get_edit_comment_form(self, row_id):
        data = web_db.Db()
        comment = data.getPrinterComment(row_id)
        html = """
        <form action="<host>printer_list" enctype="application/x-www-form-urlencoded" method="post">
        <input type="hidden" name="action" value="2">
        Новый коментарий<br>
        <input name="id" type="hidden" value="<row_id>">
        <textarea name="comment" rows="5" cols="40"><comment></textarea>
        <br>
        <input type="submit" value="Изменить">
        </form>
        <br><br><br>
        """
        html = html.replace("<host>", SERVER_HOST)
        html = html.replace("<row_id>", row_id)
        html = html.replace("<comment>", comment)
        return html

    # action
    # 0 show new comment form
    # 1 delete by id
    def on_get(self, req, resp, action_id=-1, edit_id=-1):
        utils = webAnswers.utils.WebUtils()
        token_result = utils.check_cookie_token(req.cookies)
        resp.content_type = "text/html"
        resp.status = falcon.HTTP_200

        if token_result:
            text = ""
            if action_id == "0":
                text = self.get_basic_html()
                edit_comment_form_code = self.get_edit_comment_form(edit_id)
                print("edit")
                text = text.replace("<edit_comment_form>", edit_comment_form_code)
            elif action_id == "1":
                data = web_db.Db()
                data.deletePrinter(edit_id)
                text = self.get_basic_html()
            else:
                text = self.get_basic_html()
            resp.text = text
            """"""
        else:
            resp.text = "not authorized"

    def on_post(self, req, resp):
        utils = webAnswers.utils.WebUtils()
        token_result = utils.check_cookie_token(req.cookies)
        resp.content_type = "text/html"
        resp.status = falcon.HTTP_200

        if token_result:
            param = req.media
            action = param['action']
            # action list
            # 0 add printer
            # 2 edit comment

            if action == "0":
                data = web_db.Db()
                data.addPrinter(param)
            if action == "2":
                data = web_db.Db()
                data.updatePrinterComment(param)
            resp.text = self.get_basic_html()
        else:
            resp.text = "not authorized"
