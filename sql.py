import MySQLdb
import config

db = MySQLdb.connect(host=config.database.HOST, user=config.database.USER, passwd=config.database.PASSWD, db=config.database.DB)
c = db.cursor()

def add(table_name, data_tuple):
    if table_name == "spending":
        c.execute("INSERT INTO spending (

    if table_name == "bills":
        pass

    if table_name == "accounts":
        pass

db.close()
