
import customtkinter as ctk
from tkinter import ttk, messagebox

from models.customer import CustomerModel


class CustomersWindow:

    def __init__(self, app):

        self.app = app
        self.customer_model = CustomerModel()

        # Store the selected customer ID
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
            text="Customer Management",
            font=("Arial", 30, "bold")
        )

        heading.pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        # Show a short description
        subtitle = ctk.CTkLabel(
            self.frame,
            text="Manage customer information",
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

        # =========================
        # Customer Name
        # =========================

        # Enter customer name
        self.name_entry = ctk.CTkEntry(
            input_frame,
            width=220,
            height=40,
            placeholder_text="Customer Name"
        )

        self.name_entry.grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        # =========================
        # Phone
        # =========================

        # Enter customer phone number
        self.phone_entry = ctk.CTkEntry(
            input_frame,
            width=180,
            height=40,
            placeholder_text="Phone Number"
        )

        self.phone_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        # =========================
        # Email
        # =========================

        # Enter customer email
        self.email_entry = ctk.CTkEntry(
            input_frame,
            width=250,
            height=40,
            placeholder_text="Email Address"
        )

        self.email_entry.grid(
            row=0,
            column=2,
            padx=10
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

        # Add customer button
        add_button = ctk.CTkButton(
            button_frame,
            text="Add Customer",
            width=140,
            command=self.add_customer
        )

        add_button.grid(
            row=0,
            column=0,
            padx=5
        )

        # Update customer button
        update_button = ctk.CTkButton(
            button_frame,
            text="Update",
            width=140,
            command=self.update_customer
        )

        update_button.grid(
            row=0,
            column=1,
            padx=5
        )

        # Delete customer button
        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            width=140,
            command=self.delete_customer
        )

        delete_button.grid(
            row=0,
            column=2,
            padx=5
        )

        # Clear fields button
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

        # Search customer information
        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=300,
            height=38,
            placeholder_text="Search by name, phone or email"
        )

        self.search_entry.pack(
            side="left",
            padx=(0, 10)
        )

        # Search button
        search_button = ctk.CTkButton(
            search_frame,
            text="Search",
            width=100,
            command=self.search_customer
        )

        search_button.pack(
            side="left",
            padx=5
        )

        # Show all customers button
        show_all_button = ctk.CTkButton(
            search_frame,
            text="Show All",
            width=100,
            command=self.show_all_customers
        )

        show_all_button.pack(
            side="left",
            padx=5
        )

        # =========================
        # Customer Table
        # =========================

        # Create customer table
        self.table = ttk.Treeview(
            self.frame,
            columns=(
                "ID",
                "Name",
                "Phone",
                "Email"
            ),
            show="headings"
        )

        # =========================
        # Table Headings
        # =========================

        self.table.heading(
            "ID",
            text="ID"
        )

        self.table.heading(
            "Name",
            text="Customer Name"
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
            width=60,
            anchor="center"
        )

        self.table.column(
            "Name",
            width=200
        )

        self.table.column(
            "Phone",
            width=150
        )

        self.table.column(
            "Email",
            width=280
        )

        # Show customer table
        self.table.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=15
        )

        # =========================
        # Select Row
        # =========================

        # Detect selected customer
        self.table.bind(
            "<ButtonRelease-1>",
            self.select_customer
        )

        # =========================
        # Back Button
        # =========================

        # Return to dashboard
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
        # Load Customers
        # =========================

        # Load customers when window opens
        self.load_customers()

    # =====================================================
    # Load Customers
    # =====================================================

    def load_customers(self):

        # Clear existing table data
        for row in self.table.get_children():
            self.table.delete(row)

        try:

            # Get customers from database
            customers = self.customer_model.get_customers()

            # Add customers to table
            for customer in customers:

                self.table.insert(
                    "",
                    "end",
                    values=(
                        customer[0],
                        customer[1],
                        customer[2],
                        customer[3]
                    )
                )

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not load customers.\n\n{e}"
            )

    # =====================================================
    # Validate Customer Fields
    # =====================================================

    def validate_customer_fields(self):

        # Get values from input fields
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        # Check empty fields
        if not name or not phone or not email:

            messagebox.showwarning(
                "Validation",
                "Please fill all fields."
            )

            return None

        # Check customer name
        if not all(
            char.isalpha() or char.isspace()
            for char in name
        ):

            messagebox.showwarning(
                "Validation",
                "Customer name can contain letters and spaces only."
            )

            return None

        # Check phone number
        if not phone.isdigit():

            messagebox.showwarning(
                "Validation",
                "Phone number must contain numbers only."
            )

            return None

        # Check phone number length
        if len(phone) < 9 or len(phone) > 15:

            messagebox.showwarning(
                "Validation",
                "Please enter a valid phone number."
            )

            return None

        # Check email format
        if "@" not in email or "." not in email:

            messagebox.showwarning(
                "Validation",
                "Please enter a valid email address."
            )

            return None

        # Return valid values
        return name, phone, email

    # =====================================================
    # Add Customer
    # =====================================================

    def add_customer(self):

        # Validate customer input
        values = self.validate_customer_fields()

        if values is None:
            return

        name, phone, email = values

        try:

            # Save customer to database
            self.customer_model.add_customer(
                name,
                phone,
                email
            )

            messagebox.showinfo(
                "Success",
                "Customer added successfully."
            )

            # Clear fields after adding
            self.clear_fields()

            # Refresh customer table
            self.load_customers()

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not add customer.\n\n{e}"
            )

    # =====================================================
    # Search Customer
    # =====================================================

    def search_customer(self):

        # Get search text
        search_text = self.search_entry.get().strip()

        # Show all customers if search is empty
        if not search_text:

            self.load_customers()

            return

        try:

            # Search customer data
            customers = self.customer_model.search_customers(
                search_text
            )

            # Clear old table data
            for row in self.table.get_children():
                self.table.delete(row)

            # Add search results
            for customer in customers:

                self.table.insert(
                    "",
                    "end",
                    values=(
                        customer[0],
                        customer[1],
                        customer[2],
                        customer[3]
                    )
                )

        except Exception as e:

            # Show search error
            messagebox.showerror(
                "Database Error",
                f"Could not search customers.\n\n{e}"
            )

    # =====================================================
    # Show All Customers
    # =====================================================

    def show_all_customers(self):

        # Clear search box
        self.search_entry.delete(
            0,
            "end"
        )

        # Load all customers
        self.load_customers()

    # =====================================================
    # Select Customer
    # =====================================================

    def select_customer(self, event):

        # Get selected row
        selected = self.table.focus()

        if not selected:
            return

        # Get selected customer values
        values = self.table.item(
            selected,
            "values"
        )

        if not values:
            return

        # Store customer ID
        self.selected_id = int(values[0])

        # Fill customer name
        self.name_entry.delete(
            0,
            "end"
        )

        self.name_entry.insert(
            0,
            values[1]
        )

        # Fill phone number
        self.phone_entry.delete(
            0,
            "end"
        )

        self.phone_entry.insert(
            0,
            values[2]
        )

        # Fill email address
        self.email_entry.delete(
            0,
            "end"
        )

        self.email_entry.insert(
            0,
            values[3]
        )

    # =====================================================
    # Update Customer
    # =====================================================

    def update_customer(self):

        # Check if customer is selected
        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a customer."
            )

            return

        # Validate customer input
        values = self.validate_customer_fields()

        if values is None:
            return

        name, phone, email = values

        try:

            # Update customer in database
            updated = self.customer_model.update_customer(
                self.selected_id,
                name,
                phone,
                email
            )

            if updated:

                messagebox.showinfo(
                    "Success",
                    "Customer updated successfully."
                )

            else:

                messagebox.showwarning(
                    "Warning",
                    "Customer was not found."
                )

            # Clear fields and refresh table
            self.clear_fields()
            self.load_customers()

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not update customer.\n\n{e}"
            )

    # =====================================================
    # Delete Customer
    # =====================================================

    def delete_customer(self):

        # Check if customer is selected
        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a customer."
            )

            return

        # Ask before deleting
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this customer?"
        )

        if not confirm:
            return

        try:

            # Delete selected customer
            deleted = self.customer_model.delete_customer(
                self.selected_id
            )

            if deleted:

                messagebox.showinfo(
                    "Success",
                    "Customer deleted successfully."
                )

            else:

                messagebox.showwarning(
                    "Warning",
                    "Customer was not found."
                )

            # Clear fields and refresh table
            self.clear_fields()
            self.load_customers()

        except Exception as e:

            # Show database error
            messagebox.showerror(
                "Database Error",
                f"Could not delete customer.\n\n{e}"
            )

    # =====================================================
    # Clear Fields
    # =====================================================

    def clear_fields(self):

        # Clear customer name
        self.name_entry.delete(
            0,
            "end"
        )

        # Clear phone number
        self.phone_entry.delete(
            0,
            "end"
        )

        # Clear email
        self.email_entry.delete(
            0,
            "end"
        )

        # Clear search box
        self.search_entry.delete(
            0,
            "end"
        )

        # Remove selected customer ID
        self.selected_id = None

        # Remove table selection
        for item in self.table.selection():

            self.table.selection_remove(item)

    # =====================================================
    # Back to Dashboard
    # =====================================================

    def back_to_dashboard(self):

        # Close customer window
        self.frame.destroy()

        # Import dashboard window
        from gui.dashboard import DashboardWindow

        # Open dashboard
        DashboardWindow(self.app)

