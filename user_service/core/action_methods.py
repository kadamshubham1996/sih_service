from user_service.conf.environment.config import Config
from user_service.pdf import pdf_genration
from user_service.service_api_handlers import bill_get_handler, complaint_get_handler


def get_my_bill(auth_token):
    pending_bill = bill_get_handler.get_bill_for_user(
        auth_token)
    # return jsonify({"bill":get_dict_for_bill_object(pending_bill)})
    if pending_bill:
        path = pdf_genration.send_pdf(pending_bill)
        return Config.service_url+path, 'file'


def get_my_complaint(auth_token):
    response = complaint_get_handler.get_complaint(auth_token)
    return response, 'json'

