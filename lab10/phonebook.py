import psycopg2
import csv



conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="iskanderb4",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


cur.execute("TRUNCATE TABLE phonebook RESTART IDENTITY") # necessary
conn.commit()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    phone VARCHAR(20) UNIQUE
)
""")
conn.commit()

def phone_exists(phone):
    cur.execute("SELECT 1 FROM phonebook WHERE phone = %s", (phone,))
    return cur.fetchone() is not None

def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not phone_exists(row['phone']):
                cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row['first_name'], row['phone']))
    conn.commit()

def insert_from_console():
    name = input("enter name: ")
    phone = input("enter phone: ")
    if not phone_exists(phone):
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
    else:
        print("This phone number already exists.")

def update_name_by_phone(old_phone, new_name):
    cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", (new_name, old_phone))
    conn.commit()

def update_phone_by_name(name, new_phone):
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()

def query_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def query_by_name(name):
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    print(cur.fetchall())

def query_by_phone_partial(partial):
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (partial + '%',))
    print(cur.fetchall())

def delete_by_name(name):
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    conn.commit()

def delete_by_phone(phone):
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

# uncomment if u need to run
insert_from_csv("phonebook.csv")
insert_from_console()
update_name_by_phone("123456789", "UpdatedName")
update_phone_by_name("UpdatedName", "999888777")
query_all()
query_by_name("UpdatedName")
query_by_phone_partial("999")
delete_by_name("UpdatedName")
delete_by_phone("999888777")


cur.close()
conn.close()
