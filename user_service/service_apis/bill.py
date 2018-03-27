from flask import request, jsonify
from flask_restful import Resource

from user_service.conf.environment.config import Config
from user_service.pdf import pdf_genration
from user_service.pdf.pdf_genration import send_pdf
from user_service.service_api_handlers import bill_post_handler, \
    bill_get_handler
from user_service.utils.billing_entry_method import get_dict_for_bill_object


class Bill_Pdf_Display(Resource):
    def get(self):
        # Admin hits this api
        request_data = request.get_json()
        bill_object = bill_post_handler.bill_entry(request_data)
        if bill_object:
            return None
        else:
            return {"success": False}

    def post(self):
        # Generate PDF and returns PDF URL to view
        auth_token = request.headers.get('authToken')
        request_data=request.get_json()
        pending_bill = bill_get_handler.get_bill_for_user(
            auth_token,request_data)
        if pending_bill:
            fileName = pdf_genration.send_pdf(pending_bill)
            return jsonify({"success": True, "billPath": fileName})

    # def put(self):
    #     request_data = request.get_json()
    #     history_object = history_post_handler.get_history(request_data)
    #     if history_object:
    #         return jsonify(
    #             {"billing_history": history_dict_response(history_object)})
    #         # return {"result":"success"}
    #     else:
    #         return {"success": False}
