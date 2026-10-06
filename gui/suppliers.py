
import customtkinter as ctk
from tkinter import ttk, messagebox
import re

from models.supplier import SupplierModel


class SuppliersWindow:

    def __init__(self, app):

        self.app = app
        self.supplier_model = SupplierModel()
        self.selected_id = None

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
            text="Supplier Management",
            font=("Arial", 30, "bold")
        )

        heading.pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self.frame,
            text="Manage suppliers and supplied products",
            font=("Arial", 15)
        )

        subtitle.pack(
            anchor="w",
            padx=30,
            pady=(0, 15)
        )

        # =========================
        # Input Frame
        # =========================

        input_frame = ctk.CTkFrame(
            self.frame
        )

        input_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        # Supplier Name

        self.name_entry = ctk.CTkEntry(
            input_frame,
            width=190,
            height=40,
            placeholder_text="Supplier Name"
        )

        self.name_entry.grid(
            row=0,
            column=0,
            padx=8,
            pady=15
        )

        # Item Name

        self.item_entry = ctk.CTkEntry(
            input_frame,
            width=190,
            height=40,
            placeholder_text="Item Name"
        )

        self.item_entry.grid(
            row=0,
            column=1,
            padx=8
        )

        # Quantity

        self.quantity_entry = ctk.CTkEntry(
            input_frame,
            width=120,
            height=40,
            placeholder_text="Quantity"
        )

        self.quantity_entry.grid(
            row=0,
            column=2,
            padx=8
        )

        # Unit Price

        self.price_entry = ctk.CTkEntry(
            input_frame,
            width=140,
            height=40,
            placeholder_text="Unit Cost Price (Rs.)"
        )

        self.price_entry.grid(
            row=0,
            column=3,
            padx=8
        )

        # Phone

        self.phone_entry = ctk.CTkEntry(
            input_frame,
            width=160,
            height=40,
            placeholder_text="Phone Number"
        )

        self.phone_entry.grid(
            row=1,
            column=0,
            padx=8,
            pady=(0, 15)
        )

        # Email

        self.email_entry = ctk.CTkEntry(
            input_frame,
            width=210,
            height=40,
            placeholder_text="Email Address"
        )

        self.email_entry.grid(
            row=1,
            column=1,
            padx=8
        )

        # Selling Price Display

        self.selling_price_label = ctk.CTkLabel(
            input_frame,
            text="Selling Price: Rs. 0.00",
            font=("Arial", 14, "bold")
        )

        self.selling_price_label.grid(
            row=1,
            column=2,
            columnspan=2,
            padx=8,
            sticky="w"
        )

        # Update selling price when unit price changes

        self.price_entry.bind(
            "<KeyRelease>",
            self.calculate_selling_price
        )

        # =========================
        # Buttons
        # =========================

        button_frame = ctk.CTkFrame(
            self.frame,
            fg_color="transparent"
        )

        button_frame.pack(
            pady=8
        )

        # Add

        add_button = ctk.CTkButton(
            button_frame,
            text="Add Supplier",
            width=140,
            command=self.add_supplier
        )

        add_button.grid(
            row=0,
            column=0,
            padx=5
        )

        # Update

        update_button = ctk.CTkButton(
            button_frame,
            text="Update",
            width=140,
            command=self.update_supplier
        )

        update_button.grid(
            row=0,
            column=1,
            padx=5
        )

        # Delete

        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            width=140,
            command=self.delete_supplier
        )

        delete_button.grid(
            row=0,
            column=2,
            padx=5
        )

        # Clear

        clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            width=140,
            command=self.clear_fields
        )

        clear_button.grid(
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
            fill="x",
            padx=30,
            pady=(5, 0)
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=300,
            height=38,
            placeholder_text="Search supplier, item, phone or email"
        )

        self.search_entry.pack(
            side="left",
            padx=(0, 10)
        )

        search_button = ctk.CTkButton(
            search_frame,
            text="Search",
            width=100,
            command=self.search_supplier
        )

        search_button.pack(
            side="left",
            padx=5
        )

        show_all_button = ctk.CTkButton(
            search_frame,
            text="Show All",
            width=100,
            command=self.show_all_suppliers
        )

        show_all_button.pack(
            side="left",
            padx=5
        )

        # =========================
        # Supplier Table
        # =========================

        self.table = ttk.Treeview(
            self.frame,
            columns=(
                "ID",
                "Supplier",
                "Item",
                "Quantity",
                "Unit Price",
                "Cost",
                "Selling Price",
                "Phone",
                "Email"
            ),
            show="headings"
        )

        # =========================
        # Headings
        # =========================

        self.table.heading(
            "ID",
            text="ID"
        )

        self.table.heading(
            "Supplier",
            text="Supplier"
        )

        self.table.heading(
            "Item",
            text="Item"
        )

        self.table.heading(
            "Quantity",
            text="Quantity"
        )

        self.table.heading(
            "Unit Price",
            text="Unit Price"
        )

        self.table.heading(
            "Cost",
            text="Total Cost"
        )

        self.table.heading(
            "Selling Price",
            text="Selling Price"
        )

        self.table.heading(
            "Phone",
            text="Phone"
        )

        self.table.heading(
            "Email",
            text="Email"
        )

        # =========================
        # Column Widths
        # =========================

        self.table.column(
            "ID",
            width=45,
            anchor="center"
        )

        self.table.column(
            "Supplier",
            width=130
        )

        self.table.column(
            "Item",
            width=120
        )

        self.table.column(
            "Quantity",
            width=75,
            anchor="center"
        )

        self.table.column(
            "Unit Price",
            width=100,
            anchor="e"
        )

        self.table.column(
            "Cost",
            width=100,
            anchor="e"
        )

        self.table.column(
            "Selling Price",
            width=110,
            anchor="e"
        )

        self.table.column(
            "Phone",
            width=110
        )

        self.table.column(
            "Email",
            width=180
        )

        self.table.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=15
        )

        # =========================
        # Select Row
        # =========================

        self.table.bind(
            "<ButtonRelease-1>",
            self.select_supplier
        )

        # =========================
        # Back Button
        # =========================

        back_button = ctk.CTkButton(
            self.frame,
            text="Back to Dashboard",
            width=180,
            height=40,
            command=self.back_to_dashboard
        )

        back_button.pack(
            pady=(0, 15)
        )

        # =========================
        # Load Suppliers
        # =========================

        self.load_suppliers()

    # =====================================================
    # Validate Text
    # =====================================================

    def validate_text(self, value):

        # Allow letters, numbers, spaces and basic characters
        return bool(
            re.match(
                r"^[A-Za-z0-9 .,&'()-]+$",
                value
            )
        )

    # =====================================================
    # Validate Phone
    # =====================================================

    def validate_phone(self, phone):

        # Phone number should contain only numbers
        return phone.isdigit() and len(phone) == 10

    # =====================================================
    # Validate Email
    # =====================================================

    def validate_email(self, email):

        # Check a simple email format
        return bool(
            re.match(
                r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
                email
            )
        )

    # =====================================================
    # Calculate Selling Price
    # =====================================================

    def calculate_selling_price(self, event=None):

        try:

            # Get the unit price
            unit_price = float(
                self.price_entry.get().strip()
            )

            # Calculate 3% profit
            selling_price = unit_price * 1.03

            # Show selling price in Rs.
            self.selling_price_label.configure(
                text=f"Selling Price: Rs. {selling_price:.2f}"
            )

        except ValueError:

            # Show default value for invalid input
            self.selling_price_label.configure(
                text="Selling Price: Rs. 0.00"
            )

    # =====================================================
    # Load Suppliers
    # =====================================================

    def load_suppliers(self):

        # Clear the table
        for row in self.table.get_children():
            self.table.delete(row)

        try:

            # Get suppliers from database
            suppliers = self.supplier_model.get_suppliers()

            # Add suppliers to the table
            for supplier in suppliers:

                self.insert_supplier_row(
                    supplier
                )

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not load suppliers.\n\n{e}"
            )

    # =====================================================
    # Insert Supplier Row
    # =====================================================

    def insert_supplier_row(self, supplier):

        # Add supplier data to the table
        self.table.insert(
            "",
            "end",
            values=(
                supplier[0],
                supplier[1],
                supplier[2],
                supplier[3],
                f"Rs. {float(supplier[4]):.2f}",
                f"Rs. {float(supplier[5]):.2f}",
                f"Rs. {float(supplier[6]):.2f}",
                supplier[7],
                supplier[8]
            )
        )

    # =====================================================
    # Add Supplier
    # =====================================================

    def add_supplier(self):

        # Get values from input fields
        name = self.name_entry.get().strip()
        item = self.item_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        unit_price = self.price_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        # Check empty fields

        if not all(
            [
                name,
                item,
                quantity,
                unit_price,
                phone,
                email
            ]
        ):

            messagebox.showwarning(
                "Warning",
                "Please fill all fields."
            )

            return

        # Validate supplier name

        if not self.validate_text(name):

            messagebox.showerror(
                "Invalid Name",
                "Supplier name contains invalid characters."
            )

            return

        # Validate item name

        if not self.validate_text(item):

            messagebox.showerror(
                "Invalid Item",
                "Item name contains invalid characters."
            )

            return

        # Validate quantity

        try:

            quantity = int(quantity)

        except ValueError:

            messagebox.showerror(
                "Invalid Quantity",
                "Quantity must be a whole number."
            )

            return

        # Check positive quantity

        if quantity <= 0:

            messagebox.showwarning(
                "Warning",
                "Quantity must be greater than 0."
            )

            return

        # Validate money value

        try:

            unit_price = float(unit_price)

        except ValueError:

            messagebox.showerror(
                "Invalid Price",
                "Unit price must be a valid Rs. amount."
            )

            return

        # Check positive price

        if unit_price <= 0:

            messagebox.showwarning(
                "Warning",
                "Unit price must be greater than Rs. 0."
            )

            return

        # Validate phone number

        if not self.validate_phone(phone):

            messagebox.showerror(
                "Invalid Phone",
                "Phone number must contain exactly 10 digits."
            )

            return

        # Validate email

        if not self.validate_email(email):

            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return

        try:

            # Save supplier details
            self.supplier_model.add_supplier(
                name,
                item,
                quantity,
                unit_price,
                phone,
                email
            )

            messagebox.showinfo(
                "Success",
                "Supplier added successfully."
            )

            # Clear inputs and reload table
            self.clear_fields()
            self.load_suppliers()

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not add supplier.\n\n{e}"
            )

    # =====================================================
    # Search Supplier
    # =====================================================

    def search_supplier(self):

        # Get search text
        search_text = self.search_entry.get().strip()

        # Show all suppliers when search is empty
        if not search_text:

            self.load_suppliers()

            return

        try:

            # Search suppliers
            suppliers = self.supplier_model.search_suppliers(
                search_text
            )

            # Clear old table data
            for row in self.table.get_children():
                self.table.delete(row)

            # Add search results
            for supplier in suppliers:

                self.insert_supplier_row(
                    supplier
                )

        except Exception as e:

            # Show search error
            messagebox.showerror(
                "Database Error",
                f"Could not search suppliers.\n\n{e}"
            )

    # =====================================================
    # Show All Suppliers
    # =====================================================

    def show_all_suppliers(self):

        # Clear search box
        self.search_entry.delete(
            0,
            "end"
        )

        # Load all suppliers
        self.load_suppliers()

    # =====================================================
    # Select Supplier
    # =====================================================

    def select_supplier(self, event):

        # Get selected table row
        selected = self.table.focus()

        if not selected:
            return

        # Get row values
        values = self.table.item(
            selected,
            "values"
        )

        if not values:
            return

        # Store selected supplier ID
        self.selected_id = int(
            values[0]
        )

        # Supplier Name

        self.name_entry.delete(
            0,
            "end"
        )

        self.name_entry.insert(
            0,
            values[1]
        )

        # Item

        self.item_entry.delete(
            0,
            "end"
        )

        self.item_entry.insert(
            0,
            values[2]
        )

        # Quantity

        self.quantity_entry.delete(
            0,
            "end"
        )

        self.quantity_entry.insert(
            0,
            values[3]
        )

        # Unit Price

        self.price_entry.delete(
            0,
            "end"
        )

        # Remove Rs. before putting price into entry
        price_value = str(values[4]).replace(
            "Rs. ",
            ""
        )

        self.price_entry.insert(
            0,
            price_value
        )

        # Phone

        self.phone_entry.delete(
            0,
            "end"
        )

        self.phone_entry.insert(
            0,
            values[7]
        )

        # Email

        self.email_entry.delete(
            0,
            "end"
        )

        self.email_entry.insert(
            0,
            values[8]
        )

        # Update selling price display

        try:

            # Remove Rs. before converting to number
            selling_price_value = str(
                values[6]
            ).replace(
                "Rs. ",
                ""
            )

            selling_price = float(
                selling_price_value
            )

            self.selling_price_label.configure(
                text=f"Selling Price: Rs. {selling_price:.2f}"
            )

        except ValueError:

            # Show default selling price
            self.selling_price_label.configure(
                text="Selling Price: Rs. 0.00"
            )

    # =====================================================
    # Update Supplier
    # =====================================================

    def update_supplier(self):

        # Check if a supplier is selected
        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a supplier."
            )

            return

        # Get values from input fields
        name = self.name_entry.get().strip()
        item = self.item_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        unit_price = self.price_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        # Check empty fields

        if not all(
            [
                name,
                item,
                quantity,
                unit_price,
                phone,
                email
            ]
        ):

            messagebox.showwarning(
                "Warning",
                "Please fill all fields."
            )

            return

        # Validate supplier name

        if not self.validate_text(name):

            messagebox.showerror(
                "Invalid Name",
                "Supplier name contains invalid characters."
            )

            return

        # Validate item name

        if not self.validate_text(item):

            messagebox.showerror(
                "Invalid Item",
                "Item name contains invalid characters."
            )

            return

        # Validate quantity

        try:

            quantity = int(quantity)

        except ValueError:

            messagebox.showerror(
                "Invalid Quantity",
                "Quantity must be a whole number."
            )

            return

        # Check positive quantity

        if quantity <= 0:

            messagebox.showwarning(
                "Warning",
                "Quantity must be greater than 0."
            )

            return

        # Validate unit price

        try:

            unit_price = float(unit_price)

        except ValueError:

            messagebox.showerror(
                "Invalid Price",
                "Unit price must be a valid Rs. amount."
            )

            return

        # Check positive price

        if unit_price <= 0:

            messagebox.showwarning(
                "Warning",
                "Unit price must be greater than Rs. 0."
            )

            return

        # Validate phone number

        if not self.validate_phone(phone):

            messagebox.showerror(
                "Invalid Phone",
                "Phone number must contain exactly 10 digits."
            )

            return

        # Validate email

        if not self.validate_email(email):

            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return

        try:

            # Update supplier details
            updated = self.supplier_model.update_supplier(
                self.selected_id,
                name,
                item,
                quantity,
                unit_price,
                phone,
                email
            )

            if updated:

                messagebox.showinfo(
                    "Success",
                    "Supplier updated successfully."
                )

            else:

                messagebox.showwarning(
                    "Warning",
                    "Supplier was not found."
                )

            # Clear inputs and reload table
            self.clear_fields()
            self.load_suppliers()

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not update supplier.\n\n{e}"
            )

    # =====================================================
    # Delete Supplier
    # =====================================================

    def delete_supplier(self):

        # Check if a supplier is selected
        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a supplier."
            )

            return

        # Ask before deleting
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this supplier?"
        )

        if not confirm:
            return

        try:

            # Delete the supplier
            deleted = self.supplier_model.delete_supplier(
                self.selected_id
            )

            if deleted:

                messagebox.showinfo(
                    "Success",
                    "Supplier deleted successfully."
                )

            else:

                messagebox.showwarning(
                    "Warning",
                    "Supplier was not found."
                )

            # Clear inputs and reload table
            self.clear_fields()
            self.load_suppliers()

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not delete supplier.\n\n{e}"
            )

    # =====================================================
    # Clear Fields
    # =====================================================

    def clear_fields(self):

        # Clear supplier name
        self.name_entry.delete(
            0,
            "end"
        )

        # Clear item name
        self.item_entry.delete(
            0,
            "end"
        )

        # Clear quantity
        self.quantity_entry.delete(
            0,
            "end"
        )

        # Clear price
        self.price_entry.delete(
            0,
            "end"
        )

        # Clear phone
        self.phone_entry.delete(
            0,
            "end"
        )

        # Clear email
        self.email_entry.delete(
            0,
            "end"
        )

        # Clear search
        self.search_entry.delete(
            0,
            "end"
        )

        # Reset selling price
        self.selling_price_label.configure(
            text="Selling Price: Rs. 0.00"
        )

        # Remove selected supplier
        self.selected_id = None

        # Remove table selection
        for item in self.table.selection():

            self.table.selection_remove(item)

    # =====================================================
    # Back to Dashboard
    # =====================================================

    def back_to_dashboard(self):

        # Remove current window
        self.frame.destroy()

        # Open dashboard
        from gui.dashboard import DashboardWindow

        DashboardWindow(self.app)

