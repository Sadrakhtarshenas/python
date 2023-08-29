import sqlite3

my_data = sqlite3.connect("data_test.db")

cu = my_data.cursor()

try:
    cu.execute("""
    CREATE TABLE customers (
        firstname TEXT,
        lastname TEXT,
        email TEXT
    )
""")
except:
    pass


cu.execute("SELECT * FROM customers")


u_itame = cu.fetchmany(2)



cu.execute("SELECT * FROM customers WHERE firstname LIKE 'a%'")

itames = cu.fetchall()

for i in itames:
    print(i)

cu.execute("UPDATE customers SET firstname = 'ahmad' WHERE firstname = 'kiya'")

cu.execute("DELETE FROM customers WHERE firstname = 'mamad'")

cu.execute("SELECT * FROM customers")

itames = cu.fetchall()
for i in itames:
    print(i)

cu.execute("SELECT * FROM customers ORDER BY firstname DESC")

itames = cu.fetchall()
for i in itames:
    print(i)



itames = cu.fetchall()
for i in itames:
    print(i)

my_data.commit()

my_data.close()