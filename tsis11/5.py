import psycopg2
from config import config

name = input("Enter the name which you want to delete: ")

def delete(name):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook")
        for data in cur.fetchall():
            if data[0] == name:
                dl = """
                    DELETE FROM phonebook
                    WHERE first_name = %s;
                """
                cur.execute(dl, [name])
                conn.commit()
                cur.close()
                exit()
        print(f"Phonebook haven't contact = {name}")
            
    except Exception as e:
        print(f"[INFO ERROR] {str(e)} !!!")
    finally:
        if conn is not None:
            conn.close()
            
delete(name)