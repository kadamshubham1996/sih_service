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
        print(bot_response)
        # {"isActionable": True, 'action': "GET_BILL", "answer": None}
        # {"isActionable": False, 'action': None, "answer": "this is my answe"}
        action_data = bot_response['text']
        print(action_data)
        bot_response = ast.literal_eval("{"+action_data+"}")
        is_actionable = bot_response['Action'] != "Default"
        print(is_actionable)
        if is_actionable:
            action = bot_response['Action']
        else:
            return jsonify({"action": 'no_action', "data": bot_response['Msg'],
                            "responseType": "answer"})

        method_call = get_action_map(action)
        data, action = method_call(auth_token)
        return jsonify(
            {"action": action, "data": data})
