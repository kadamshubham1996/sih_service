from user_service.db.user_models.models import Complaint,User


def create_complaint(request_data):
    username = request_data['username']
    complaint_text = request_data['complaint_text']
    try:
        user_object=User.objects.get(username=username)
        if user_object:
            complaint_object = Complaint.objects.create(user=user_object,
                                                    complaint_text=complaint_text)
            return complaint_object
    except Exception as e:
        print e
        return None
