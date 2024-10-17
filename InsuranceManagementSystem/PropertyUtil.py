import pyodbc

class PropertyUtil:
    @staticmethod
    def get_property_string():
        # Define your database connection parameters
        # Use raw strings to avoid escape sequences
        server = r'MUSICLOVER\SQLEXPRESS01'  # SQL Server instance
        database = 'insurance'      # Replace with your database name

        # Use Trusted Connection for Windows Authentication
        connection_string = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'  # This enables Windows Authentication
        )
        return connection_string


class InsuranceServiceImpl:
    def create_policy(self, policy_id, policy_name, policy_details):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Policies (PolicyID, PolicyName, PolicyDetails)
            VALUES (?, ?, ?)
            """
            cursor.execute(insert_query, (policy_id, policy_name, policy_details))
            connection.commit()
            print("Policy created successfully.")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()

    def get_policy(self, policy_id):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_query = "SELECT * FROM Policies WHERE PolicyID = ?"
            cursor.execute(select_query, (policy_id,))
            policy = cursor.fetchone()
            if policy:
                print(f"Policy found: ID: {policy[0]}, Name: {policy[1]}, Details: {policy[2]}")
            else:
                print("Policy not found.")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()

    def get_all_policies(self):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_query = "SELECT * FROM Policies"
            cursor.execute(select_query)
            policies = cursor.fetchall()
            if policies:
                print("All Policies:")
                for policy in policies:
                    print(f"ID: {policy[0]}, Name: {policy[1]}, Details: {policy[2]}")
            else:
                print("No policies available.")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()

    def update_policy(self, policy_id, policy_name, policy_details):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            update_query = """
            UPDATE Policies
            SET PolicyName = ?, PolicyDetails = ?
            WHERE PolicyID = ?
            """
            cursor.execute(update_query, (policy_name, policy_details, policy_id))
            connection.commit()
            print("Policy updated successfully.")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()

    def delete_policy(self, policy_id):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            delete_query = "DELETE FROM Policies WHERE PolicyID = ?"
            cursor.execute(delete_query, (policy_id,))
            connection.commit()
            print("Policy deleted successfully.")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()

    def create_user(self, username, password, role):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Users (Username, Password, Role)
            VALUES (?, ?, ?)
            """
            cursor.execute(insert_query, (username, password, role))
            connection.commit()
            print(f"User {username} created successfully!")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()

    def create_client(self, client_id, client_name, contact_info, policy_id):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Clients (ClientID, ClientName, ContactInfo, PolicyID)
            VALUES (?, ?, ?, ?)
            """
            cursor.execute(insert_query, (client_id, client_name, contact_info, policy_id))
            connection.commit()
            print(f"Client {client_name} created successfully!")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()

    def create_payment(self, payment_date, payment_amount, client_id):
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Payments (PaymentDate, PaymentAmount, ClientID)
            VALUES (?, ?, ?)
            """
            cursor.execute(insert_query, (payment_date, payment_amount, client_id))
            connection.commit()
            print(f"Payment of {payment_amount} created for client ID {client_id}!")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()


def main():
    insurance_service = InsuranceServiceImpl()

    while True:
        print("\nInsurance Management System")
        print("1. Create Policy")
        print("2. Get Policy by ID")
        print("3. Get All Policies")
        print("4. Update Policy")
        print("5. Delete Policy")
        print("6. Add User")
        print("7. Add Client")
        print("8. Add Payment")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            policy_id = int(input("Enter policy ID: "))
            policy_name = input("Enter policy name: ")
            policy_details = input("Enter policy details: ")
            insurance_service.create_policy(policy_id, policy_name, policy_details)

        elif choice == "2":
            policy_id = int(input("Enter policy ID: "))
            insurance_service.get_policy(policy_id)

        elif choice == "3":
            insurance_service.get_all_policies()

        elif choice == "4":
            policy_id = int(input("Enter the policy ID to update: "))
            policy_name = input("Enter new policy name: ")
            policy_details = input("Enter new policy details: ")
            insurance_service.update_policy(policy_id, policy_name, policy_details)

        elif choice == "5":
            policy_id = int(input("Enter the policy ID to delete: "))
            insurance_service.delete_policy(policy_id)

        elif choice == "6":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (e.g., Admin, Client, etc.): ")
            insurance_service.create_user(username, password, role)

        elif choice == "7":
            client_id = int(input("Enter client ID: "))
            client_name = input("Enter client name: ")
            contact_info = input("Enter contact information: ")
            policy_id = int(input("Enter policy ID associated with the client: "))
            insurance_service.create_client(client_id, client_name, contact_info, policy_id)

        elif choice == "8":
            payment_date = input("Enter payment date (YYYY-MM-DD): ")
            payment_amount = float(input("Enter payment amount: "))
            client_id = int(input("Enter client ID for payment: "))
            insurance_service.create_payment(payment_date, payment_amount, client_id)

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
