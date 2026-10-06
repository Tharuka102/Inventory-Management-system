
from database import get_connection
from datetime import datetime


class SalesModel:

    # =====================================================
    # Get Customers
    # =====================================================

    def get_customers(self):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get customer ID and name
            query = """
                SELECT id, name
                FROM customers
                ORDER BY name
            """

            # Run the query
            cursor.execute(query)

            # Return all customers
            return cursor.fetchall()

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Get Products
    # =====================================================

    def get_products(self):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get products that are in stock
            query = """
                SELECT
                    id,
                    name,
                    quantity,
                    cost_price,
                    selling_price
                FROM products
                WHERE quantity > 0
                ORDER BY name
            """

            # Run the query
            cursor.execute(query)

            # Return the products
            return cursor.fetchall()

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Get Product By ID
    # =====================================================

    def get_product(self, product_id):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Find one product using its ID
            query = """
                SELECT
                    id,
                    name,
                    quantity,
                    cost_price,
                    selling_price
                FROM products
                WHERE id = %s
            """

            # Run the query with product ID
            cursor.execute(
                query,
                (product_id,)
            )

            # Return the selected product
            return cursor.fetchone()

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Generate Invoice Number
    # =====================================================

    def generate_invoice_number(self):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get the latest sale ID
            query = """
                SELECT id
                FROM sales
                ORDER BY id DESC
                LIMIT 1
            """

            # Run the query
            cursor.execute(query)

            # Get the latest ID
            result = cursor.fetchone()

            # Create the next ID
            if result:

                next_id = result[0] + 1

            else:

                next_id = 1

            # Create the invoice number
            invoice_number = f"INV-{next_id:05d}"

            # Return the invoice number
            return invoice_number

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Save Sale
    # =====================================================

    def save_sale(
        self,
        invoice_number,
        customer_id,
        subtotal,
        discount,
        total,
        payment,
        balance,
        cart_items
    ):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # ---------------------------------------------
            # Check Payment
            # ---------------------------------------------

            # Check if customer paid enough
            if payment < total:

                raise ValueError(
                    "Payment is less than the total amount."
                )

            # ---------------------------------------------
            # Check Stock
            # ---------------------------------------------

            # Check stock for every cart item
            for item in cart_items:

                product_id = item["product_id"]
                quantity = item["quantity"]

                query = """
                    SELECT quantity
                    FROM products
                    WHERE id = %s
                    FOR UPDATE
                """

                # Get current stock
                cursor.execute(
                    query,
                    (product_id,)
                )

                product = cursor.fetchone()

                # Check if the product exists
                if not product:

                    raise ValueError(
                        f"Product ID {product_id} was not found."
                    )

                # Get available quantity
                available_quantity = product[0]

                # Check if there is enough stock
                if available_quantity < quantity:

                    raise ValueError(
                        f"Not enough stock for product ID "
                        f"{product_id}."
                    )

            # ---------------------------------------------
            # Insert Sale
            # ---------------------------------------------

            # SQL query to save the sale
            sale_sql = """
                INSERT INTO sales
                (
                    invoice_number,
                    customer_id,
                    subtotal,
                    discount,
                    total,
                    payment,
                    balance,
                    sale_date
                )
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Values for the sale
            sale_values = (
                invoice_number,
                customer_id,
                subtotal,
                discount,
                total,
                payment,
                balance,
                datetime.now()
            )

            # Save the sale
            cursor.execute(
                sale_sql,
                sale_values
            )

            # Get the new sale ID
            sale_id = cursor.lastrowid

            # ---------------------------------------------
            # Insert Sale Items
            # ---------------------------------------------

            # SQL query to save sale items
            item_sql = """
                INSERT INTO sale_items
                (
                    sale_id,
                    product_id,
                    quantity,
                    unit_price,
                    cost_price,
                    total
                )
                VALUES
                (%s, %s, %s, %s, %s, %s)
            """

            # SQL query to reduce product stock
            update_stock_sql = """
                UPDATE products
                SET quantity = quantity - %s
                WHERE id = %s
            """

            # Process each item in the cart
            for item in cart_items:

                product_id = item["product_id"]
                quantity = item["quantity"]
                unit_price = item["unit_price"]
                cost_price = item["cost_price"]
                item_total = item["total"]

                # Save the sale item
                cursor.execute(
                    item_sql,
                    (
                        sale_id,
                        product_id,
                        quantity,
                        unit_price,
                        cost_price,
                        item_total
                    )
                )

                # Reduce the product stock
                cursor.execute(
                    update_stock_sql,
                    (
                        quantity,
                        product_id
                    )
                )

            # ---------------------------------------------
            # Commit Transaction
            # ---------------------------------------------

            # Save all changes to the database
            connection.commit()

            # Return the sale ID
            return sale_id

        except Exception as error:

            # Undo changes if an error happens
            connection.rollback()

            # Send the error back
            raise error

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Get Sales
    # =====================================================

    def get_sales(self):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get all sales with customer names
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

            # Return all sales
            return cursor.fetchall()

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Search Sales
    # =====================================================

    def search_sales(self, search_text):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Prepare the search text
            search_value = f"%{search_text}%"

            # Search by invoice number or customer name
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

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Get Sale Items
    # =====================================================

    def get_sale_items(self, sale_id):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get items from the selected sale
            query = """
                SELECT
                    si.id,
                    p.name,
                    si.quantity,
                    si.unit_price,
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

            # Return the sale items
            return cursor.fetchall()

        finally:

            # Close database resources
            cursor.close()
            connection.close()

