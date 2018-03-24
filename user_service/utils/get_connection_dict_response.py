def get_connection_dict_response(connection_object):
    print connection_object
    print "Hackathon...."
    response_dict = {
                     'customerId' : connection_object.customer_id,
                     }

    return response_dict
