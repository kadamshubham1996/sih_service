from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handlers import complaint_post_handler, complaint_get_handler
from user_service.utils.complaint_get_dict import complaint_get_dict


class Complaint(Resource):
    def post(self):
            request_data = request.get_json()
            complaint_object = complaint_post_handler.create_complaint(request_data)
            if complaint_object:
                return jsonify({"Complaint": "success"})

            else:
                return {"success": False}


    def get(self):
        request_data = request.get_json()
        complaint_object= complaint_get_handler.get_complaint(request_data)
        if complaint_object:
            return jsonify({"Complaint": complaint_get_dict(complaint_object)})

        else:
            return {"success": False}