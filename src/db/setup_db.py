import sqlite3

def setup_db():
    conn = sqlite3.connect('subscriptions.db')

    c = conn.cursor()

    c.execute('''
        CREATE TABLE subscriptions (
            name TEXT PRIMARY KEY,
            renewal_date TEXT NOT NULL
        )
    ''')
            
    c.execute('''
        CREATE TABLE email (
            address TEXT PRIMARY KEY
        )
    ''')

    conn.commit()

    conn.close()

if __name__ == "__main__":
    setup_db()