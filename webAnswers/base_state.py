from pathlib import Path

import falcon

import webAnswers.utils
import web_db


class WebBaseState:

    def get_basic_html(self):
        utils = webAnswers.utils.WebUtils()
        data = web_db.Db()

        html = Path('http_template/base_state.html').read_text(encoding="utf-8")
        html = html.replace("<app_menu>", utils.get_html_menu())

        cartridge_model_list_html = ""
        cartridge_model_list_html_template = """
        <tr>
        <td><input type="checkbox" name="id" value="{id}"></td>
        <td><input type="text" name="model" value="{model}" disabled></td>
        <td><input type="text" name="amount" value="{amount}" disabled></td>
        </tr>
    """
        rows = data.getAllBaseStateCartridges()

        for row in rows:
            html_row = cartridge_model_list_html_template
            html_row = html_row.replace('{id}', str(row['id']))
            html_row = html_row.replace('{cartridge_id}', str(row['cartridge_id']))
            html_row = html_row.replace('{model}', row['model'])
            html_row = html_row.replace('{amount}', str(row['amount']))
            cartridge_model_list_html += html_row

        html = html.replace("<base_cartridge_list>", cartridge_model_list_html)

        cartridge_model_list_html = ""
        cartridge_model_list_html_template = """<option value="{cartridge_id}">{model}</option>"""

        rows = data.getAllCartdrigeModel()
        for row in rows:
            html_row = cartridge_model_list_html_template
            html_row = html_row.replace('{cartridge_id}', str(row['id']))
            html_row = html_row.replace('{model}', row['model'])
            cartridge_model_list_html += html_row
        html = html.replace("<cartridge_model_list>", cartridge_model_list_html)

        return html

    def on_get(self, req, resp):
        utils = webAnswers.utils.WebUtils()
        token_result = utils.check_cookie_token(req.cookies)
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        if token_result:
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
            # 0 take
            # 1 change amount
            # 2 delete
            # 3 add to base state
            error_message = ""
            if param['action'] == "0":
                if "id" in param:
                    if type(param['id']) is list:
                        for ids in param['id']:
                            if data.takeOneCartridge(ids) is False:
                                print("offfff")
                                error_message = "Закончились картриджи"

                    else:
                        if data.takeOneCartridge(param['id']) is False:
                            print("offfff")
                            error_message = "Закончились картриджи"

            if param['action'] == "1":
                if "id" in param:
                    if type(param['id']) is list:
                        for ids in param['id']:
                            data.changeBaseStateCartridgeAmount(ids, param['new_amount'])
                    else:
                        data.changeBaseStateCartridgeAmount(param['id'], param['new_amount'])

            if param['action'] == "2":
                if "id" in param:
                    if type(param['id']) is list:
                        for ids in param['id']:
                            data.deleteCartridgeFromBaseState(ids)
                    else:
                        data.deleteCartridgeFromBaseState(param['id'])

            if param['action'] == "3":
                data.addCartridgesToBaseState(param['cartridge_id'], param['amount'])
            html = self.get_basic_html()
            html = html.replace("<error_message>", error_message)
            resp.text = html
        else:
            resp.text = "not authorized"
