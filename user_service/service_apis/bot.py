from flask import request, jsonify
from flask_restful import Resource
import ast
from user_service.core.action_map import get_action_map
from user_service.utils import chat_bot


class Bot(Resource):
    def post(self):
        # import pdb;pdb.set_trace()
        request_data = request.get_json()
        auth_token = request.headers.get('authToken')
        query = request_data['query']
        bot_response = chat_bot.get_resopnse_from_bot(query)

        # {"isActionable": True, 'action': "GET_BILL", "answer": None}
        # {"isActionable": False, 'action': None, "answer": "this is my answe"}
        action_data = bot_response['text']
        bot_response = ast.literal_eval(action_data)
        is_actionable = bot_response['isActionable']
        action = None
        if is_actionable:
            action = bot_response['action']
        else:
            return jsonify({"action": None, "data": action['answer'],
                            "responseType": "answer"})

        method_call = get_action_map(action)
        response, response_type = method_call(auth_token)
        return jsonify(
            {"action": action, "data": response, "responseType": response_type})
