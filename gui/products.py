
import customtkinter as ctk
from tkinter import ttk, messagebox

from models.product import ProductModel


class ProductsWindow:

    def __init__(self, app):

        self.app = app
        self.product_model = ProductModel()

        # Store the selected product ID
        self.selected_product_id = None

        # =========================
        # Main Frame
        # =========================

        self.frame = ctk.CTkFrame(
            self.app,
            corner_radius=0
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # =========================
        # Heading
        # =========================

        title = ctk.CTkLabel(
            self.frame,
            text="Product Management",
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            )
        )

        title.pack(
            pady=(20, 5)
        )

        # Show a short description
        subtitle = ctk.CTkLabel(
            self.frame,
            text="Manage products, stock and prices"
        )

        subtitle.pack(
            pady=(0, 15)
        )

        # =========================
        # Form Frame
        # =========================

        form_frame = ctk.CTkFrame(
            self.frame
        )

        form_frame.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # =========================
        # Product Name
        # =========================

        ctk.CTkLabel(
            form_frame,
            text="Product Name"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        # Enter product name
        self.name_entry = ctk.CTkEntry(
            form_frame,
            width=220,
            placeholder_text="Enter product name"
        )

        self.name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # =========================
        # Stock Quantity
        # =========================

        ctk.CTkLabel(
            form_frame,
            text="Stock Quantity"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        # Enter stock quantity
        self.quantity_entry = ctk.CTkEntry(
            form_frame,
            width=150,
            placeholder_text="Enter quantity"
        )

        self.quantity_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        # =========================
        # Cost Price
        # =========================

        ctk.CTkLabel(
            form_frame,
            text="Cost Price (Rs.)"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        # Enter product cost price
        self.cost_price_entry = ctk.CTkEntry(
            form_frame,
            width=220,
            placeholder_text="Enter cost price"
        )

        self.cost_price_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # =========================
        # Selling Price
        # =========================

        ctk.CTkLabel(
            form_frame,
            text="Selling Price (Rs.)"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        # Enter product selling price
        self.selling_price_entry = ctk.CTkEntry(
            form_frame,
            width=150,
            placeholder_text="Enter selling price"
        )

        self.selling_price_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=10
        )

        # =========================
        # Buttons
        # =========================

        button_frame = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        button_frame.pack(
            pady=10
        )

        # Add new product
        ctk.CTkButton(
            button_frame,
            text="Add Product",
            width=130,
            command=self.add_product
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        # Update selected product
        ctk.CTkButton(
            button_frame,
            text="Update",
            width=130,
            command=self.update_product
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        # Delete selected product
        ctk.CTkButton(
            button_frame,
            text="Delete",
            width=130,
            command=self.delete_product
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        # Clear form fields
        ctk.CTkButton(
            button_frame,
            text="Clear",
            width=130,
            command=self.clear_fields
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        # =========================
        # Search Frame
        # =========================

        search_frame = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        search_frame.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        # Search product by name
        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=300,
            placeholder_text="Search product name"
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        # Search button
        ctk.CTkButton(
            search_frame,
            text="Search",
            width=100,
            command=self.search_products
        ).pack(
            side="left",
            padx=5
        )

        # Show all products
        ctk.CTkButton(
            search_frame,
            text="Show All",
            width=100,
            command=self.load_products
        ).pack(
            side="left",
            padx=5
        )

        # =========================
        # Table Frame
        # =========================

        table_frame = ctk.CTkFrame(
            self.frame
        )

        table_frame.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        # =========================
        # Treeview Style
        # =========================

        style = ttk.Style()

        # Set table row height and font
        style.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )

        # Set table heading font
        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        # =========================
        # Product Table
        # =========================

        columns = (
            "ID",
            "Product Name",
            "Stock",
            "Cost Price",
            "Selling Price"
        )

        # Create product table
        self.product_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        # Add table headings
        self.product_table.heading(
            "ID",
            text="ID"
        )

        self.product_table.heading(
            "Product Name",
            text="Product Name"
        )

        self.product_table.heading(
            "Stock",
            text="Stock"
        )

        self.product_table.heading(
            "Cost Price",
            text="Cost Price (Rs.)"
        )

        self.product_table.heading(
            "Selling Price",
            text="Selling Price (Rs.)"
        )

        # Set ID column
        self.product_table.column(
            "ID",
            width=60,
            anchor="center"
        )

        # Set product name column
        self.product_table.column(
            "Product Name",
            width=250
        )

        # Set stock column
        self.product_table.column(
            "Stock",
            width=100,
            anchor="center"
        )

        # Set cost price column
        self.product_table.column(
            "Cost Price",
            width=130,
            anchor="center"
        )

        # Set selling price column
        self.product_table.column(
            "Selling Price",
            width=130,
            anchor="center"
        )

        # Show product table
        self.product_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        # =========================
        # Scrollbar
        # =========================

        # Create vertical scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.product_table.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Connect scrollbar with table
        self.product_table.configure(
            yscrollcommand=scrollbar.set
        )

        # =========================
        # Select Row
        # =========================

        # Detect selected table row
        self.product_table.bind(
            "<ButtonRelease-1>",
            self.select_product
        )

        # =========================
        # Back Button
        # =========================

        # Return to dashboard
        ctk.CTkButton(
            self.frame,
            text="← Back to Dashboard",
            width=180,
            command=self.back_to_dashboard
        ).pack(
            pady=(0, 15)
        )

        # =========================
        # Load Products
        # =========================

        # Load products when window opens
        self.load_products()

    # =====================================================
    # Add Product
    # =====================================================

    def add_product(self):

        # Get values from input fields
        name = self.name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        cost_price = self.cost_price_entry.get().strip()
        selling_price = self.selling_price_entry.get().strip()

        # Check product name
        if not name:
            messagebox.showwarning(
                "Validation",
                "Please enter product name."
            )
            return

        # Check product name contains valid text
        if not any(char.isalpha() for char in name):
            messagebox.showwarning(
                "Validation",
                "Product name must contain letters."
            )
            return

        # Check quantity
        try:
            quantity = int(quantity)

            if quantity < 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Validation",
                "Stock quantity must be a valid whole number."
            )
            return

        # Check cost price
        try:
            cost_price = float(cost_price)

            if cost_price <= 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Validation",
                "Cost price must be greater than 0."
            )
            return

        # Check selling price
        try:
            selling_price = float(selling_price)

            if selling_price <= 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Validation",
                "Selling price must be greater than 0."
            )
            return

        # Check price has maximum 2 decimal places
        if "." in self.cost_price_entry.get():
            decimal_part = self.cost_price_entry.get().split(".")[1]

            if len(decimal_part) > 2:
                messagebox.showwarning(
                    "Validation",
                    "Cost price can have maximum 2 decimal places."
                )
                return

        if "." in self.selling_price_entry.get():
            decimal_part = self.selling_price_entry.get().split(".")[1]

            if len(decimal_part) > 2:
                messagebox.showwarning(
                    "Validation",
                    "Selling price can have maximum 2 decimal places."
                )
                return

        # Selling price should not be lower than cost price
        if selling_price < cost_price:
            messagebox.showwarning(
                "Validation",
                "Selling price cannot be lower than cost price."
            )
            return

        try:

            # Save product to database
            self.product_model.add_product(
                name,
                quantity,
                cost_price,
                selling_price
            )

            messagebox.showinfo(
                "Success",
                "Product added successfully."
            )

            # Clear fields after adding
            self.clear_fields()

            # Refresh product table
            self.load_products()

        except Exception as error:

            # Show database error
            messagebox.showerror(
                "Error",
                f"Failed to add product.\n\n{error}"
            )

    # =====================================================
    # Load Products
    # =====================================================

    def load_products(self):

        try:

            # Get products from database
            products = self.product_model.get_products()

            # Clear old table data
            self.product_table.delete(
                *self.product_table.get_children()
            )

            # Add products to table
            for product in products:

                product_id = product[0]
                product_name = product[1]
                stock = product[2]
                cost_price = float(product[3])
                selling_price = float(product[4])

                # Show product information
                self.product_table.insert(
                    "",
                    "end",
                    values=(
                        product_id,
                        product_name,
                        stock,
                        f"Rs. {cost_price:.2f}",
                        f"Rs. {selling_price:.2f}"
                    )
                )

        except Exception as error:

            # Show error if products cannot be loaded
            messagebox.showerror(
                "Error",
                f"Failed to load products.\n\n{error}"
            )

    # =====================================================
    # Search Products
    # =====================================================

    def search_products(self):

        # Get search text
        search_text = self.search_entry.get().strip()

        # Show all products when search is empty
        if not search_text:

            self.load_products()
            return

        # Check search text contains letters
        if not any(char.isalpha() for char in search_text):
            messagebox.showwarning(
                "Validation",
                "Please enter a valid product name."
            )
            return

        try:

            # Search products from database
            products = self.product_model.search_products(
                search_text
            )

            # Clear old search results
            self.product_table.delete(
                *self.product_table.get_children()
            )

            # Add search results to table
            for product in products:

                product_id = product[0]
                product_name = product[1]
                stock = product[2]
                cost_price = float(product[3])
                selling_price = float(product[4])

                # Show product information
                self.product_table.insert(
                    "",
                    "end",
                    values=(
                        product_id,
                        product_name,
                        stock,
                        f"Rs. {cost_price:.2f}",
                        f"Rs. {selling_price:.2f}"
                    )
                )

        except Exception as error:

            # Show error if search fails
            messagebox.showerror(
                "Error",
                f"Search failed.\n\n{error}"
            )

    # =====================================================
    # Select Product
    # =====================================================

    def select_product(self, event):

        # Get selected row
        selected = self.product_table.selection()

        if not selected:
            return

        # Get selected row values
        values = self.product_table.item(
            selected[0],
            "values"
        )

        # Store product ID
        self.selected_product_id = values[0]

        # Fill product name
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, values[1])

        # Fill quantity
        self.quantity_entry.delete(0, "end")
        self.quantity_entry.insert(0, values[2])

        # Fill cost price without Rs. text
        self.cost_price_entry.delete(0, "end")
        self.cost_price_entry.insert(
            0,
            str(values[3]).replace("Rs. ", "")
        )

        # Fill selling price without Rs. text
        self.selling_price_entry.delete(0, "end")
        self.selling_price_entry.insert(
            0,
            str(values[4]).replace("Rs. ", "")
        )

    # =====================================================
    # Update Product
    # =====================================================

    def update_product(self):

        # Check if a product is selected
        if self.selected_product_id is None:

            messagebox.showwarning(
                "Selection",
                "Please select a product first."
            )

            return

        # Get values from input fields
        name = self.name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        cost_price = self.cost_price_entry.get().strip()
        selling_price = self.selling_price_entry.get().strip()

        # Check product name
        if not name:
            messagebox.showwarning(
                "Validation",
                "Please enter product name."
            )
            return

        # Check product name contains letters
        if not any(char.isalpha() for char in name):
            messagebox.showwarning(
                "Validation",
                "Product name must contain letters."
            )
            return

        # Check quantity
        try:

            quantity = int(quantity)

            if quantity < 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Stock quantity must be a valid whole number."
            )

            return

        # Check cost price
        try:

            cost_price = float(cost_price)

            if cost_price <= 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Cost price must be greater than 0."
            )

            return

        # Check selling price
        try:

            selling_price = float(selling_price)

            if selling_price <= 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Selling price must be greater than 0."
            )

            return

        # Check cost price decimal places
        if "." in self.cost_price_entry.get():

            decimal_part = self.cost_price_entry.get().split(".")[1]

            if len(decimal_part) > 2:

                messagebox.showwarning(
                    "Validation",
                    "Cost price can have maximum 2 decimal places."
                )

                return

        # Check selling price decimal places
        if "." in self.selling_price_entry.get():

            decimal_part = self.selling_price_entry.get().split(".")[1]

            if len(decimal_part) > 2:

                messagebox.showwarning(
                    "Validation",
                    "Selling price can have maximum 2 decimal places."
                )

                return

        # Selling price should not be lower than cost price
        if selling_price < cost_price:

            messagebox.showwarning(
                "Validation",
                "Selling price cannot be lower than cost price."
            )

            return

        try:

            # Update product in database
            updated = self.product_model.update_product(
                self.selected_product_id,
                name,
                quantity,
                cost_price,
                selling_price
            )

            if updated:

                messagebox.showinfo(
                    "Success",
                    "Product updated successfully."
                )

                # Clear fields after update
                self.clear_fields()

                # Refresh table
                self.load_products()

            else:

                messagebox.showwarning(
                    "Update",
                    "Product was not found."
                )

        except Exception as error:

            # Show database error
            messagebox.showerror(
                "Error",
                f"Failed to update product.\n\n{error}"
            )

    # =====================================================
    # Delete Product
    # =====================================================

    def delete_product(self):

        # Check if a product is selected
        if self.selected_product_id is None:

            messagebox.showwarning(
                "Selection",
                "Please select a product first."
            )

            return

        # Ask user before deleting
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this product?"
        )

        if not confirm:
            return

        try:

            # Delete selected product
            deleted = self.product_model.delete_product(
                self.selected_product_id
            )

            if deleted:

                messagebox.showinfo(
                    "Success",
                    "Product deleted successfully."
                )

                # Clear fields
                self.clear_fields()

                # Refresh table
                self.load_products()

            else:

                messagebox.showwarning(
                    "Delete",
                    "Product was not found."
                )

        except Exception as error:

            # Show database error
            messagebox.showerror(
                "Error",
                f"Failed to delete product.\n\n{error}"
            )

    # =====================================================
    # Clear Fields
    # =====================================================

    def clear_fields(self):

        # Remove selected product
        self.selected_product_id = None

        # Clear product name
        self.name_entry.delete(
            0,
            "end"
        )

        # Clear quantity
        self.quantity_entry.delete(
            0,
            "end"
        )

        # Clear cost price
        self.cost_price_entry.delete(
            0,
            "end"
        )

        # Clear selling price
        self.selling_price_entry.delete(
            0,
            "end"
        )

        # Clear search box
        self.search_entry.delete(
            0,
            "end"
        )

        # Remove table selection
        selected = self.product_table.selection()

        if selected:
            self.product_table.selection_remove(
                *selected
            )

    # =====================================================
    # Back to Dashboard
    # =====================================================

    def back_to_dashboard(self):

        # Close product window
        self.frame.destroy()

        # Import dashboard window
        from gui.dashboard import DashboardWindow

        # Open dashboard
        DashboardWindow(
            self.app
        )

