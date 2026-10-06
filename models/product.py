
from database import get_connection


class ProductModel:

    # Add a new product
    def add_product(
        self,
        name,
        quantity,
        cost_price,
        selling_price
    ):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to add product
            query = """
                INSERT INTO products
                (
                    name,
                    quantity,
                    cost_price,
                    selling_price
                )
                VALUES (%s, %s, %s, %s)
            """

            # Run the query
            cursor.execute(
                query,
                (
                    name,
                    quantity,
                    cost_price,
                    selling_price
                )
            )

            # Save the product
            connection.commit()

            # Return success
            return True

        except Exception as error:

            # Undo changes if an error happens
            connection.rollback()

            # Send the error back
            raise error

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Get all products
    def get_products(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to get all products
            query = """
                SELECT
                    id,
                    name,
                    quantity,
                    cost_price,
                    selling_price
                FROM products
                ORDER BY id DESC
            """

            # Run the query
            cursor.execute(query)

            # Return product data
            return cursor.fetchall()

        except Exception as error:

            # Send the error back
            raise error

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Search products by name
    def search_products(self, search_text):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Add % for partial search
            search_value = f"%{search_text}%"

            # SQL query to search products
            query = """
                SELECT
                    id,
                    name,
                    quantity,
                    cost_price,
                    selling_price
                FROM products
                WHERE name LIKE %s
                ORDER BY id DESC
            """

            # Run the search query
            cursor.execute(
                query,
                (search_value,)
            )

            # Return matching products
            return cursor.fetchall()

        except Exception as error:

            # Send the error back
            raise error

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Update product details
    def update_product(
        self,
        product_id,
        name,
        quantity,
        cost_price,
        selling_price
    ):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to update product
            query = """
                UPDATE products
                SET
                    name = %s,
                    quantity = %s,
                    cost_price = %s,
                    selling_price = %s
                WHERE id = %s
            """

            # Run the update query
            cursor.execute(
                query,
                (
                    name,
                    quantity,
                    cost_price,
                    selling_price,
                    product_id
                )
            )

            # Save the changes
            connection.commit()

            # Check if a product was updated
            return cursor.rowcount > 0

        except Exception as error:

            # Undo changes if an error happens
            connection.rollback()

            # Send the error back
            raise error

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Delete a product
    def delete_product(self, product_id):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to delete product
            query = """
                DELETE FROM products
                WHERE id = %s
            """

            # Run the delete query
            cursor.execute(
                query,
                (product_id,)
            )

            # Save the changes
            connection.commit()

            # Check if a product was deleted
            return cursor.rowcount > 0

        except Exception as error:

            # Undo changes if an error happens
            connection.rollback()

            # Send the error back
            raise error

        finally:

            # Close database connection
            cursor.close()
            connection.close()
