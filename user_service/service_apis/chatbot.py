# from flask import request
# from flask_restful import Resource
#
# from user_service.Bot.chatbot import Bot_get
#
#
# class ChatBot(Resource):
#     def post(self):
#         abc=request.get_json()
#         if abc:
#            Bot_get(abc)
#            return {"success":"success"}
#         else:
#             return {"success1 ":"failse"}