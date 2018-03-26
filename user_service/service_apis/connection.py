from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import new_connection_post_handler
from user_service.utils.get_connection_dict_response import \
    get_connection_dict_response
from user_service.utils.send_customerid_methods import send_customerid_email


class Connection(Resource):
    def post(self):
        request_data = request.get_json()
        print request_data
        connection_object = new_connection_post_handler.create_connection(request_data)
        send_customerid_email(connection_object)
        print connection_object.customer_id
        return {"result":"hello"}

