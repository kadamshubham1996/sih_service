from user_service.db.user_models.models import Connection
from user_service.utils.exceptions import GenericCustomException


def create_connection(request_data):
    consumer_type = request_data['consumerType']
    supply_type = request_data['supplyType']
    name = request_data['name']
    email_id = request_data['emailId']
    survey_number = request_data['surveyNumber']
    society_name = request_data['societyName']
    line_no1 = request_data['line_no1']
    line_no2 = request_data['line_no2']
    village = request_data['village']
    taluka = request_data['taluka']
    district = request_data['district']
    state = request_data['state']
    pin_code = request_data['pincode']
    try:
        connection_object = Connection.objects.create(
            consumer_type=consumer_type, supply_type=supply_type,
            name = name,email_id=email_id,
            survey_number=survey_number, society_name=society_name,
            line_no1=line_no1,line_no2=line_no2,
            village=village,taluka=taluka,
            district=district, state=state,pincode=pin_code)


        connection_object.customer_id = "MSEB" + str(
            10000 + connection_object.id)
        connection_object.save()
        return connection_object
    except Exception as e:
        print e
        #raise GenericCustomException(message="Error while creating connection !!")
        return None