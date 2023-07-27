import argparse
import sqlite3
import os

import src.db.setup_db as setup_db
import src.db.database as database
import src.utils.verify as verify
import src.utils.email_dispatcher as email_dispatcher

# function to parse command-line argument for adding, removing, and changing the notification email address
def create_parser():
    parser = argparse.ArgumentParser(description = "Manage and notify subscription renewals")
    parser.add_argument('--add', nargs = 2, metavar = ('SUBSCRIPTION', 'DATE'), help = 'Add a new subscription. Date format: YYYY-MM-DD')
    parser.add_argument('--remove', metavar = 'SUBSCRIPTION', help = 'Remove a subscription.')
    parser.add_argument('--email', metavar = 'EMAIL', help = 'Set the notification email.')
    return parser

def main():
    # initial setup, ran once
    if(not os.path.exists('subscriptions.db')):
        # connect to database
        conn = sqlite3.connect('subscriptions.db')
        c = conn.cursor()

        # setup the tables
        setup_db.setup_db()

        # welcome messages
        print("Welcome to your personal subscription reminder service! You will be notified two days in advance before any active subscription renews.")
        print("Enter an active subscription in the following format:")
        print("subscription_name renewal_date")
        print("The name should be one word, and the renewal date should have the format DD-MM (e.g., YouTube 7/20)")
        print("Enter 'done' when finished.")

        # user-input subscription loop
        while(True):
            # get and verify user input
            user_input = input("Subscription: ")
            if(user_input.lower() == 'done'):
                break

            # verify input format
            if(len(user_input.split()) != 2):
                print("Invalid format. Please enter in the format,")
                print("subscription_name renewal_date")
                continue

            # split the name of renewal date of the subscription
            subscription, date = user_input.split()

            # verify renewal date format
            renewal_date = verify.verify_subscription_date(date)
            if(renewal_date == ""):
                print("Invalid renewal date format. Please enter with the format MM-DD.")
                continue

            # add the subscription to the database
            database.add_subscription(subscription, renewal_date, c)
        
        # acquire and verify notification email address
        while(True):
            email = input("Enter an email address at which to receive notifications: ")
            if(verify.verify_email(email)):
                # add the notification email address to the database
                database.set_email(email, c)
                break
            print("Invalid email address input format. Please enter only one valid email address.")
        
        # additional information regarding subscription adding and removing
        print("You are all set. Use '--add', '--remove', and '--email' to manage your subscriptions.")
        print("Run 'python3 subscription-tracker.py --help' for additional information")
    else:
        # connect to database
        conn = sqlite3.connect('subscriptions.db')
        c = conn.cursor()
    
    # argument parser setup
    parser = create_parser()
    args = parser.parse_args()

    # add a new subscription
    if(args.add):
        subscription, date = args.add
        renewal_date = verify.verify_subscription_date(date)
        if(renewal_date == ""):
            print("Invalid renewal date format. Please enter with the format MM-DD.")
        else:
            database.add_subscription(subscription, renewal_date, c)
    # remove an existing subscription
    elif(args.remove):
        all_subs = set(database.get_subscriptions(c))
        subscription = args.remove
        if(subscription not in all_subs):
            print("Subscription does not exist.")
        else:
            database.remove_subscription(subscription, c)
    # set notification email address
    elif(args.email):
        email = args.email
        if(not verify.verify_email(email)):
            print("Invalid email address input format. Please enter only one valid email address.")
        else:
            database.update_email(email, database.get_email(c), c)
    else:
        # daily check to see if there are any renewals within two days
        email = database.get_email(c)
        subscriptions = database.get_renewals(c)
        if(len(subscriptions)):
            email_dispatcher.send_email(email, subscriptions)
    
    # close connection
    conn.commit()

if __name__ == "__main__":
    main()


    