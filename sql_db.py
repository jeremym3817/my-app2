import sqlite3
import requests
import json

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS CLASSES")
# Creating table, (maybe Class time is in datetime format)

table = """ CREATE TABLE CLASSES(
        ID PRIMARY KEY,
        Section_Name VARCHAR(10) NOT NULL,
        Name VARCHAR(255) NOT NULL,
        Year_Taken INT NOT NULL, 
        Class_Size INT NOT NULL,
        Class_Time VARCHAR(255) NOT NULL,
        Professor VARCHAR(50) NOT NULL,
        Difficulty INT NOT NULL
        );"""
cur.execute(table)
con.commit()

#'2007-01-01 10:00:00'
#yyyy-MM-dd HH:mm:ss
cur.execute("""
    INSERT INTO CLASSES VALUES
    (0, "CS_2500", 'Intro to Software', 1, 214, "2021-01-01 08:30:00", "Dr.Steven Bar", 8.2),
    (1, "CS_3500", 'Algorithm Class', 3, 201, "2021-01-01 011:00:00", "David Cerna", 1.2)
        """)
con.commit()
res = cur.execute("SELECT * FROM CLASSES")
print(res.fetchall()[1])

for i in range(len(res.fetchall())):
    message = {
        f'{i}': res.fetchall()[i]
    }
# print(message)
# def createJSON()
# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()

# for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
#     print(row)

# con.close()
# new_con = sqlite3.connect("tutorial.db")
# new_cur = new_con.cursor()
# res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
# title, year = res.fetchone()
# print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')



#importing json

# Creating the outline for the json converter in python
# import json

# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32
# }

# with open('data.json', 'w', encoding='utf-8') as f:
#   json.dump(data, f, ensure_ascii=False, indent=4)