import sqlite3
import csv

laptops = []
with open("laptops.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        laptops.append(tuple(row))

connect = sqlite3.connect("mobileandlaptap.db")
data = connect.cursor() 
data.execute("""
    CREATE TABLE mobile (
            brand TEXT,
            name TEXT,
            year TEXT,
            ram TEXT,
            camera TEXT,
            price TEXT
    )
""")
data.execute("""
    CREATE TABLE laptop(
            Manufacturer TEXT,
            Brand TEXT,
            Category TEXT,
            Scrreen_Size TEXT,
            Screen TEXT,
            CPU TEXT,
            RAM TEXT,
            Storage TEXT,
            GPU TEXT,
            Op_System TEXT,
            Op_System_Version TEXT,
            Weight TEXT,
            Price TEXT
    )
""")
customers = [("Apple1", "iPad Pro 12.9 (2018)", "2018", "4 GB", "12 MP", "1100 EUR"),
            ("Apple2", "iPad Pro 11", "2018", "4 GB", "12 MP", "880 EUR"),
            ("Apple3", "iPhone XS Max", "2018", "4 GB", "12 MP", "1250 EUR"),
            ("Apple4", "iPhone XS", "2018", "4 GB", "12 MP", "1150 EUR"),
            ("Apple5", "iPhone XR", "2018", "3 GB", "12 MP", "850 EUR"),
            ("Apple6", "Watch Series 4", "2018", "0 GB", "No", "700 EUR"),
            ("Apple7", "Watch Series 4 Aluminum", "2018", "0 GB", "No", "430 EUR"),
            ("Apple8", "iPad 9.7 (2018)", "2018", "2 GB", "8 MP", "350 EUR"),
            ("Apple9", "iPhone X", "2017", "3 GB", "12 MP", "1000 EUR"),
            ("Apple10", "iPhone 8 Plus", "2017", "3 GB", "12 MP", "770 EUR"),
            ("Apple11", "iPhone 8", "2017", "2 GB", "12 MP", "700 EUR"),
            ("Apple12", "Watch Edition Series 3", "2017", "0.768 GB", "No", "1450 EUR"),
            ("Apple13", "Watch Series 3", "2017", "0.768 GB", "No", "700 EUR"),
            ("Apple14", "Watch Series 3 Aluminum", "2017", "0.768 GB", "No", "480 EUR"),
            ("Apple15", "iPad Pro 12.9 (2018)", "2018", "4 GB", "12 MP", "1100 EUR"),
            ("Apple16", "iPad Pro 11", "2018", "4 GB", "12 MP", "880 EUR"),
            ("Apple17", "iPhone XS Max", "2018", "4 GB", "12 MP", "1250 EUR"),
            ("Apple18", "iPhone XS", "2018", "4 GB", "12 MP", "1150 EUR"),
            ("Apple19", "iPhone XR", "2018", "3 GB", "12 MP", "850 EUR"),
            ("Apple20", "Watch Series 4", "2018", "0 GB", "No", "700 EUR"),
            ("Apple21", "Watch Series 4 Aluminum", "2018", "0 GB", "No", "430 EUR"),
            ("Apple22", "iPad 9.7 (2018)", "2018", "2 GB", "8 MP", "350 EUR"),
            ("Apple23", "iPhone X", "2017", "3 GB", "12 MP", "1000 EUR"),
            ("Apple24", "iPhone 8 Plus", "2017", "3 GB", "12 MP", "770 EUR"),
            ("Apple25", "iPhone 8", "2017", "2 GB", "12 MP", "700 EUR"),
            ("Apple26", "Watch Edition Series 3", "2017", "0.768 GB", "No", "1450 EUR"),
            ("Apple27", "Watch Series 3", "2017", "0.768 GB", "No", "700 EUR"),
            ("Apple28", "Watch Series 3 Aluminum", "2017", "0.768 GB", "No", "480 EUR"),
            ("Apple29", "iPad Pro 12.9 (2017)", "2017", "4 GB", "12 MP", "900 EUR"),
            ("Apple30", "iPad Pro 10.5 (2017)", "2017", "4 GB", "12 MP", "730 EUR"),
            ("Apple31", "iPad 9.7 (2017)", "2017", "2 GB", "8 MP", "390 EUR"),
            ("Apple32", "Watch Edition Series 2 42mm", "2016", "0.512 GB", "No", "1500 EUR"),
            ("Apple33", "Watch Series 2 42mm", "2016", "0.512 GB", "No", "700 EUR"),
            ("Apple34", "Watch Edition Series 2 38mm", "2016", "0.512 GB", "No", "1450 EUR"),
            ("Apple35", "Watch Series 2 38mm", "2016", "0.512 GB", "No", "650 EUR"),
            ("Apple36", "Watch Series 2 Aluminum 42mm", "2016", "0.512 GB", "No", "450 EUR"),
            ("Apple37", "Watch Series 1 Aluminum 42mm", "2016", "0.512 GB", "No", "300 EUR"),
            ("Apple38", "Watch Series 2 Aluminum 38mm", "2016", "0.512 GB", "No", "420 EUR"),
            ("Apple39", "Watch Series 1 Aluminum 38mm", "2016", "0.512 GB", "No", "270 EUR"),
            ("Apple40", "iPhone 7 Plus", "2016", "3 GB", "12 MP", "690 EUR"),
            ("Apple41", "iPhone 7", "2016", "2 GB", "12 MP", "550 EUR"),
            ("Apple42", "iPad Pro 9.7 (2016)", "2016", "2 GB", "12 MP", "690 EUR"),
            ("Apple43", "iPhone SE", "2016", "2 GB", "12 MP", "300 EUR"),
            ("Apple44", "iPhone 6s Plus", "2015", "2 GB", "12 MP", "470 EUR"),
            ("Apple45", "iPhone 6s", "2015", "2 GB", "12 MP", "500 EUR"),
            ("Apple46", "iPad Pro 12.9 (2015)", "2015", "4 GB", "8 MP", "850 EUR"),
            ("Apple47", "iPad mini 4.1", "2015", "2 GB", "8 MP", "3360 EUR"),
            ("Apple48", "Watch Edition 42mm (1st gen)", "2014", "0.512 GB", "No", "13000 EUR"),
            ("Apple49", "Watch Edition 38mm (1st gen)", "2014", "0.512 GB", "No", "11000 EUR"),
            ("Apple50", "Watch 42mm (1st gen)", "2014", "0.512 GB", "No", "700 EUR"),
            ("Apple51", "Watch 38mm (1st gen)", "2014", "0.512 GB", "No", "650 EUR"),
            ("Apple52", "Watch Sport 42mm (1st gen)", "2014", "0.512 GB", "No", "250 EUR"),
            ("Apple53", "Watch Sport 38mm (1st gen)", "2014", "0.512 GB", "No", "250 EUR"),
            ("Apple54", "iPad Air 2", "2014", "2 GB", "8 MP", "440 EUR"),
            ('Apple', 'iPhone 14 Plus', "2022", '6 GB', "120p", '4000 EUR'),
            ('Apple', 'iPhone 14 Pro Max', "2022", '6 GB', '1080p', '5900 EUR'),
            ('Apple', 'iPhone 13 mini', "2021", '4 GB','1080p', '5000 EUR'),
            ('Apple', 'iPhone 11 Pro', "2019", '4 GB', '1080p', '4500 EUR')]
# add apple phon in list
for i in customers:
    connect.execute("INSERT INTO mobile VALUES (?, ?, ?, ?, ?, ?)", i)
# add laptops in list
for i in laptops:
    connect.execute("INSERT INTO laptop VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", i)

data.execute("SELECT * FROM mobile WHERE year >= '2017'")
itames = data.fetchall()
for i in itames:
    print(i)
data.execute("DELETE FROM laptop WHERE RAM <= '4'")
data.execute("SELECT CPU FROM laptop WHERE RAM > '4'")
for i in data.fetchall():
    print(i)

print("_________________________________")
data.execute("SELECT * FROM laptop ORDER BY RAM DESC")
items = data.fetchall()
c = 0
for i in items:
    print(i)
    c+=1
    if c == 5:
        break

data.execute("SELECT * FROM mobile WHERE Price > '500'")
for i in data.fetchall():
    print(i)

data.execute("SELECT * FROM laptop WHERE Price > '10000'")
for i in data.fetchall():
    print(i)
# delet tabels in
connect.commit()
connect.close()