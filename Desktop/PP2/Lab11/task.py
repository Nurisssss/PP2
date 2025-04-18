import psycopg2
import csv

def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="password",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print("[INFO] Connected:", db_version)
        cur.close()
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print("[ERROR] Connection failed:", error)
        return None


def createTable(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS phonebook2 (
            id SERIAL,
            phone VARCHAR(11),
            name VARCHAR(255) UNIQUE
        )
    """
    cursor.execute(query)


def insertData(cursor, name, phone):
    query = """
        INSERT INTO phonebook2 (name, phone)
        VALUES (%s, %s)
        ON CONFLICT (name) DO NOTHING;
    """
    cursor.execute(query, (name, phone))


def getTable(cursor):
    cursor.execute("SELECT * FROM phonebook2")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def updateData(cursor, where, towhat):
    if where.isnumeric():
        query = "UPDATE phonebook2 SET name = %s WHERE phone = %s"
    else:
        query = "UPDATE phonebook2 SET phone = %s WHERE name = %s"
    cursor.execute(query, (towhat, where))


def showData(cursor, select, order):
    query = f'SELECT "{select}" FROM phonebook2 ORDER BY "{order}"'
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def deleteData(cursor, where):
    if where.isnumeric():
        query = "DELETE FROM phonebook2 WHERE phone = %s"
    else:
        query = "DELETE FROM phonebook2 WHERE name = %s"
    cursor.execute(query, (where,))


conn = connect()
if conn is None:
    exit()

cursor = conn.cursor()
createTable(cursor)

print("Type of query: insert, insertbycsv, update, selectinorder, delete")
typ = input().strip()

if typ == "insert":
    n = int(input("Amount of data: "))
    for _ in range(n):
        name = input("Name: ")
        phone = input("Phone: ")
        insertData(cursor, name, phone)

elif typ == "insertbycsv":
    s = input("CSV file name (without .csv): ")
    dataSet = []
    try:
        with open(f"data/{s}.csv", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                name, phone = row[0].split(';')
                insertData(cursor, name, phone)
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")

elif typ == "update":
    where = input("Change in (name or phone): ")
    towhat = input("To: ")
    updateData(cursor, where, towhat)

elif typ == "selectinorder":
    select = input("Select column (name or phone): ")
    order = input("Order by (name or phone): ")
    showData(cursor, select, order)

elif typ == "delete":
    where = input("Delete where name or phone = ")
    deleteData(cursor, where)

conn.commit()
getTable(cursor)
cursor.close()
conn.close()
