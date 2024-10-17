import pyodbc

class PropertyUtil:
    @staticmethod
    def get_property_string():
        # Define your database connection parameters
        server = r'MUSICLOVER\SQLEXPRESS01'  # SQL Server instance
        database = 'insurance'      # Replace with your database name

        # Use Trusted Connection for Windows Authentication
        connection_string = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'        # This enables Windows Authentication
        )

        return connection_string

    @staticmethod
    def check_connection():
        connection_string = PropertyUtil.get_property_string()
        try:
            connection = pyodbc.connect(connection_string)
            connection.close()
            return True  # Connection successful
        except Exception as e:
            print("Connection failed:", e)
            return False  # Connection failed
