import psycopg2
from config import config

name = input("Enter new name: ")
surname = input("Enter new surname: ")
number = input("Enter phone number: ")

def insert_update(name, surname, numder):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook")
        for contact in cur.fetchall():
            if contact[0] == name:
                update = """
                UPDATE phonebook SET
                phone_number = %s 
                where first_name = %s
                """
                cur.execute(update, (number, name))
                conn.commit()
                cur.close()
                exit()
        insert = """
        INSERT INTO 
        phonebook(first_name, last_name, phone_number)
        VALUES(%s, %s, %s)
        """
        cur.execute(insert, (name, surname, number))
        conn.commit()
        cur.close()
        
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
insert_update(name, surname, number)