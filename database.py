
import mysql.connector


# MySQL database settings
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "smart_inventory"


# Create the database
def create_database():

    # Connect to MySQL server
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )
    # Create cursor
    cursor = connection.cursor()
    try:

        # Create database if it does not exist
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
        )

        # Save changes
        connection.commit()

    finally:

        # Close cursor and connection
        cursor.close()
        connection.close()

# Connect to the project database
def get_connection():

    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Create all project tables
def create_tables():

    # Connect to database
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100)
                    NOT NULL UNIQUE,
                password VARCHAR(255)
                    NOT NULL
            )
        """)

        # Create customers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100)
                    NOT NULL,
                phone VARCHAR(20),
                email VARCHAR(100),
                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create suppliers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100)
                    NOT NULL,
                phone VARCHAR(20),
                email VARCHAR(100),
                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100)
                    NOT NULL UNIQUE,
                quantity INT
                    NOT NULL DEFAULT 0,
                cost_price DECIMAL(10,2)
                    NOT NULL DEFAULT 0.00,
                selling_price DECIMAL(10,2)
                    NOT NULL DEFAULT 0.00,
                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create supplier products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS supplier_products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                supplier_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                unit_price DECIMAL(10,2)
                    NOT NULL,
                cost_price DECIMAL(10,2)
                    NOT NULL,
                FOREIGN KEY (supplier_id)
                    REFERENCES suppliers(id)
                    ON DELETE CASCADE,
                FOREIGN KEY (product_id)
                    REFERENCES products(id)
                    ON DELETE CASCADE,
                UNIQUE KEY unique_supplier_product
                    (supplier_id, product_id)
            )
        """)

        # Create sales table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INT AUTO_INCREMENT PRIMARY KEY,
                invoice_number VARCHAR(50)
                    NOT NULL UNIQUE,
                customer_id INT NULL,
                subtotal DECIMAL(10,2)
                    NOT NULL DEFAULT 0.00,
                discount DECIMAL(10,2)
                    NOT NULL DEFAULT 0.00,
                total DECIMAL(10,2)
                    NOT NULL DEFAULT 0.00,
                payment DECIMAL(10,2)
                    NOT NULL DEFAULT 0.00,
                balance DECIMAL(10,2)
                    NOT NULL DEFAULT 0.00,
                sale_date TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id)
                    REFERENCES customers(id)
                    ON DELETE SET NULL
            )
        """)

        # Create sale items table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sale_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sale_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                unit_price DECIMAL(10,2)
                    NOT NULL,
                cost_price DECIMAL(10,2)
                    NOT NULL,
                total DECIMAL(10,2)
                    NOT NULL,
                FOREIGN KEY (sale_id)
                    REFERENCES sales(id)
                    ON DELETE CASCADE,
                FOREIGN KEY (product_id)
                    REFERENCES products(id)
                    ON DELETE RESTRICT
            )
        """)

        # Save table changes
        connection.commit()

    finally:

        # Close database connection
        cursor.close()
        connection.close()


# Create the default login user
def create_default_user():

    # Connect to database
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # SQL query for creating the user
        sql = """
            INSERT IGNORE INTO users
            (
                username,
                password
            )
            VALUES (%s, %s)
        """

        # Default username and password
        values = (
            "user",
            "1234"
        )

        # Run the query
        cursor.execute(
            sql,
            values
        )

        # Save the user
        connection.commit()

    finally:

        # Close cursor and connection
        cursor.close()
        connection.close()

# Start the complete database setup
def initialize_database():

    # Create database
    create_database()
    # Create tables
    create_tables()
    # Create default user
    create_default_user()


# Test the database setup
if __name__ == "__main__":
    try:

        # Run database setup
        initialize_database()
        # Show success messages
        print("================================")
        print("MySQL database connected!")
        print("Database created successfully!")
        print("Tables created successfully!")
        print("Default user created!")
        print("================================")

    # Show error if MySQL has a problem
    except mysql.connector.Error as error:
        print("Database error:", error)

