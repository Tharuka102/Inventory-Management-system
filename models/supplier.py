
from database import get_connection

class SupplierModel:

    # =====================================================
    # Add Supplier
    # =====================================================

    def add_supplier(
        self,
        name,
        item,
        quantity,
        unit_price,
        phone,
        email
    ):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # ---------------------------------------------
            # 1. Create Supplier
            # ---------------------------------------------

            # Add the supplier details
            supplier_query = """
                INSERT INTO suppliers
                (
                    name,
                    phone,
                    email
                )
                VALUES (%s, %s, %s)
            """

            # Run the supplier query
            cursor.execute(
                supplier_query,
                (
                    name,
                    phone,
                    email
                )
            )

            # Get the new supplier ID
            supplier_id = cursor.lastrowid

            # ---------------------------------------------
            # 2. Calculate Cost
            # ---------------------------------------------

            # Calculate the total cost
            cost_price = quantity * unit_price

            # Calculate selling price with 3% profit
            selling_price = unit_price * 1.03

            # ---------------------------------------------
            # 3. Find Product
            # ---------------------------------------------

            # Find the product by name
            product_query = """
                SELECT
                    id,
                    quantity
                FROM products
                WHERE LOWER(TRIM(name)) = LOWER(TRIM(%s))
            """

            # Run the product search
            cursor.execute(
                product_query,
                (item,)
            )

            # Get the product data
            product = cursor.fetchone()

            # ---------------------------------------------
            # 4. Create / Update Product
            # ---------------------------------------------

            # Check if the product already exists
            if product:

                # Get the existing product ID
                product_id = product[0]

                # Update the existing product
                update_product_query = """
                    UPDATE products
                    SET
                        quantity = quantity + %s,
                        cost_price = %s,
                        selling_price = %s
                    WHERE id = %s
                """

                cursor.execute(
                    update_product_query,
                    (
                        quantity,
                        unit_price,
                        selling_price,
                        product_id
                    )
                )

            else:

                # Add a new product
                insert_product_query = """
                    INSERT INTO products
                    (
                        name,
                        quantity,
                        cost_price,
                        selling_price
                    )
                    VALUES (%s, %s, %s, %s)
                """

                cursor.execute(
                    insert_product_query,
                    (
                        item,
                        quantity,
                        unit_price,
                        selling_price
                    )
                )

                # Get the new product ID
                product_id = cursor.lastrowid

            # ---------------------------------------------
            # 5. Create Supplier-Product Relationship
            # ---------------------------------------------

            # Connect the supplier with the product
            supplier_product_query = """
                INSERT INTO supplier_products
                (
                    supplier_id,
                    product_id,
                    quantity,
                    unit_price,
                    cost_price
                )
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(
                supplier_product_query,
                (
                    supplier_id,
                    product_id,
                    quantity,
                    unit_price,
                    cost_price
                )
            )

            # ---------------------------------------------
            # 6. Save Everything
            # ---------------------------------------------

            # Save all changes
            connection.commit()

            # Show that the operation was successful
            return True

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
    # Get All Suppliers
    # =====================================================

    def get_suppliers(self):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Get supplier and product details
            query = """
                SELECT
                    s.id,
                    s.name,
                    p.name AS item_name,
                    sp.quantity,
                    sp.unit_price,
                    sp.cost_price,
                    p.selling_price,
                    s.phone,
                    s.email
                FROM suppliers s

                INNER JOIN supplier_products sp
                    ON s.id = sp.supplier_id

                INNER JOIN products p
                    ON sp.product_id = p.id

                ORDER BY s.id DESC
            """

            # Run the query
            cursor.execute(query)

            # Return all suppliers
            return cursor.fetchall()

        except Exception as error:

            # Send the error back
            raise error

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Search Suppliers
    # =====================================================

    def search_suppliers(self, search_text):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # Prepare the search text
            search_value = f"%{search_text}%"

            # Search supplier and product details
            query = """
                SELECT
                    s.id,
                    s.name,
                    p.name AS item_name,
                    sp.quantity,
                    sp.unit_price,
                    sp.cost_price,
                    p.selling_price,
                    s.phone,
                    s.email
                FROM suppliers s

                INNER JOIN supplier_products sp
                    ON s.id = sp.supplier_id

                INNER JOIN products p
                    ON sp.product_id = p.id

                WHERE
                    s.name LIKE %s
                    OR p.name LIKE %s
                    OR s.phone LIKE %s
                    OR s.email LIKE %s

                ORDER BY s.id DESC
            """

            # Run the search query
            cursor.execute(
                query,
                (
                    search_value,
                    search_value,
                    search_value,
                    search_value
                )
            )

            # Return matching suppliers
            return cursor.fetchall()

        except Exception as error:

            # Send the error back
            raise error

        finally:

            # Close database resources
            cursor.close()
            connection.close()

    # =====================================================
    # Update Supplier
    # =====================================================

    def update_supplier(
        self,
        supplier_id,
        name,
        item,
        quantity,
        unit_price,
        phone,
        email
    ):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # ---------------------------------------------
            # 1. Get Existing Supplier Product
            # ---------------------------------------------

            # Get the current product details
            old_query = """
                SELECT
                    product_id,
                    quantity
                FROM supplier_products
                WHERE supplier_id = %s
            """

            # Run the query
            cursor.execute(
                old_query,
                (supplier_id,)
            )

            # Get the old supplier product
            old_data = cursor.fetchone()

            # Check if supplier product exists
            if not old_data:

                raise Exception(
                    "Supplier product information was not found."
                )

            # Store old product information
            old_product_id = old_data[0]
            old_quantity = old_data[1]

            # ---------------------------------------------
            # 2. Find New Product
            # ---------------------------------------------

            # Find the new product by name
            product_query = """
                SELECT id
                FROM products
                WHERE LOWER(TRIM(name)) = LOWER(TRIM(%s))
            """

            # Run the product search
            cursor.execute(
                product_query,
                (item,)
            )

            # Get the product
            product = cursor.fetchone()

            # ---------------------------------------------
            # 3. Calculate Prices
            # ---------------------------------------------

            # Calculate selling price
            selling_price = unit_price * 1.03

            # Calculate total cost
            cost_price = quantity * unit_price

            # ---------------------------------------------
            # 4. Update Supplier
            # ---------------------------------------------

            # Update supplier information
            supplier_update = """
                UPDATE suppliers
                SET
                    name = %s,
                    phone = %s,
                    email = %s
                WHERE id = %s
            """

            cursor.execute(
                supplier_update,
                (
                    name,
                    phone,
                    email,
                    supplier_id
                )
            )

            # =================================================
            # Product Changed
            # =================================================

            # Check if a different product was selected
            if product and product[0] != old_product_id:

                # Get the new product ID
                new_product_id = product[0]

                # Remove old stock

                # Remove the old quantity from stock
                remove_old_stock = """
                    UPDATE products
                    SET quantity = quantity - %s
                    WHERE id = %s
                """

                cursor.execute(
                    remove_old_stock,
                    (
                        old_quantity,
                        old_product_id
                    )
                )

                # Add new stock

                # Add the new quantity to stock
                add_new_stock = """
                    UPDATE products
                    SET
                        quantity = quantity + %s,
                        cost_price = %s,
                        selling_price = %s
                    WHERE id = %s
                """

                cursor.execute(
                    add_new_stock,
                    (
                        quantity,
                        unit_price,
                        selling_price,
                        new_product_id
                    )
                )

                # Update supplier relationship

                # Connect supplier with the new product
                update_relationship = """
                    UPDATE supplier_products
                    SET
                        product_id = %s,
                        quantity = %s,
                        unit_price = %s,
                        cost_price = %s
                    WHERE supplier_id = %s
                """

                cursor.execute(
                    update_relationship,
                    (
                        new_product_id,
                        quantity,
                        unit_price,
                        cost_price,
                        supplier_id
                    )
                )

            # =================================================
            # Same Product
            # =================================================

            else:

                # Keep the existing product ID
                product_id = old_product_id

                # Find the stock quantity difference
                quantity_difference = quantity - old_quantity

                # Update product stock

                # Change the product stock
                update_stock = """
                    UPDATE products
                    SET
                        quantity = quantity + %s,
                        cost_price = %s,
                        selling_price = %s
                    WHERE id = %s
                """

                cursor.execute(
                    update_stock,
                    (
                        quantity_difference,
                        unit_price,
                        selling_price,
                        product_id
                    )
                )

                # Update supplier product

                # Update supplier product details
                update_relationship = """
                    UPDATE supplier_products
                    SET
                        quantity = %s,
                        unit_price = %s,
                        cost_price = %s
                    WHERE supplier_id = %s
                """

                cursor.execute(
                    update_relationship,
                    (
                        quantity,
                        unit_price,
                        cost_price,
                        supplier_id
                    )
                )

            # ---------------------------------------------
            # 5. Commit
            # ---------------------------------------------

            # Save all changes
            connection.commit()

            # Show that the update was successful
            return True

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
    # Delete Supplier
    # =====================================================

    def delete_supplier(self, supplier_id):

        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        try:

            # ---------------------------------------------
            # 1. Get Supplied Products
            # ---------------------------------------------

            # Get products supplied by this supplier
            query = """
                SELECT
                    product_id,
                    quantity
                FROM supplier_products
                WHERE supplier_id = %s
            """

            cursor.execute(
                query,
                (supplier_id,)
            )

            # Get all supplied products
            products = cursor.fetchall()

            # ---------------------------------------------
            # 2. Remove Supplied Quantity From Stock
            # ---------------------------------------------

            # Remove supplied quantities from stock
            for product_id, quantity in products:

                # Update the product stock
                update_stock = """
                    UPDATE products
                    SET quantity = quantity - %s
                    WHERE id = %s
                """

                cursor.execute(
                    update_stock,
                    (
                        quantity,
                        product_id
                    )
                )

            # ---------------------------------------------
            # 3. Delete Supplier
            # ---------------------------------------------

            # Delete the supplier
            delete_query = """
                DELETE FROM suppliers
                WHERE id = %s
            """

            cursor.execute(
                delete_query,
                (supplier_id,)
            )

            # Check if supplier was deleted
            deleted = cursor.rowcount > 0

            # ---------------------------------------------
            # 4. Commit
            # ---------------------------------------------

            # Save all changes
            connection.commit()

            # Return delete result
            return deleted

        except Exception as error:

            # Undo changes if an error happens
            connection.rollback()

            # Send the error back
            raise error

        finally:

            # Close database resources
            cursor.close()
            connection.close()

