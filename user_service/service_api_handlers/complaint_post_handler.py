from user_service.db.user_models.models import Complaint,LoginEntry


def create_complaint(request_data):
    authtoken = request_data['AuthID']
    title=request_data['title']
    complaint_text = request_data['complaint_text']
    try:
        login_object=LoginEntry.objects.get(auth_token=authtoken)
        complaint_object = Complaint.objects.create(user=login_object.user,
                                                    complaint_text=complaint_text)
        return complaint_object
    except Exception as e:
        print e
        return None
