import pyodbc
from dao.ipolicy_service import IPolicyService
from entity.policy import Policy
from entity.user import User
from entity.client import Client
from entity.payment import Payment
from property_util import PropertyUtil  # Assuming PropertyUtil is defined to get connection details

class InsuranceServiceImpl(IPolicyService):
    def __init__(self):
        self.policies = []  # List to store policy objects
        self.users = []     # List to store user objects
        self.clients = []   # List to store client objects
        self.payments = []  # List to store payment objects

    def create_policy(self, policy: Policy) -> bool:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Policies (PolicyName, PolicyDetails)
            VALUES (?, ?)
            """
            cursor.execute(insert_query, (policy.policyName, policy.policyDetails))
            connection.commit()
            print("Policy created successfully.")
            self.policies.append(policy)
            return True

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            cursor.close()
            connection.close()

    def get_policy(self, policy_id: int) -> Policy:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_query = "SELECT * FROM Policies WHERE PolicyID = ?"
            cursor.execute(select_query, (policy_id,))
            policy = cursor.fetchone()
            if policy:
                return Policy(policyId=policy[0], policyName=policy[1], policyDetails=policy[2])
            else:
                raise PolicyNotFoundException("Policy not found")

        except Exception as e:
            print("Error:", e)
            return None

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
            return [Policy(policyId=policy[0], policyName=policy[1], policyDetails=policy[2]) for policy in policies]

        except Exception as e:
            print("Error:", e)
            return []

        finally:
            cursor.close()
            connection.close()

    def update_policy(self, policy: Policy) -> bool:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            update_query = """
            UPDATE Policies
            SET PolicyName = ?, PolicyDetails = ?
            WHERE PolicyID = ?
            """
            cursor.execute(update_query, (policy.policyName, policy.policyDetails, policy.policyId))
            connection.commit()
            print("Policy updated successfully.")
            return True

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            cursor.close()
            connection.close()

    def delete_policy(self, policy_id: int) -> bool:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            delete_query = "DELETE FROM Policies WHERE PolicyID = ?"
            cursor.execute(delete_query, (policy_id,))
            connection.commit()
            print("Policy deleted successfully.")
            return True

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            cursor.close()
            connection.close()

    def create_user(self, user: User) -> bool:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Users (Username, Password, Role)
            VALUES (?, ?, ?)
            """
            cursor.execute(insert_query, (user.username, user.password, user.role))
            connection.commit()
            print(f"User {user.username} created successfully!")
            self.users.append(user)
            return True

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            cursor.close()
            connection.close()

    def create_client(self, client: Client) -> bool:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Clients (ClientName, ContactInfo, PolicyID)
            VALUES (?, ?, ?)
            """
            # Use getter methods to access client attributes
            cursor.execute(insert_query, (client.get_clientName(), client.get_contactInfo(), client.get_policyId()))
            connection.commit()
            print(f"Client {client.get_clientName()} created successfully!")  # Use getter method
            self.clients.append(client)  # Also store in memory if needed
            return True

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            cursor.close()
            connection.close()

    def get_client(self, client_id: int) -> Client:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            select_query = "SELECT * FROM Clients WHERE ClientID = ?"
            cursor.execute(select_query, (client_id,))
            client_data = cursor.fetchone()

            if client_data:
                return Client(clientId=client_data[0],
                              clientName=client_data[1],
                              contactInfo=client_data[2],
                              policyId=client_data[3])
            else:
                print("Client not found.")
                return None

        except Exception as e:
            print("Error:", e)
            return None

        finally:
            cursor.close()
            connection.close()

    def create_payment(self, payment: Payment) -> bool:
        connection_string = PropertyUtil.get_property_string()

        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO Payments (PaymentDate, PaymentAmount, ClientID)
            VALUES (?, ?, ?)
            """
            cursor.execute(insert_query, (payment.payment_date, payment.payment_amount, payment.client.get_clientId()))
            connection.commit()
            print(f"Payment of {payment.payment_amount} created for client {payment.client.get_clientName()}!")  # Ensure this is correct
            self.payments.append(payment)
            return True

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            cursor.close()
            connection.close()
