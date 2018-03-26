
from user_service.utils.sms_utils import send_sms
def create_OTP(request_data):
    phone=request_data['phone']
    object = str(1000 + 3)
    sms_utlis.send_sms(phone,object)
    return True