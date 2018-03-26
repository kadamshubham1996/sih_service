from flask import request, jsonify
from flask_restful import Resource

from user_service.conf.environment.config import Config
from user_service.pdf import pdf_genration
from user_service.pdf.pdf_genration import send_pdf
from user_service.service_api_handlers import bill_post_handler, \
    bill_get_handler
from user_service.utils.billing_entry_method import get_dict_for_bill_object


class Bill(Resource):
    def post(self):
        request_data = request.get_json()
        bill_object = bill_post_handler.bill_entry(request_data)
        if bill_object:
            return None
        else:
            return {"success": False}

    def get(self):
        auth_token = request.headers.get('authToken')
        pending_bill = bill_get_handler.get_bill_for_user(
            auth_token)
        # return jsonify({"bill":get_dict_for_bill_object(pending_bill)})
        if pending_bill:
            path = pdf_genration.send_pdf(pending_bill)
            return jsonify({"success": True, "billPath": Config.service_url+path})


    def put(self):
        pass

