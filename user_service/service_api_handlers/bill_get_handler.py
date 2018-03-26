from datetime import datetime
from user_service.db.user_models.models import BillingEntry, LoginEntry


def get_bill_for_user(auth_key):
    login_entry=LoginEntry.objects.get(auth_token=auth_key)
    pending_bills = BillingEntry.objects.filter(user=login_entry.user,is_paid=False)
    # last_bill = None
    # for bill in pending_bills:
    #     if bill.month.month == datetime.now().month:
    #         last_bill = pending_bills
    return pending_bills
