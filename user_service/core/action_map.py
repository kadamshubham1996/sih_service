from user_service.core.action_methods import get_my_bill, get_my_complaint


def get_action_map(request_string):
    action_map ={
        "SAY_HELLO": "Hello welcome !!",


       "Generate bill pdf": get_my_bill,
    #     # "GET_COMPLAINT": get_my_complaint,
    #     "bill_History":,
    #     "BillLastdate":,
    #     "Screenshot_newConnection":,
    # "complaint_registration":,
    }
    return action_map[request_string]