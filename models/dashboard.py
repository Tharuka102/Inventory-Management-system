
from database import get_connection

class DashboardModel:

    # Get the total number of products
    def get_total_products(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()
        try:

            # Count all products
            query = """
                SELECT COUNT(*)
                FROM products
            """

            # Run the query
            cursor.execute(query)

            # Get the result
            result = cursor.fetchone()

            # Return the product count
            return result[0]

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get the total number of suppliers
    def get_total_suppliers(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Count all suppliers
            query = """
                SELECT COUNT(*)
                FROM suppliers
            """

            # Run the query
            cursor.execute(query)

            # Get the result
            result = cursor.fetchone()

            # Return the supplier count
            return result[0]

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get the total number of customers
    def get_total_customers(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Count all customers
            query = """
                SELECT COUNT(*)
                FROM customers
            """

            # Run the query
            cursor.execute(query)

            # Get the result
            result = cursor.fetchone()

            # Return the customer count
            return result[0]

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get the total sales amount
    def get_total_sales(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Add all sales totals
            query = """
                SELECT COALESCE(SUM(total), 0)
                FROM sales
            """

            # Run the query
            cursor.execute(query)

            # Get the result
            result = cursor.fetchone()

            # Return the sales amount
            return float(result[0])

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get the top three customers
    def get_top_customers(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Find customers with the highest purchases
            query = """
                SELECT
                    c.name,
                    COUNT(s.id) AS purchase_count,
                    COALESCE(SUM(s.total), 0) AS total_purchases
                FROM customers c
                INNER JOIN sales s
                    ON c.id = s.customer_id
                GROUP BY c.id, c.name
                ORDER BY total_purchases DESC
                LIMIT 3
            """

            # Run the query
            cursor.execute(query)

            # Return the top customers
            return cursor.fetchall()

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get the top three suppliers
    def get_top_suppliers(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()
        try:

            # Find suppliers with the most items
            query = """
                SELECT
                    s.name,
                    COALESCE(SUM(sp.quantity), 0) AS total_items
                FROM suppliers s
                INNER JOIN supplier_products sp
                    ON s.id = sp.supplier_id
                GROUP BY s.id, s.name
                ORDER BY total_items DESC
                LIMIT 3
            """

            # Run the query
            cursor.execute(query)

            # Return the top suppliers
            return cursor.fetchall()

        finally:

            # Close database connection
            cursor.close()
            connection.close()

