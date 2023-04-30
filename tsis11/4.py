import psycopg2
from config import config

n = input("Enter your query data: ")

def limit(n):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        limit = "SELECT * FROM phonebook LIMIT %s"
        cur.execute(limit, n)
        l = list(cur.fetchall())
        return l
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
def offset(n):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        limit = "SELECT * FROM phonebook OFFSET %s"
        cur.execute(limit, n)
        l = list(cur.fetchall())
        return l
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

l = limit(n)
for i in l:
    print(i)          
            
        
"""l = offset(n)
for i in l:
    print(i)"""