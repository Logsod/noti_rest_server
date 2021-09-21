from pathlib import Path

import falcon

import webAnswers.utils
import web_db


class WebCartridgeModel:

    def get_basic_html(self):
        utils = webAnswers.utils.WebUtils()
        data = web_db.Db()

        html = Path('http_template/cartridge_model.html').read_text(encoding="utf-8")
        html = html.replace("<app_menu>", utils.get_html_menu())

        cartridge_model_list_html = ""
        cartridge_model_list_html_template = """<tr>
                        <td><input type="checkbox" name="cartridges_id" value="{cartridge_model_id}"></td>
                        <td><input type="text" name="cartridge_model_name" value="{cartridge_model_name}" disabled></td>
                        <td>{depString}</td>
                        
                    </tr>"""
        rows = data.getAllCartdrigeModel()
        for row in rows:
            html_row = cartridge_model_list_html_template
            html_row = html_row.replace('{cartridge_model_id}', str(row['id']))
            html_row = html_row.replace('{cartridge_model_name}', row['model'])
            depString = row['depString']
            if row['depString'] is None:
                row['depString'] = ""
            html_row = html_row.replace('{depString}', row['depString'])
            cartridge_model_list_html += html_row

        html = html.replace("<cartridge_list_form_html>", cartridge_model_list_html)

        cartridge_model_list_html = ""
        cartridge_model_list_html_template = """<option value="{printers_id}">{printers_name}</option>"""
        rows = data.getAllPrinterModel()

        for row in rows:
            html_row = cartridge_model_list_html_template
            html_row = html_row.replace('{printers_id}', str(row['id']))
            html_row = html_row.replace('{printers_name}', str(row['model']))
            cartridge_model_list_html += html_row

        html = html.replace("<printers_list>", cartridge_model_list_html)

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
            # 0 add cartridge
            # 1 delete cartridge
            # 2 add dep
            # 3 clear dep
            if param['action'] == "1":
                if "cartridge_model_id" in param:
                    if type(param['cartridge_model_id']) is list:
                        for ids in param['cartridge_model_id']:
                            data.deleteCartdrigeModel(ids)
                    else:
                        data.deleteCartdrigeModel(param['cartridge_model_id'])

            if param['action'] == "2":

                printers_id = []
                cartridges_id = []
                if type(param['printers_id']) is str:
                    printers_id.append(param['printers_id'])
                    param['printers_id'] = printers_id
                # else:
                # printers_id = param['printers_id']

                if type(param['cartridges_id']) is str:
                    cartridges_id.append(param['cartridges_id'])
                    param['cartridges_id'] = cartridges_id
                # else:
                # cartridges_id = param['cartridges_id']

                data.updateCartridgeModelDep(param)

            if param['action'] == "3":
                cartridges_id = []
                if type(param['cartridges_id']) is str:
                    cartridges_id.append(param['cartridges_id'])
                    param['cartridges_id'] = cartridges_id
                data.clearCartridgesDep(param)

            if param['action'] == "0":
                data.addCartdrigeModel(param['cartridge_model_name'])

            resp.text = self.get_basic_html()
        else:
            resp.text = "not authorized"
