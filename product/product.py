import csv
from datetime import datetime
from util.ui import TerminalToolkit
from util.input_validator import InputValidator

class Product:
    """
    Represents a product in an inventory system.

    This class provides functionality to create, manage, and retrieve product records stored in a CSV file.
    It includes methods to add and remove inventory, update product details, and fetch product data by ID.

    Attributes:
    - product_file (str): Path to the CSV file storing product data.
    - product_columns (list): List of column names for the product file.
    """

    product_file = "data/products.csv"
    product_columns = ["pid", "is_active", "inventory", "pname", "pdescription", "pprice", "added_date", "ptags"]

    def __init__(self, pname, pdescription, inventory, pprice, ptags):
        """
        Constructor for the Product class.

        Parameters:
        - pname (str): Name of the product.
        - pdescription (str): Description of the product.
        - inventory (int): Initial inventory count of the product.
        - pprice (float): Price of the product.
        - ptags (str): Tags associated with the product, separated by '|'.

        This constructor initializes a new Product instance and writes its data to the product file.
        """
        self.pid = self._generate_pid()
        self.is_active = True
        self.inventory = inventory
        self.pname = pname
        self.pdescription = pdescription
        self.pprice = pprice
        self.added_date = datetime.now().strftime("%Y-%m-%d")
        self.ptags = ptags
        self._write_to_file()

    @classmethod
    def from_existing(cls, pid, is_active, inventory, pname, pdescription, pprice, added_date, ptags):
        """
        Creates a Product object from existing data.

        Parameters:
        - pid (int): Product ID.
        - is_active (bool): Whether the product is active.
        - inventory (int): Inventory count of the product.
        - pname (str): Name of the product.
        - pdescription (str): Description of the product.
        - pprice (float): Price of the product.
        - added_date (str): Date the product was added (YYYY-MM-DD).
        - ptags (str): Tags associated with the product, separated by '|'.

        Returns:
        - Product: A Product object initialized with the given data.
        """
        obj = cls.__new__(cls)
        obj.pid = pid
        obj.is_active = is_active
        obj.inventory = inventory
        obj.pname = pname
        obj.pdescription = pdescription
        obj.pprice = pprice
        obj.added_date = added_date
        obj.ptags = ptags
        return obj

    @classmethod
    def _generate_pid(cls):
        """
        Generates a new unique product ID based on the number of records in the product file.

        Returns:
        - int: A unique product ID.
        """
        try:
            with open(cls.product_file, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                pid = sum(1 for _ in reader) + 1
        except FileNotFoundError:
            pid = 1
        return pid

    def _write_to_file(self):
        """
        Writes the current product's data to the product file.

        Handles exceptions related to file permissions and general errors. If an exception occurs, an appropriate
        error message is printed to assist with debugging.
        """
        try:
            # Check if file exists and write header if needed
            write_header = not self._file_exists()
            with open(self.product_file, "a", newline="") as file:
                writer = csv.writer(file)
                if write_header:
                    writer.writerow(self.product_columns)
                writer.writerow([
                    self.pid, self.is_active, self.inventory, self.pname,
                    self.pdescription, self.pprice, self.added_date, self.ptags
                ])
        except PermissionError:
            print("Error: Insufficient permissions to write to the product file.")
        except IOError as e:
            print(f"Error: I/O error occurred while writing to the file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    @staticmethod
    def _file_exists():
        """
        Checks whether the product file exists.

        Returns:
        - bool: True if the file exists, False otherwise.
        """
        try:
            with open(Product.product_file, "r"):
                return True
        except FileNotFoundError:
            return False

    # Getters
    def get_pid(self):
        """
        Returns the product ID.

        Returns:
        - int: Product ID.
        """
        return self.pid

    def get_is_active(self):
        """
        Returns whether the product is active.

        Returns:
        - bool: True if active, False otherwise.
        """
        return self.is_active

    def get_inventory(self):
        """
        Returns the current inventory count.

        Returns:
        - int: Inventory count.
        """
        return self.inventory

    def get_pname(self):
        """
        Returns the product name.

        Returns:
        - str: Product name.
        """
        return self.pname

    def get_pdescription(self):
        """
        Returns the product description.

        Returns:
        - str: Product description.
        """
        return self.pdescription

    def get_pprice(self):
        """
        Returns the product price.

        Returns:
        - float: Product price.
        """
        return self.pprice

    def get_added_date(self):
        """
        Returns the date the product was added.

        Returns:
        - str: Added date in YYYY-MM-DD format.
        """
        return self.added_date

    def get_ptags(self):
        """
        Returns the product tags.

        Returns:
        - str: Tags associated with the product, separated by '|'.
        """
        return self.ptags

    # Setters
    def set_is_active(self, is_active):
        """
        Sets the active status of the product and updates the product file.

        Parameters:
        - is_active (bool): True to activate, False to deactivate.
        """
        self.is_active = is_active
        self._update_file()

    def set_pname(self, pname):
        """
        Sets the product name and updates the product file.

        Parameters:
        - pname (str): New product name.
        """
        self.pname = pname
        self._update_file()

    def set_pdescription(self, pdescription):
        """
        Sets the product description and updates the product file.

        Parameters:
        - pdescription (str): New product description.
        """
        self.pdescription = pdescription
        self._update_file()

    def set_pprice(self, pprice):
        """
        Sets the product price and updates the product file.

        Parameters:
        - pprice (float): New product price.
        """
        self.pprice = pprice
        self._update_file()

    def set_ptags(self, ptags):
        """
        Sets the product tags and updates the product file.

        Parameters:
        - ptags (str): New product tags, separated by '|'.
        """
        self.ptags = ptags
        self._update_file()

    # Inventory management
    def add_inventory(self, num):
        """
        Adds to the product's inventory and updates the product file.

        Parameters:
        - num (int): Number of items to add. Must be positive.
        """
        if num > 0:
            self.inventory += num
            self._update_file()
        else:
            print("Error: Cannot add non-positive inventory.")

    def remove_inventory(self, num):
        """
        Removes from the product's inventory and updates the product file.

        Parameters:
        - num (int): Number of items to remove. Must be positive and not exceed current inventory.
        """
        if num > 0 and num <= self.inventory:
            self.inventory -= num
            self._update_file()
        else:
            print("Error: Invalid inventory removal amount.")

    def _update_file(self):
        """
        Updates the product record in the product file.

        Handles exceptions related to file read/write operations. Ensures robust error messages for debugging.
        """
        try:
            rows = []
            with open(self.product_file, "r") as file:
                reader = csv.reader(file)
                rows = list(reader)

            # Find and update the row matching this pid
            for row in rows:
                if row[0] == str(self.pid):
                    row[1] = self.is_active
                    row[2] = self.inventory
                    row[3] = self.pname
                    row[4] = self.pdescription
                    row[5] = self.pprice
                    row[7] = self.ptags
                    break

            with open(self.product_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        except FileNotFoundError:
            print("Error: Product file not found.")
        except IOError as e:
            print(f"Error: I/O error occurred while updating the file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    @staticmethod
    def take_constructor_input():
        """
        Facilitates user input for creating a new Product object.

        Returns:
        - Product: A new Product object initialized with user-provided data.
        """
        toolkit = TerminalToolkit()
        validator = InputValidator()

        pname = validator.get_string_input("Enter product name: ", min_length=3, max_length=50)
        pdescription = validator.get_string_input("Enter product description: ", min_length=3, max_length=200)
        inventory = validator.get_int_input("Enter inventory count: ", min_val=0)
        pprice = validator.get_float_input("Enter product price: ", min_val=0.01)
        ptags = ""

        while True:
            ptags = validator.get_string_input("Enter product tags (separated by '|'): ")
            if all(tag.strip() for tag in ptags.split("|")):
                break
            toolkit.draw_box("Invalid format for tags. Please use 'tag1|tag2|tag3'.", color="red")

        return Product(pname, pdescription, inventory, pprice, ptags)

    @classmethod
    def get_product(cls, pid):
        """
        Retrieves a product by its ID and returns it as a Product object.

        Parameters:
        - pid (int): The ID of the product to retrieve.

        Returns:
        - Product: A Product object if found, None otherwise.

        Notes:
        - If the product is not found, an error message is printed.
        - Logs an error message if the product file is missing or another issue occurs.
        """
        try:
            with open(cls.product_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["pid"]) == pid:
                        return cls.from_existing(
                            pid=int(row["pid"]),
                            is_active=row["is_active"] == "True",
                            inventory=int(row["inventory"]),
                            pname=row["pname"],
                            pdescription=row["pdescription"],
                            pprice=float(row["pprice"]),
                            added_date=row["added_date"],
                            ptags=row["ptags"]
                        )
            print(f"Error: Product with ID {pid} not found.")
        except FileNotFoundError:
            print("Error: Product file not found.")
        except ValueError:
            print("Error: Data in the product file is malformed.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return None
