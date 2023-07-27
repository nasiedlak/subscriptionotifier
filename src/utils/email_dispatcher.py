import yagmail

# function to send email to the notification email address
def send_email(email, subscriptions):
    if(email):
        yag = yagmail.SMTP('csubnotifier@gmail.com', 'zfgeueushtkmwgls')
        contents = 'Your following subscription(s) are up for renewal:\n\n'
        for sub, date in subscriptions:
            contents += f"{sub} - Renewal Date: {date}\n"
        yag.send(email, 'Subscription Renewal Reminder', contents)