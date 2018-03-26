from user_service.db.user_models.models import BillingEntry, LoginEntry


def get_complaint(request_data):
    authtoken = request_data['authToken']
    try:
        login_object=LoginEntry.objects.get(auth_token=authtoken)
        if login_object:
            billing_object = BillingEntry.objects.get(user=login_object.user)
            return billing_object
    except Exception as e:
        print e
        return None