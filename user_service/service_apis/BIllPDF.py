from flask_restful import Resource
from flask import send_from_directory

class ViewPDF(Resource):
    def get(self,filename):
        return send_from_directory('/home/rckstr/work/hackathon_user_service-master/user_service/pdf/static/',str(filename))



