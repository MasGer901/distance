import sqlite3 as sql


def receiver(city, street, house, Lo1, La1, calculated):
    insert_payment = (city, street, house, Lo1, La1, calculated)
    with sql.connect('service.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO USERS_LOCATION (city, street, house, Lo1, La1, calculated)
                                            VALUES (?,?,?,?,?,?) RETURNING id """
        cursor.execute(query, insert_payment)
        res = next(cursor)
        id = res[0]
        db.commit()
    return id


def calculated():
    with sql.connect('service.db') as db:
        cursor = db.cursor()
        query = """ SELECT * FROM USERS_LOCATION ORDER BY ID"""
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def calculated_id(id):
    with sql.connect('service.db') as db:
        cursor = db.cursor()
        result = cursor.execute(f'SELECT * FROM USERS_LOCATION WHERE id = "{id}"')
        body = cursor.fetchall()
    return body


def delete_calculated(id):
    with sql.connect('service.db') as db:
        cursor = db.cursor()
        cursor.execute(f'DELETE FROM USERS_LOCATION WHERE id = "{id}"')
        db.commit()


with sql.connect('service.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS "USERS_LOCATION" (
	"id"	INTEGER NOT NULL UNIQUE,
	"city"	TEXT NOT NULL,
	"street"	TEXT NOT NULL,
	"house"	INTEGER NOT NULL,
	"Lo1"	REAL NOT NULL,
	"La1"	REAL NOT NULL,
	"calculated"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)"""
