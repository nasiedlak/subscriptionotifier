import yagmail
from keys import FROM_EMAIL, TP_KEY

# function to send email to the notification email address
def send_email(email, subscriptions):
    if(email):
        yag = yagmail.SMTP(FROM_EMAIL, TP_KEY)
        contents = 'Your following subscription(s) are up for renewal:\n\n'
        for sub, date in subscriptions:
            contents += f"{sub} - Renewal Date: {date}\n"
        yag.send(email, 'Subscription Renewal Reminder', contents)