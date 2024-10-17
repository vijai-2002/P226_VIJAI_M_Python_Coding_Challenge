from dao.insurance_service_impl import InsuranceServiceImpl
from entity.policy import Policy
from entity.user import User
from entity.client import Client
from entity.payment import Payment
from property_util import PropertyUtil  # Import PropertyUtil

def main():
    # Check if connection to the database is successful
    if not PropertyUtil.check_connection():
        print("Unable to connect to the database. Exiting...")
        return
    else:
        print("Connection successful")

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
            # Create a new policy
            policy_id = int(input("Enter policy ID: "))
            policy_name = input("Enter policy name: ")
            policy_details = input("Enter policy details: ")

            new_policy = Policy(policyId=policy_id, policyName=policy_name, policyDetails=policy_details)

            if insurance_service.create_policy(new_policy):  # Pass the Policy object
                print("Policy created successfully.")
            else:
                print("Failed to create policy.")

        elif choice == "2":
            policy_id = int(input("Enter policy ID: "))
            policy = insurance_service.get_policy(policy_id)
            if policy:
                print(f"Policy ID: {policy.policyId}, Name: {policy.policyName}, Details: {policy.policyDetails}")
            else:
                print("Policy not found.")

        elif choice == "3":
            policies = insurance_service.get_all_policies()
            if policies:
                for policy in policies:
                    print(f"Policy ID: {policy.policyId}, Name: {policy.policyName}, Details: {policy.policyDetails}")
            else:
                print("No policies found.")

        elif choice == "4":
            policy_id = int(input("Enter the policy ID to update: "))
            policy_name = input("Enter new policy name: ")
            policy_details = input("Enter new policy details: ")

            updated_policy = Policy(policyId=policy_id, policyName=policy_name, policyDetails=policy_details)
            if insurance_service.update_policy(updated_policy):
                print("Policy updated successfully.")
            else:
                print("Failed to update policy.")

        elif choice == "5":
            policy_id = int(input("Enter the policy ID to delete: "))
            if insurance_service.delete_policy(policy_id):
                print("Policy deleted successfully.")
            else:
                print("Failed to delete policy.")

        elif choice == "6":
            user_id = int(input("Enter user ID: "))  # Get user ID from input
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (e.g., Admin, Client, etc.): ")
            user = User(userId=user_id, username=username, password=password, role=role)  # Pass userId
            insurance_service.create_user(user)

        elif choice == "7":
            client_id = int(input("Enter client ID: "))
            client_name = input("Enter client name: ")
            contact_info = input("Enter contact information: ")
            policy_id = int(input("Enter policy ID associated with the client: "))
            new_client = Client(clientId=client_id, clientName=client_name, contactInfo=contact_info, policyId=policy_id)
            insurance_service.create_client(new_client)

        elif choice == "8":
            payment_id = int(input("Enter payment ID: "))  # Prompt for payment ID
            payment_date = input("Enter payment date (YYYY-MM-DD): ")
            payment_amount = float(input("Enter payment amount: "))
            client_id = int(input("Enter client ID for payment: "))
            
            client = insurance_service.get_client(client_id)  # Assuming this method exists to retrieve client
            if client:
                payment = Payment(payment_id=payment_id, payment_date=payment_date, payment_amount=payment_amount, client=client)  # Pass the Client object
                insurance_service.create_payment(payment)
            else:
                print("Client not found. Payment could not be created.")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
