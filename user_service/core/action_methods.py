from user_service.conf.environment.config import Config
from user_service.pdf import pdf_genration
from user_service.service_api_handlers import bill_get_handler, \
    complaint_get_handler, complaint_post_handler


def get_my_bill(auth_token, query=None):
    pending_bill = bill_get_handler.get_bill_for_bot(
        auth_token)
     # return jsonify({"bill":get_dict_for_bill_object(pending_bill)})
    if pending_bill:
        filename = pdf_genration.send_pdf(pending_bill)
        return str(filename),'view_pdf'


def complaint_status(auth_token, query=None):
    response = complaint_get_handler.get_complaint_for_bot(auth_token)
    print response.user
    return str(str(response.user.username)+" "+str(response.title)+" "+str(response.complaint_text)+" "+str(response.status)), 'default'

def bill_History(auth_token, query=None):
    pending_bill = bill_get_handler.get_bill_for_bot(auth_token)
    if pending_bill:
        return str(str(pending_bill.user.username)+" "+str(pending_bill.month)+" "+str(pending_bill.last_date)+" "+str(pending_bill.billing_units)+" "+str(pending_bill.bill_amount)+" "+str(pending_bill.is_paid)),'default'

def   bill_History1(auth_token, query=None):
    pending_bill = bill_get_handler.get_bill_for_bot(auth_token)
    if pending_bill:
        return str(pending_bill.last_date),'default'

def complaint_registration_for_bot(auth_token, query=None):

    complaint_post_handler.create_complaint_bot(auth_token, query)
    return 'complaint registered','default'