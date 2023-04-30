import psycopg2
from config import config

def insert_list(l):
    insert = """
    INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s);
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(insert, (l))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

l = [
    ("name1", "surname1", "+7-777-777-77-77"),
    ("name2", "surname2", "+7-888-888-88-88"),
    ("name3", "surname3", "+7-666-666-66-66"),
]

insert_list(l)