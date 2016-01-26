import MySQLdb
import config

def add(table_name, data_tuple):
    db = MySQLdb.connect(host=config.database.HOST, user=config.database.USER, passwd=config.database.PASSWD, db=config.database.DB)
    cur = db.cursor()

    if table_name == "spending":
        cur.execute("INSERT INTO spending (spend_description, spend_date, spend_amount, account_used) VALUES (%s, %s, %s, %s)", data_tuple)
        db.commit()
        cur.close()

    elif table_name == "bills":
        cur.execute("INSERT INTO bills (bill_name, pay_date, pay_amount) VALUES (%s, %s, %s)", data_tuple)
        db.commit()
        cur.close()

    elif table_name == "accounts":
        cur.execute("INSERT INTO accounts (account_name, account_balance) VALUES (%s, %s)", data_tuple)
        db.commit()
        cur.close()

    db.close()

def edit():
    db = MySQLdb.connect(host=config.database.HOST, user=config.database.USER, passwd=config.database.PASSWD, db=config.database.DB)
    pass

def remove():
    db = MySQLdb.connect(host=config.database.HOST, user=config.database.USER, passwd=config.database.PASSWD, db=config.database.DB)
    pass

def select(table_name):
    db = MySQLdb.connect(host=config.database.HOST, user=config.database.USER, passwd=config.database.PASSWD, db=config.database.DB)
    cur = db.cursor()

    if table_name == "spending":
        pass

    elif table_name == "bills":
        cur.execute("SELECT * FROM bills;")
        db.close()
        return cur.fetchall()

    elif table_name == "accounts":
        pass

