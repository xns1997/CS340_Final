# import pymysql
# pymysql.install_as_MySQLdb()

from django.db import connection


data = connection.cursor().execute("SELECT * FROM cs340_xuna.villagers")

print(data)