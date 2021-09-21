from pathlib import Path

import falcon

import webAnswers.utils
import web_db


class WebPrinterModel:

    def get_basic_html(self):
        utils = webAnswers.utils.WebUtils()
        data = web_db.Db()

        html = Path('http_template/printer_model.html').read_text(encoding="utf-8")
        html = html.replace("<app_menu>", utils.get_html_menu())

        printer_model_list_html = ""
        printer_model_list_html_template = """<tr>
                        <td><input type="checkbox" name="printer_model_id" value="{printer_model_id}"></td>
                        <td><input type="text" name="printer_model_name" value="{printer_model_name}" disabled></td>
                    </tr>"""
        data = data.getAllPrinterModel()
        for row in data:
            html_row = printer_model_list_html_template
            html_row = html_row.replace('{printer_model_id}', str(row['id']))
            html_row = html_row.replace('{printer_model_name}', row['model'])
            printer_model_list_html += html_row

        html = html.replace("<printer_list_form_html>", printer_model_list_html)
        return html

    def on_get(self, req, resp):
        utils = webAnswers.utils.WebUtils()
        token_result = utils.check_cookie_token(req.cookies)
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        if token_result:
            resp.content_type = 'text/html'
            resp.text = self.get_basic_html()
        else:
            resp.text = "not authorized"

    def on_post(self, req, resp):
        utils = webAnswers.utils.WebUtils()
        token_result = utils.check_cookie_token(req.cookies)
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        if token_result:
            data = web_db.Db()
            param = req.media
            print(param)
            # action list
            # 0 add printer
            # 1 delete printer
            if param['action'] == "1":
                if "printer_model_id" in param:
                    print(type(param['printer_model_id']))
                    if type(param['printer_model_id']) is list:
                        for ids in param['printer_model_id']:
                            data.deletePrinterModel(ids)
                    else:
                        data.deletePrinterModel(param['printer_model_id'])

            if param['action'] == "0":
                data.addPrinterModel(param['printer_model_name'])

            resp.text = self.get_basic_html()
        else:
            resp.text = "not authorized"
