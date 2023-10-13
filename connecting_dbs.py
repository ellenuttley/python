import mysql.connector
from config import USER, PASSWORD, HOST

class DBConnectionFailed(Exception):
    pass

def connect_mysql(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=db_name
    )
    return cnx

def get_all_records():
    try:
        db_name = 'tests'
        db_connection = connect_mysql(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM abcreport"""
        cur.execute(query)
        results = cur.fetchall()
        for record in results:
            print(record)
        cur.close()
    except Exception:
        raise DBConnectionFailed("Failed to read data from database")
    finally:
        if db_connection:
            db_connection.close()

def calc_com():
    sales = []
    for item in sold_items:
        sales.append(item[2])
    commission = sum(sales) + (commission/100)
    return commission

def rep_records(rep_name):
    try:
        db_name = 'tests'
        db_connection = connect_mysql(db_name)
        cur = db_connection.cursor()
        query = """'SELECT Item, Units, Total FROM abcreport WHERE Rep={}'"""
        cur.execute(query)
        results = cur.fetchall()
        for record in results:
            print(record)
        cur.close()
        comp = round(calc_com(results, commission=10), 2)
    except Exception:
        raise DBConnectionFailed("Failed to read data from database")
    finally:
        if db_connection:
            db_connection.close()
    print(f"Commission for {rep_name} is {comp}")
    return rep_name, comp

def main():
    get_all_records()
    rep_records("Jones")

    pass

if __name__ == '__main__':
    main()
