from flask import request

from user_service.db.user_models.models import LoginEntry, BillingEntry


def get_history(request_data):
    authtoken = request_data['AuthID']
    month = request_data['month']
    try:
        login_object=LoginEntry.objects.get(auth_token=authtoken)
        print login_object.auth_token
        print month
        billing_object=BillingEntry.objects.get(user=login_object.user,month=month)
        print billing_object.month
        return billing_object
    except Exception as e:
        print e
        return None