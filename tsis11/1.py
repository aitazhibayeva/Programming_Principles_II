import psycopg2
from config import config


def pattern():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook")
        for contact in cur.fetchall():
            print(f"name: {contact[0]},  surname: {contact[1]}, number: {contact[2]}")
        
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
pattern()