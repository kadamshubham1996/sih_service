from user_service.db.user_models.models import LoginEntry, BillingEntry


def get_history(request_data):
    authtoken = request_data['AuthID']
    date = request_data['month']
    try:
        login_object=LoginEntry.objects.get(auth_token=authtoken)
        billing_object = BillingEntry.objects.get(user=login_object.user,
                                                    month=date)
        return billing_object
    except Exception as e:
        print e
        return None