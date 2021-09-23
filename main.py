# examples/things.py

# Let's get this party started!
from wsgiref.simple_server import make_server

import falcon
from answers import signin
import answers.checktoken
import answers.printer_model
import answers.printer
import answers.signin
import answers.cartridge_model
import answers.cartridge_model_dep
import answers.cartridge_base_state
import answers.cartridge_state_list
import answers.cartridge_state

import webAnswers.index
import webAnswers.main
import webAnswers.printer_model
import webAnswers.printer_list
import webAnswers.cartridge_model
import webAnswers.base_state
import webAnswers.state


# ######################################
# # disable cross origin for swagger api test
# from falcon_cors import CORS
# cors = CORS(
#     allow_all_origins=True,
#     allow_all_headers=True,
#     allow_all_methods=True,
# )
# app = falcon.API(middleware=[cors.middleware])

#######################################
# main workflow
app = falcon.App()

# app.req_options.auto_parse_form_urlencoded = True
# android
app.add_route('/signin', answers.signin.SignIn())
app.add_route('/checkToken', answers.checktoken.CheckToken())
app.add_route('/printerModel', answers.printer_model.PrinterModel())
app.add_route('/printerModel/{id}', answers.printer_model.PrinterModel())
app.add_route('/printer', answers.printer.Printer())
app.add_route('/printer/{id}', answers.printer.Printer())
app.add_route('/cartridgeModel', answers.cartridge_model.CartridgeModel())
app.add_route('/cartridgeModel/{id}', answers.cartridge_model.CartridgeModel())
app.add_route('/cartridgeModel/model_dep', answers.cartridge_model_dep.CartridgeModelDep())
app.add_route('/cartridgeModel/model_dep/{id}', answers.cartridge_model_dep.CartridgeModelDep())
app.add_route('/cartridgeBaseState', answers.cartridge_base_state.CartridgeBaseState())
app.add_route('/cartridgeStateList', answers.cartridge_state_list.CartridgeStateList())
app.add_route('/cartridgeState/{state_id}', answers.cartridge_state.CartridgeState())
app.add_route('/cartridgeState', answers.cartridge_state.CartridgeState())

# web
app.add_route('/', webAnswers.index.WebIndex())
app.add_route('/main', webAnswers.main.WebMain())
app.add_route('/printer_model', webAnswers.printer_model.WebPrinterModel())
app.add_route('/printer_list', webAnswers.printer_list.WebPrinterList())
app.add_route('/printer_list/{action_id}/{edit_id}', webAnswers.printer_list.WebPrinterList())
app.add_route('/cartridge_model', webAnswers.cartridge_model.WebCartridgeModel())
app.add_route('/base_state', webAnswers.base_state.WebBaseState())
app.add_route('/state/{state_id}', webAnswers.state.WebState())

# todo 
# некоторые запросы используют несколько подключений к mysql что не есть хорошо
# можно добавить инверсию зависимостей и прокидывать подключение

# updateCartridgeModelDep дохрена запросов, можно как то оптимизировать

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
