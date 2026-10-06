
import customtkinter as ctk
from tkinter import ttk, messagebox

from models.sales import SalesModel


class SalesWindow:

    def __init__(self, app):

        self.app = app
        self.sales_model = SalesModel()

        # Store products added to the cart
        self.cart_items = []

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

        heading = ctk.CTkLabel(
            self.frame,
            text="Sales Management",
            font=("Arial", 26, "bold")
        )

        heading.pack(
            pady=(15, 10)
        )

        # =========================
        # Top Section
        # =========================

        top_frame = ctk.CTkFrame(
            self.frame
        )

        top_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Invoice Number
        ctk.CTkLabel(
            top_frame,
            text="Invoice No:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.invoice_entry = ctk.CTkEntry(
            top_frame,
            width=150
        )

        self.invoice_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        # Invoice number cannot be edited
        self.invoice_entry.configure(
            state="readonly"
        )

        # Customer
        ctk.CTkLabel(
            top_frame,
            text="Customer:"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.customer_combo = ctk.CTkComboBox(
            top_frame,
            width=200
        )

        self.customer_combo.grid(
            row=0,
            column=3,
            padx=10
        )

        # =========================
        # Product Section
        # =========================

        product_frame = ctk.CTkFrame(
            self.frame
        )

        product_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Product
        ctk.CTkLabel(
            product_frame,
            text="Product:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.product_combo = ctk.CTkComboBox(
            product_frame,
            width=230,
            command=self.product_selected
        )

        self.product_combo.grid(
            row=0,
            column=1,
            padx=10
        )

        # Stock
        ctk.CTkLabel(
            product_frame,
            text="Stock:"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.stock_label = ctk.CTkLabel(
            product_frame,
            text="0",
            font=("Arial", 14, "bold")
        )

        self.stock_label.grid(
            row=0,
            column=3,
            padx=10
        )

        # Quantity
        ctk.CTkLabel(
            product_frame,
            text="Quantity:"
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        self.quantity_entry = ctk.CTkEntry(
            product_frame,
            width=80
        )

        self.quantity_entry.grid(
            row=0,
            column=5,
            padx=10
        )

        # Unit Price
        ctk.CTkLabel(
            product_frame,
            text="Unit Price:"
        ).grid(
            row=0,
            column=6,
            padx=10
        )

        self.price_label = ctk.CTkLabel(
            product_frame,
            text="Rs. 0.00",
            font=("Arial", 14, "bold")
        )

        self.price_label.grid(
            row=0,
            column=7,
            padx=10
        )

        # Add Button
        add_button = ctk.CTkButton(
            product_frame,
            text="Add to Cart",
            width=120,
            command=self.add_to_cart
        )

        add_button.grid(
            row=0,
            column=8,
            padx=15
        )

        # =========================
        # Cart Table
        # =========================

        table_frame = ctk.CTkFrame(
            self.frame
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        columns = (
            "id",
            "product",
            "quantity",
            "unit_price",
            "total"
        )

        self.cart_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        self.cart_table.heading(
            "id",
            text="ID"
        )

        self.cart_table.heading(
            "product",
            text="Product"
        )

        self.cart_table.heading(
            "quantity",
            text="Quantity"
        )

        self.cart_table.heading(
            "unit_price",
            text="Unit Price"
        )

        self.cart_table.heading(
            "total",
            text="Total"
        )

        self.cart_table.column(
            "id",
            width=50,
            anchor="center"
        )

        self.cart_table.column(
            "product",
            width=250
        )

        self.cart_table.column(
            "quantity",
            width=100,
            anchor="center"
        )

        self.cart_table.column(
            "unit_price",
            width=120,
            anchor="center"
        )

        self.cart_table.column(
            "total",
            width=120,
            anchor="center"
        )

        self.cart_table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # Remove Button
        remove_button = ctk.CTkButton(
            table_frame,
            text="Remove Selected",
            width=140,
            command=self.remove_from_cart
        )

        remove_button.pack(
            pady=(0, 10)
        )

        # =========================
        # Bottom Section
        # =========================

        bottom_frame = ctk.CTkFrame(
            self.frame
        )

        bottom_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Subtotal
        ctk.CTkLabel(
            bottom_frame,
            text="Subtotal:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=8
        )

        self.subtotal_label = ctk.CTkLabel(
            bottom_frame,
            text="Rs. 0.00",
            font=("Arial", 14, "bold")
        )

        self.subtotal_label.grid(
            row=0,
            column=1,
            padx=10
        )

        # Discount
        ctk.CTkLabel(
            bottom_frame,
            text="Discount:"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.discount_entry = ctk.CTkEntry(
            bottom_frame,
            width=100
        )

        self.discount_entry.grid(
            row=0,
            column=3,
            padx=10
        )

        self.discount_entry.insert(
            0,
            "0"
        )

        # Total
        ctk.CTkLabel(
            bottom_frame,
            text="Grand Total:"
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        self.total_label = ctk.CTkLabel(
            bottom_frame,
            text="Rs. 0.00",
            font=("Arial", 15, "bold")
        )

        self.total_label.grid(
            row=0,
            column=5,
            padx=10
        )

        # Payment
        ctk.CTkLabel(
            bottom_frame,
            text="Payment:"
        ).grid(
            row=0,
            column=6,
            padx=10
        )

        self.payment_entry = ctk.CTkEntry(
            bottom_frame,
            width=100
        )

        self.payment_entry.grid(
            row=0,
            column=7,
            padx=10
        )

        self.payment_entry.bind(
            "<KeyRelease>",
            lambda event: self.calculate_balance()
        )

        # Balance
        ctk.CTkLabel(
            bottom_frame,
            text="Balance:"
        ).grid(
            row=0,
            column=8,
            padx=10
        )

        self.balance_label = ctk.CTkLabel(
            bottom_frame,
            text="Rs. 0.00",
            font=("Arial", 14, "bold")
        )

        self.balance_label.grid(
            row=0,
            column=9,
            padx=10
        )

        # =========================
        # Buttons
        # =========================

        button_frame = ctk.CTkFrame(
            self.frame
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        save_button = ctk.CTkButton(
            button_frame,
            text="Save Sale",
            width=130,
            command=self.save_sale
        )

        save_button.pack(
            side="left",
            padx=10
        )

        clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            width=130,
            command=self.clear_sale
        )

        clear_button.pack(
            side="left",
            padx=10
        )

        back_button = ctk.CTkButton(
            button_frame,
            text="Back to Dashboard",
            width=150,
            command=self.back_to_dashboard
        )

        back_button.pack(
            side="right",
            padx=10
        )

        # =========================
        # Load Data
        # =========================

        self.load_customers()
        self.load_products()
        self.generate_invoice()

    # ==================================================
    # Load Customers
    # ==================================================

    def load_customers(self):

        try:

            # Get customers from database
            customers = self.sales_model.get_customers()

            # Add walk-in customer
            self.customer_map = {
                "Walk-in Customer": None
            }

            customer_list = [
                "Walk-in Customer"
            ]

            # Add customers to the list
            for customer_id, name in customers:

                display_name = f"{customer_id} - {name}"

                customer_list.append(
                    display_name
                )

                self.customer_map[
                    display_name
                ] = customer_id

            self.customer_combo.configure(
                values=customer_list
            )

            self.customer_combo.set(
                "Walk-in Customer"
            )

        except Exception as error:

            # Show error if customers cannot load
            messagebox.showerror(
                "Error",
                f"Could not load customers.\n\n{error}"
            )

    # ==================================================
    # Load Products
    # ==================================================

    def load_products(self):

        try:

            # Get available products
            products = self.sales_model.get_products()

            self.product_map = {}

            product_list = []

            # Add products to the combo box
            for product_id, name, quantity, cost_price, selling_price in products:

                display_name = f"{product_id} - {name}"

                product_list.append(
                    display_name
                )

                self.product_map[
                    display_name
                ] = product_id

            self.product_combo.configure(
                values=product_list
            )

            if product_list:

                self.product_combo.set(
                    product_list[0]
                )

                self.product_selected(
                    product_list[0]
                )

            else:

                self.product_combo.set(
                    ""
                )

        except Exception as error:

            # Show error if products cannot load
            messagebox.showerror(
                "Error",
                f"Could not load products.\n\n{error}"
            )

    # ==================================================
    # Product Selected
    # ==================================================

    def product_selected(self, selected_product):

        # Check if a product was selected
        if not selected_product:
            return

        if selected_product not in self.product_map:
            return

        product_id = self.product_map[
            selected_product
        ]

        try:

            # Get selected product details
            product = self.sales_model.get_product(
                product_id
            )

            if product:

                product_id = product[0]
                product_name = product[1]
                stock = product[2]
                cost_price = product[3]
                selling_price = product[4]

                # Show available stock
                self.stock_label.configure(
                    text=str(stock)
                )

                # Show selling price in Rs.
                self.price_label.configure(
                    text=f"Rs. {float(selling_price):.2f}"
                )

        except Exception as error:

            # Show error if product details cannot load
            messagebox.showerror(
                "Error",
                f"Could not load product details.\n\n{error}"
            )

    # ==================================================
    # Add To Cart
    # ==================================================

    def add_to_cart(self):

        # Get selected product
        selected_product = self.product_combo.get()

        if not selected_product:

            messagebox.showwarning(
                "Warning",
                "Please select a product."
            )

            return

        # Get quantity from the input
        quantity_text = self.quantity_entry.get().strip()

        if not quantity_text:

            messagebox.showwarning(
                "Warning",
                "Please enter quantity."
            )

            return

        try:

            # Quantity must be a whole number
            quantity = int(
                quantity_text
            )

        except ValueError:

            messagebox.showwarning(
                "Warning",
                "Quantity must be a whole number."
            )

            return

        # Quantity must be positive
        if quantity <= 0:

            messagebox.showwarning(
                "Warning",
                "Quantity must be greater than 0."
            )

            return

        product_id = self.product_map.get(
            selected_product
        )

        if product_id is None:
            return

        try:

            # Get latest product stock
            product = self.sales_model.get_product(
                product_id
            )

            if not product:

                messagebox.showerror(
                    "Error",
                    "Product not found."
                )

                return

            product_id = product[0]
            product_name = product[1]
            stock = int(product[2])
            cost_price = float(product[3])
            selling_price = float(product[4])

            # Check available stock
            if quantity > stock:

                messagebox.showwarning(
                    "Stock Error",
                    f"Only {stock} items are available."
                )

                return

            # Check duplicate product
            for item in self.cart_items:

                if item["product_id"] == product_id:

                    new_quantity = (
                        item["quantity"] + quantity
                    )

                    if new_quantity > stock:

                        messagebox.showwarning(
                            "Stock Error",
                            f"Only {stock} items are available."
                        )

                        return

                    # Update existing cart item
                    item["quantity"] = new_quantity

                    item["total"] = (
                        new_quantity * selling_price
                    )

                    self.refresh_cart()

                    self.quantity_entry.delete(
                        0,
                        "end"
                    )

                    return

            # Add new item
            item = {
                "product_id": product_id,
                "product_name": product_name,
                "quantity": quantity,
                "unit_price": selling_price,
                "cost_price": cost_price,
                "total": quantity * selling_price
            }

            self.cart_items.append(
                item
            )

            # Refresh cart table
            self.refresh_cart()

            self.quantity_entry.delete(
                0,
                "end"
            )

        except Exception as error:

            # Show error when adding product
            messagebox.showerror(
                "Error",
                f"Could not add product.\n\n{error}"
            )

    # ==================================================
    # Refresh Cart
    # ==================================================

    def refresh_cart(self):

        # Clear old cart rows
        for item in self.cart_table.get_children():

            self.cart_table.delete(
                item
            )

        subtotal = 0

        # Add current cart items
        for item in self.cart_items:

            self.cart_table.insert(
                "",
                "end",
                values=(
                    item["product_id"],
                    item["product_name"],
                    item["quantity"],
                    f"Rs. {item['unit_price']:.2f}",
                    f"Rs. {item['total']:.2f}"
                )
            )

            subtotal += item["total"]

        # Show subtotal
        self.subtotal_label.configure(
            text=f"Rs. {subtotal:.2f}"
        )

        self.calculate_total()

    # ==================================================
    # Remove From Cart
    # ==================================================

    def remove_from_cart(self):

        # Get selected cart item
        selected = self.cart_table.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select an item to remove."
            )

            return

        selected_item = self.cart_table.item(
            selected[0]
        )

        product_id = int(
            selected_item["values"][0]
        )

        # Remove selected product
        self.cart_items = [
            item
            for item in self.cart_items
            if item["product_id"] != product_id
        ]

        self.refresh_cart()

    # ==================================================
    # Calculate Total
    # ==================================================

    def calculate_total(self):

        try:

            # Calculate subtotal
            subtotal = sum(
                item["total"]
                for item in self.cart_items
            )

            # Get discount value
            discount_text = self.discount_entry.get().strip()

            if discount_text == "":
                discount = 0
            else:
                discount = float(discount_text)

            # Do not allow negative discount
            if discount < 0:
                discount = 0

            total = subtotal - discount

            # Total cannot be negative
            if total < 0:
                total = 0

            # Show total in Rs.
            self.total_label.configure(
                text=f"Rs. {total:.2f}"
            )

            self.calculate_balance()

        except ValueError:

            # Show default value for invalid discount
            self.total_label.configure(
                text="Rs. 0.00"
            )

    # ==================================================
    # Calculate Balance
    # ==================================================

    def calculate_balance(self):

        try:

            # Get total without Rs. text
            total_text = self.total_label.cget(
                "text"
            ).replace(
                "Rs. ",
                ""
            )

            total = float(
                total_text
            )

            # Get payment value
            payment_text = self.payment_entry.get().strip()

            if payment_text == "":
                payment = 0
            else:
                payment = float(payment_text)

            balance = payment - total

            # Show balance in Rs.
            self.balance_label.configure(
                text=f"Rs. {balance:.2f}"
            )

        except ValueError:

            # Show default value for invalid payment
            self.balance_label.configure(
                text="Rs. 0.00"
            )

    # ==================================================
    # Generate Invoice
    # ==================================================

    def generate_invoice(self):

        try:

            # Generate a new invoice number
            invoice_number = (
                self.sales_model.generate_invoice_number()
            )

            self.invoice_entry.configure(
                state="normal"
            )

            self.invoice_entry.delete(
                0,
                "end"
            )

            self.invoice_entry.insert(
                0,
                invoice_number
            )

            self.invoice_entry.configure(
                state="readonly"
            )

        except Exception as error:

            # Show invoice error
            messagebox.showerror(
                "Error",
                f"Could not generate invoice number.\n\n{error}"
            )

    # ==================================================
    # Save Sale
    # ==================================================

    def save_sale(self):

        # Check if cart has products
        if not self.cart_items:

            messagebox.showwarning(
                "Warning",
                "Please add at least one product."
            )

            return

        try:

            # Calculate subtotal
            subtotal = sum(
                item["total"]
                for item in self.cart_items
            )

            # Get discount
            discount_text = (
                self.discount_entry.get().strip()
            )

            if discount_text == "":
                discount = 0
            else:
                discount = float(discount_text)

            # Check discount
            if discount < 0:

                messagebox.showwarning(
                    "Warning",
                    "Discount cannot be negative."
                )

                return

            if discount > subtotal:

                messagebox.showwarning(
                    "Warning",
                    "Discount cannot be greater than subtotal."
                )

                return

            total = subtotal - discount

            # Get payment
            payment_text = (
                self.payment_entry.get().strip()
            )

            if payment_text == "":

                messagebox.showwarning(
                    "Warning",
                    "Please enter payment."
                )

                return

            payment = float(
                payment_text
            )

            # Payment cannot be negative
            if payment < 0:

                messagebox.showwarning(
                    "Warning",
                    "Payment cannot be negative."
                )

                return

            # Check payment amount
            if payment < total:

                messagebox.showwarning(
                    "Payment Error",
                    "Payment is less than the total amount."
                )

                return

            balance = payment - total

            # Get invoice number
            invoice_number = (
                self.invoice_entry.get()
            )

            # Get selected customer
            customer_name = (
                self.customer_combo.get()
            )

            customer_id = self.customer_map.get(
                customer_name
            )

            # Save sale to database
            sale_id = self.sales_model.save_sale(
                invoice_number,
                customer_id,
                subtotal,
                discount,
                total,
                payment,
                balance,
                self.cart_items
            )

            messagebox.showinfo(
                "Success",
                f"Sale saved successfully.\n\n"
                f"Invoice: {invoice_number}\n"
                f"Total: Rs. {total:.2f}\n"
                f"Balance: Rs. {balance:.2f}"
            )

            # Clear the sale after saving
            self.clear_sale()

        except ValueError as error:

            # Show invalid input message
            messagebox.showwarning(
                "Invalid Input",
                str(error)
            )

        except Exception as error:

            # Show database error
            messagebox.showerror(
                "Error",
                f"Could not save sale.\n\n{error}"
            )

    # ==================================================
    # Clear Sale
    # ==================================================

    def clear_sale(self):

        # Empty the cart
        self.cart_items = []

        # Clear cart table
        for item in self.cart_table.get_children():

            self.cart_table.delete(
                item
            )

        # Clear quantity
        self.quantity_entry.delete(
            0,
            "end"
        )

        # Reset discount
        self.discount_entry.delete(
            0,
            "end"
        )

        self.discount_entry.insert(
            0,
            "0"
        )

        # Clear payment
        self.payment_entry.delete(
            0,
            "end"
        )

        # Reset money values
        self.subtotal_label.configure(
            text="Rs. 0.00"
        )

        self.total_label.configure(
            text="Rs. 0.00"
        )

        self.balance_label.configure(
            text="Rs. 0.00"
        )

        # Reset product details
        self.stock_label.configure(
            text="0"
        )

        self.price_label.configure(
            text="Rs. 0.00"
        )

        # Reload products and invoice
        self.load_products()
        self.generate_invoice()

    # ==================================================
    # Back To Dashboard
    # ==================================================

    def back_to_dashboard(self):

        # Remove current window
        self.frame.destroy()

        # Open dashboard
        from gui.dashboard import DashboardWindow

        DashboardWindow(
            self.app
        )

