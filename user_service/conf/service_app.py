import django

from user_service.conf.init_startup import init_startup
from user_service.service_apis.bot import Bot

django.setup()

from flask_restful import Api

from user_service.service_apis.Validate import Validate
from user_service.service_apis.ping import Ping
from user_service.service_apis.user import UserHandler
from user_service.service_apis.login import Login
from user_service.service_apis.logout import Logout
from user_service.service_apis.question import Question
from user_service.service_apis.bill import Bill
from user_service.service_apis.connection import Connection
from user_service.service_apis.complaint import Complaint
# from user_service.service_apis.chatbot import ChatBot
from user_service.service_apis.history import Bill_History

app = init_startup()
api = Api(app)

api.add_resource(Ping, '/ping')
api.add_resource(Bot, '/bot')
api.add_resource(UserHandler, '/user', '/user/<string:username>')
api.add_resource(Login, '/login')
api.add_resource(Logout, "/logout")
api.add_resource(Validate, '/validate')
api.add_resource(Connection, '/connection')
api.add_resource(Question, '/question')
api.add_resource(Bill, "/bill")
api.add_resource(Complaint, "/complaint")
# api.add_resource(ChatBot,"/chat")
api.add_resource(Bill_History, "/bill_history")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
