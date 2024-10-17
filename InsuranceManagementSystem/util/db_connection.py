import mysql.connector
from util.property_util import PropertyUtil

class DBConnection:
    @staticmethod
    def get_connection():
        connection_string = PropertyUtil.get_property_string("db.properties")
        conn = mysql.connector.connect(connection_string)
        return conn
