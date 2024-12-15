# initializer.py
import os
import pandas as pd
from datetime import datetime
from util.password import Password
from util.input_validator import InputValidator

# File and directory setup
DATA_DIR = "data"
DATA_FILES_DIR = os.path.join(DATA_DIR, "data_files")
LOG_DIR = os.path.join(DATA_DIR, "logs")

PRODUCT_FILE = os.path.join(DATA_FILES_DIR, "products.csv")
EMPLOYEE_FILE = os.path.join(DATA_FILES_DIR, "employees.csv")

LOG_FILES = {
    "sign_in_log": ["eid", "action", "timestamp"],
    "profile_activity_log": ["eid", "action", "timestamp"],
    "supervisor_alerts": ["eid", "timestamp", "timespan", "header", "body", "alert_level"],
    "manager_alerts": ["eid", "timestamp", "timespan", "header", "body", "alert_level"],
    "product_add_remove_readd": ["eid", "pid", "timestamp", "action"],
    "restock": ["eid", "pid", "timestamp", "quantity"],
    "product_update_log": ["eid", "pid", "column_name", "old_value", "new_value", "timestamp"],
    "fire_employee_log": ["fired_by", "fired_eid", "timestamp", "note"],
    "add_employee_log": ["eid", "timestamp"],
    "sales_log": ["eid", "quantity", "timestamp"],
}

# Helper Functions
def create_empty_csv(file_path, columns):
    """Creates an empty CSV file with specified columns."""
    try:
        if not os.path.exists(file_path):
            pd.DataFrame(columns=columns).to_csv(file_path, index=False)
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")
    except Exception as e:
        print(f"Error creating file {file_path}: {e}")

def setup_directories():
    """Sets up the data and log directories."""
    try:
        os.makedirs(DATA_FILES_DIR, exist_ok=True)
        os.makedirs(LOG_DIR, exist_ok=True)
        print(f"Directories ensured: {DATA_FILES_DIR}, {LOG_DIR}")
    except Exception as e:
        print(f"Error creating directories: {e}")
        raise

def initialize_logs():
    """Creates all required log files."""
    try:
        for log_name, columns in LOG_FILES.items():
            file_path = os.path.join(LOG_DIR, f"{log_name}.csv")
            create_empty_csv(file_path, columns)
    except Exception as e:
        print(f"Error initializing logs: {e}")
        raise

def initialize_data_files():
    """Initializes the product and employee files."""
    try:
        product_columns = ["pid", "is_active", "inventory", "pname", "pdescription", "pprice", "added_date", "ptags"]
        create_empty_csv(PRODUCT_FILE, product_columns)
        
        employee_columns = [
            "eid", "first_name", "last_name", "starting_date", "is_active",
            "etype", "eemail", "ephone", "fav_food", "password"
        ]
        create_empty_csv(EMPLOYEE_FILE, employee_columns)
    except Exception as e:
        print(f"Error initializing data files: {e}")
        raise

def add_admin():
    """Prompts for admin details and adds the admin to the employee file."""
    print("Admin Initialization")
    try:
        password_handler = Password()
        input_handler = InputValidator()

        # Collect admin details using InputValidator
        first_name = input_handler.get_string_input(prompt="Enter Admin First Name: ", min_length=3)
        last_name = input_handler.get_string_input(prompt="Enter Admin Last Name: ", min_length=3)
        email = input_handler.get_email_input(prompt="Enter Admin Email: ")
        phone = input_handler.get_phone_input(prompt="Enter Admin Phone: ")
        fav_food = input_handler.get_string_input(prompt="Enter Admin Favorite Food: ", min_length=3)

        # Get secure password input with validation
        password = input_handler.get_password_input(prompt="Enter Admin Password: ", min_length=8, max_length=20)

        # Hash the password using Password class
        hashed_password = password_handler.hash_password(password)

        admin_data = pd.DataFrame([{
            "eid": 0,
            "first_name": first_name,
            "last_name": last_name,
            "starting_date": datetime.now().strftime("%Y-%m-%d"),
            "is_active": True,
            "etype": 0,
            "eemail": email,
            "ephone": phone,
            "fav_food": fav_food,
            "password": hashed_password
        }])

        if os.path.exists(EMPLOYEE_FILE):
            existing_data = pd.read_csv(EMPLOYEE_FILE)
            combined_data = pd.concat([existing_data, admin_data], ignore_index=True)
            combined_data.to_csv(EMPLOYEE_FILE, index=False)
            print("Admin added to existing employee file.")
        else:
            admin_data.to_csv(EMPLOYEE_FILE, index=False)
            print("Admin added and employee file created.")
    except Exception as e:
        print(f"Error adding admin: {e}")
        raise

# Main Initialization
def main():
    try:
        setup_directories()
        initialize_logs()
        initialize_data_files()
        add_admin()
        print("System Initialized Successfully!")
    except Exception as e:
        print(f"System initialization failed: {e}")

if __name__ == "__main__":
    main()
