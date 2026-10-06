
from database import get_connection


class ReportModel:

    # Get all sales records
    def get_sales_report(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get sales and customer details
            query = """
                SELECT
                    s.id,
                    s.invoice_number,
                    COALESCE(c.name, 'Walk-in Customer'),
                    s.subtotal,
                    s.discount,
                    s.total,
                    s.payment,
                    s.balance,
                    s.sale_date
                FROM sales s
                LEFT JOIN customers c
                    ON s.customer_id = c.id
                ORDER BY s.id DESC
            """

            # Run the query
            cursor.execute(query)

            # Return sales data
            return cursor.fetchall()

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Search sales by invoice or customer
    def search_sales_report(self, search_text):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Prepare the search text
            search_value = f"%{search_text}%"

            # Search sales records
            query = """
                SELECT
                    s.id,
                    s.invoice_number,
                    COALESCE(c.name, 'Walk-in Customer'),
                    s.subtotal,
                    s.discount,
                    s.total,
                    s.payment,
                    s.balance,
                    s.sale_date
                FROM sales s
                LEFT JOIN customers c
                    ON s.customer_id = c.id
                WHERE
                    s.invoice_number LIKE %s
                    OR c.name LIKE %s
                ORDER BY s.id DESC
            """

            # Run the search query
            cursor.execute(
                query,
                (
                    search_value,
                    search_value
                )
            )

            # Return matching sales
            return cursor.fetchall()

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get products from a selected sale
    def get_sale_items(self, sale_id):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get sale item details
            query = """
                SELECT
                    p.name,
                    si.quantity,
                    si.unit_price,
                    si.cost_price,
                    si.total
                FROM sale_items si
                INNER JOIN products p
                    ON si.product_id = p.id
                WHERE si.sale_id = %s
                ORDER BY si.id
            """

            # Run the query
            cursor.execute(
                query,
                (sale_id,)
            )

            # Return sale items
            return cursor.fetchall()

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Calculate profit for one sale
    def get_sale_profit(self, sale_id):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Calculate profit from sale items
            query = """
                SELECT
                    COALESCE(
                        SUM(
                            (unit_price - cost_price) * quantity
                        ),
                        0
                    )
                FROM sale_items
                WHERE sale_id = %s
            """

            # Run the query
            cursor.execute(
                query,
                (sale_id,)
            )

            # Get the result
            result = cursor.fetchone()

            # Return profit value
            return float(result[0])

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get total sales amount
    def get_total_sales(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Add all sale totals
            query = """
                SELECT COALESCE(SUM(total), 0)
                FROM sales
            """

            # Run the query
            cursor.execute(query)

            # Get the result
            result = cursor.fetchone()

            # Return total sales
            return float(result[0])

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get total profit
    def get_total_profit(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Calculate profit from all sale items
            query = """
                SELECT
                    COALESCE(
                        SUM(
                            (unit_price - cost_price) * quantity
                        ),
                        0
                    )
                FROM sale_items
            """

            # Run the query
            cursor.execute(query)

            # Get the result
            result = cursor.fetchone()

            # Return total profit
            return float(result[0])

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get total number of products
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

            # Return product count
            return result[0]

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get total number of customers
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

            # Return customer count
            return result[0]

        finally:

            # Close database connection
            cursor.close()
            connection.close()
