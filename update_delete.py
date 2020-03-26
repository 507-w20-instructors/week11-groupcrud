import sqlite3

conn = sqlite3.connect("teachingassignments2.sqlite")
cur = conn.cursor()

drop_instructors = '''
    DROP TABLE IF EXISTS "Instructors";
'''

create_instructors = '''
    CREATE TABLE IF NOT EXISTS "Instructors" (
        "Id"        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        "LastName"  TEXT NOT NULL,
        "FirstName" TEXT NOT NULL,
        "Uniqname"  TEXT NOT NULL,
        "Office"    TEXT
    );
'''

drop_classes = '''
    DROP TABLE IF EXISTS 'Classes'
'''

create_classes = '''
    CREATE TABLE 'Classes' (
    'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'CourseDept' TEXT NOT NULL,
    'CourseNum' INTEGER NOT NULL,
    'TeacherId' INTEGER
    ); 
'''

cur.execute(drop_instructors)
cur.execute(create_instructors)
cur.execute(drop_classes)
cur.execute(create_classes)

conn.commit()

##############################
## INSERT multiple instructors
##############################
instructors = [
    ["Newman", "Mark", "mwnewman", "4380 North Quad"],
    ["Oney", "Steven", "soney", "4366 North Quad"],
    ["Van Lent", "Colleen", "collemc", "715 N. University"],
    ["Adjunct", "Joe", "joeadj", None]
]

insert_instructors = '''
    INSERT INTO Instructors
    VALUES (NULL, ?, ?, ?, ?)
'''

for instr in instructors:
    print("inserting", instr)
    cur.execute(insert_instructors, instr)

conn.commit()

##############################
## UPDATE instructor's office
##############################
update_instructor_office = '''
    UPDATE Instructors
    SET Office = ? 
    WHERE LastName = ?
'''
newman_update = ['4445 North Quad', 'Newman']

cur.execute(update_instructor_office, newman_update)
conn.commit()

##############################
## DELETE by last name
##############################
delete_instructor_by_lastname = '''
    DELETE FROM Instructors
    WHERE LastName = ?
'''
oney_lastname = ["Oney"]

cur.execute(delete_instructor_by_lastname, oney_lastname)
conn.commit()


##############################
## DELETE by Uniqname
##############################
delete_instructor_by_uniqname = '''
    DELETE FROM Instructors
    WHERE Uniqname = ?
'''
adjunct_uniqname = ["joeadj"]

cur.execute(delete_instructor_by_uniqname, adjunct_uniqname)
conn.commit()

##############################
## UPDATE instructor's last name
##############################
update_instructor_name = '''
    UPDATE Instructors
    SET LastName = ? 
    WHERE LastName = ?
'''

newman_update = ['Blueman', 'Newman']

cur.execute(update_instructor_name, newman_update)
conn.commit()