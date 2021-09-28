from pathlib import Path

import falcon

import webAnswers.utils
import web_db
from const import SERVER_HOST


class WebState:
    def get_basic_html(self, current_state):
        utils = webAnswers.utils.WebUtils()
        data = web_db.Db()
        html = Path('http_template/state.html').read_text(encoding="utf-8")
        html = html.replace("<app_menu>", utils.get_html_menu())
        html = html.replace("{host}", SERVER_HOST)
        html = html.replace("{current_state_id}", current_state)

        # cartridge_list_html = ""
        cartridge_list_html_template = """<tr>
        <td><input type="checkbox" name="row_state_id" value="{row_state_id}"></td>
        <td><input type="text" name="row_state_id" value="{row_state_id}" disabled></td>
        <td><input type="text" name="model" value="{model}" disabled></td>
        </td>"""

        # rows = data.getCartridgesByState(current_state)
        # for row in rows:
        #     html_row = cartridge_list_html_template
        #     html_row = html_row.replace("{row_state_id}", str(row['row_state_id']))
        #     html_row = html_row.replace("{model}", row['model'])
        #     cartridge_list_html += html_row
        #
        # html = html.replace("<cartridge_list>", cartridge_list_html)

        grouped_rows = data.getCartridgesByStateGrouped(current_state)

        spoiler_list = ""

        spoiler_list_template = Path('http_template/spoiler_list_template.html').read_text(encoding="utf-8")
        for row in grouped_rows:
            html_row = spoiler_list_template
            html_row = html_row.replace("{cartridge_id}", str(row['cartridge_id']))
            html_row = html_row.replace("{model}", row['model'])
            html_row = html_row.replace("{amount}", str(row['amount']))

            cartridges = data.getCartridgesByStateAndCartridge(current_state, row['cartridge_id'])
            cartridge_list_html = "<table border=1>"
            for c_row in cartridges:
                chtml_row = cartridge_list_html_template
                chtml_row = chtml_row.replace("{row_state_id}", str(c_row['row_state_id']))
                chtml_row = chtml_row.replace("{model}", c_row['model'])
                cartridge_list_html += chtml_row
            cartridge_list_html += "</table>"
            html_row = html_row.replace("{cartridge_list}", cartridge_list_html)

            print(row)
            spoiler_list += html_row

        html = html.replace("<spoilers>", spoiler_list)

        print(grouped_rows)

        status_html = ""
        status_html_template = """<option value="{state_id}">{state_name}</option>"""

        rows = data.getStateListLabels()
        for row in rows:
            if int(current_state) != int(row['id']):
                html_row = status_html_template
                html_row = html_row.replace("{state_id}", str(row['id']))
                html_row = html_row.replace("{state_name}", row['state_name'])
                status_html += html_row

        html = html.replace("<status_list>", status_html)

        return html

    # action
    # 0 show new comment form
    # 1 delete by id
    def on_get(self, req, resp, state_id=-1):
        utils = webAnswers.utils.WebUtils()
        token_result = utils.check_cookie_token(req.cookies)
        if token_result:
            resp.content_type = "text/html"
            resp.status = falcon.HTTP_200
            resp.text = self.get_basic_html(state_id)
        else:
            resp.text = "not authorized"

    def on_post(self, req, resp, state_id=-1):
        utils = webAnswers.utils.WebUtils()
        token_result = utils.check_cookie_token(req.cookies)
        resp.content_type = "text/html"
        resp.status = falcon.HTTP_200
        if token_result:
            param = req.media
            action = param['action']
            # action list
            # 0 change status
            # 1 delete

            data = web_db.Db()
            if param['action'] == "0":
                if "row_state_id" in param:
                    if type(param['row_state_id']) is list:
                        for ids in param['row_state_id']:
                            from_state = data.getCurrentCartridgeStateLabel(ids)
                            to_state = data.getStateLabelById(param['new_state'])
                            data.writeToLog("Картридж:" + str(ids) + " " + from_state + " Изменен на " + to_state)
                            data.changeCartridgeState(param['new_state'], ids)
                    else:
                        from_state = data.getCurrentCartridgeStateLabel(param['row_state_id'])
                        to_state = data.getStateLabelById(param['new_state'])
                        data.writeToLog(
                            "Картридж:" + str(param['row_state_id']) + " " + from_state + " Изменен на " + to_state)
                        data.changeCartridgeState(param['new_state'], param['row_state_id'])

            if param['action'] == "1":
                if "row_state_id" in param:
                    if type(param['row_state_id']) is list:
                        for ids in param['row_state_id']:
                            data.deleteCartridgeState(ids)
                    else:
                        data.deleteCartridgeState(param['row_state_id'])

            resp.text = self.get_basic_html(state_id)

        else:
            resp.text = "not authorized"
