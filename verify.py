import re
from datetime import datetime

def verify_subscription_date(date):
    try:
        month, day = map(int, date.split('-'))
        renewal_date = datetime(datetime.now().year, month, day).strftime('%Y-%m-%d')
        return renewal_date
    except ValueError:
        return ""

def verify_email(email):
    if(len(email.split()) != 1 or not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)):
        return False
    return True