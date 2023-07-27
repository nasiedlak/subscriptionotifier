from datetime import datetime, timedelta

# function to add a new subscription to the subscriptions database
def add_subscription(subscription, date, cursor):
    cursor.execute('INSERT INTO subscriptions VALUES (?, ?)', (subscription, date))

# function to remove an existing subscription from the subscriptions database
def remove_subscription(subscription, cursor):
    cursor.execute('DELETE FROM subscriptions WHERE name = ?', (subscription,))

def get_subscriptions(cursor):
    cursor.execute('SELECT * FROM subscriptions')
    return cursor.fetchall()

# function to set the notification email address
def set_email(email, cursor):
    cursor.execute('INSERT OR REPLACE INTO email VALUES (?)', (email,))

def update_email(new_email, old_email, cursor):
    print(old_email, new_email)
    cursor.execute('DELETE FROM email WHERE address = ?', (old_email,))
    cursor.execute('INSERT INTO email (address) VALUES (?)', (new_email,))

# function to get the notification email address
def get_email(cursor):
    cursor.execute('SELECT address FROM email')
    result = cursor.fetchone()
    return result[0] if result else None

# function to get all subscription to be renewed within the next two days
def get_renewals(cursor):
    today = datetime.now().date()
    in_two_days = today + timedelta(days = 2)
    cursor.execute('SELECT * FROM subscriptions WHERE date(renewal_date) BETWEEN ? AND ?', (today, in_two_days))
    return cursor.fetchall()