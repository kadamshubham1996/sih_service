from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import history_post_handler, put_pay
from user_service.utils.history_dict_response import history_dict_response


class Bill_History(Resource):
    def post(self):
            # Select month and autopopulate billing info
            request_data = request.get_json()
            history_object = history_post_handler.get_history(request_data)
            if history_object:
                return jsonify({"billing_history": history_dict_response(history_object)})
                #return {"result":"success"}
            else:
                return {"success": False}

    def put(self):
            request_data=request.get_json()
            pay_object=put_pay.pay(request_data)
            if pay_object:
                return {"success":"paid"}
            else:
                return {"success": False}
