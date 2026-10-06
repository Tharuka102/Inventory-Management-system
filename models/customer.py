
from database import get_connection

class CustomerModel:

    # Add a new customer
    def add_customer(
        self,
        name,
        phone,
        email
    ):
        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to add customer
            query = """
                INSERT INTO customers
                (
                    name,
                    phone,
                    email
                )
                VALUES (%s, %s, %s)
            """
            # Run the insert query
            cursor.execute(
                query,
                (
                    name,
                    phone,
                    email
                )
            )

            # Save the new customer
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

    # Get all customers
    def get_customers(self):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to get customers
            query = """
                SELECT
                    id,
                    name,
                    phone,
                    email
                FROM customers
                ORDER BY id DESC
            """

            # Run the query
            cursor.execute(query)

            # Return customer data
            return cursor.fetchall()

        except Exception as error:

            # Send the error back
            raise error

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Search customers
    def search_customers(self, search_text):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Add % to search for matching text
            search_value = f"%{search_text}%"

            # SQL query to search customers
            query = """
                SELECT
                    id,
                    name,
                    phone,
                    email
                FROM customers
                WHERE
                    name LIKE %s
                    OR phone LIKE %s
                    OR email LIKE %s
                ORDER BY id DESC
            """

            # Run the search query
            cursor.execute(
                query,
                (
                    search_value,
                    search_value,
                    search_value
                )
            )

            # Return matching customers
            return cursor.fetchall()

        except Exception as error:

            # Send the error back
            raise error

        finally:

            # Close database connection
            cursor.close()
            connection.close()

    # Update customer details
    def update_customer(
        self,
        customer_id,
        name,
        phone,
        email
    ):
        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to update customer
            query = """
                UPDATE customers
                SET
                    name = %s,
                    phone = %s,
                    email = %s
                WHERE id = %s
            """

            # Run the update query
            cursor.execute(
                query,
                (
                    name,
                    phone,
                    email,
                    customer_id
                )
            )

            # Save the changes
            connection.commit()

            # Return True if a customer was updated
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

    # Delete a customer
    def delete_customer(self, customer_id):

        # Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # SQL query to delete customer
            query = """
                DELETE FROM customers
                WHERE id = %s
            """

            # Run the delete query
            cursor.execute(
                query,
                (customer_id,)
            )
            # Save the changes
            connection.commit()

            # Return True if a customer was deleted
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

