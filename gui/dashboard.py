
import customtkinter as ctk

from models.dashboard import DashboardModel


class DashboardWindow:

    def __init__(self, app):

        self.app = app

        # Create dashboard model
        self.dashboard_model = DashboardModel()

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
        # Sidebar
        # =========================

        self.sidebar = ctk.CTkFrame(
            self.frame,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # =========================
        # System Title
        # =========================

        title = ctk.CTkLabel(
            self.sidebar,
            text="INVENTORY\nSYSTEM",
            font=("Arial", 22, "bold")
        )

        title.pack(
            pady=(40, 45)
        )

        # =========================
        # Sidebar Buttons
        # =========================

        self.create_sidebar_button("Dashboard")
        self.create_sidebar_button("Suppliers")
        self.create_sidebar_button("Customers")
        self.create_sidebar_button("Products")
        self.create_sidebar_button("Sales")
        self.create_sidebar_button("Reports")

        # =========================
        # Logout Button
        # =========================

        logout_button = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            width=180,
            height=40,
            corner_radius=8,
            fg_color="#C0392B",
            hover_color="#A93226",
            command=self.logout
        )

        logout_button.pack(
            side="bottom",
            padx=20,
            pady=30
        )

        # =========================
        # Content Area
        # =========================

        self.content = ctk.CTkFrame(
            self.frame,
            corner_radius=0
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =========================
        # Header
        # =========================

        heading = ctk.CTkLabel(
            self.content,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )

        heading.pack(
            anchor="w",
            padx=35,
            pady=(30, 5)
        )

        welcome = ctk.CTkLabel(
            self.content,
            text="Welcome back! Here's your inventory overview.",
            font=("Arial", 15)
        )

        welcome.pack(
            anchor="w",
            padx=35,
            pady=(0, 20)
        )

        # =========================
        # Summary Cards
        # =========================

        cards_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        cards_frame.pack(
            fill="x",
            padx=35
        )

        # Give equal space to all cards
        for column in range(4):

            cards_frame.grid_columnconfigure(
                column,
                weight=1
            )

        # Product count
        self.product_value = self.create_card(
            cards_frame,
            "Total Products",
            "0",
            0
        )

        # Supplier count
        self.supplier_value = self.create_card(
            cards_frame,
            "Total Suppliers",
            "0",
            1
        )

        # Customer count
        self.customer_value = self.create_card(
            cards_frame,
            "Total Customers",
            "0",
            2
        )

        # Total sales amount
        self.sales_value = self.create_card(
            cards_frame,
            "Total Sales",
            "Rs. 0.00",
            3
        )

        # =========================
        # Bottom Section
        # =========================

        bottom_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        bottom_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(20, 25)
        )

        # =========================
        # Top Customers
        # =========================

        customer_frame = ctk.CTkFrame(
            bottom_frame,
            corner_radius=12
        )

        customer_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        customer_title = ctk.CTkLabel(
            customer_frame,
            text="Top Customers",
            font=("Arial", 20, "bold")
        )

        customer_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        customer_subtitle = ctk.CTkLabel(
            customer_frame,
            text="Customers with highest purchases",
            font=("Arial", 12)
        )

        customer_subtitle.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # Store customer rows
        self.customer_rows = []

        for _ in range(3):

            row = self.create_customer_row(
                customer_frame,
                "No customer data",
                "0 purchases"
            )

            self.customer_rows.append(row)

        # =========================
        # Top Suppliers
        # =========================

        supplier_frame = ctk.CTkFrame(
            bottom_frame,
            corner_radius=12
        )

        supplier_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        supplier_title = ctk.CTkLabel(
            supplier_frame,
            text="Top Suppliers",
            font=("Arial", 20, "bold")
        )

        supplier_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        supplier_subtitle = ctk.CTkLabel(
            supplier_frame,
            text="Suppliers providing most stock",
            font=("Arial", 12)
        )

        supplier_subtitle.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # Store supplier rows
        self.supplier_rows = []

        for _ in range(3):

            row = self.create_supplier_row(
                supplier_frame,
                "No supplier data",
                "0 items"
            )

            self.supplier_rows.append(row)

        # Load data from database
        self.load_dashboard_data()

    # =====================================================
    # Sidebar Buttons
    # =====================================================

    def create_sidebar_button(self, text):

        # Select the correct function for each button
        if text == "Dashboard":
            command = self.open_dashboard

        elif text == "Suppliers":
            command = self.open_suppliers

        elif text == "Customers":
            command = self.open_customers

        elif text == "Products":
            command = self.open_products

        elif text == "Sales":
            command = self.open_sales

        elif text == "Reports":
            command = self.open_reports

        else:
            command = None

        # Create sidebar button
        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            width=180,
            height=42,
            corner_radius=8,
            command=command
        )

        button.pack(
            padx=20,
            pady=7
        )

    # =====================================================
    # Dashboard
    # =====================================================

    def open_dashboard(self):

        # Dashboard is already open
        pass

    # =====================================================
    # Suppliers
    # =====================================================

    def open_suppliers(self):

        self.frame.destroy()

        from gui.suppliers import SuppliersWindow

        SuppliersWindow(
            self.app
        )

    # =====================================================
    # Customers
    # =====================================================

    def open_customers(self):

        self.frame.destroy()

        from gui.customers import CustomersWindow

        CustomersWindow(
            self.app
        )

    # =====================================================
    # Products
    # =====================================================

    def open_products(self):

        self.frame.destroy()

        from gui.products import ProductsWindow

        ProductsWindow(
            self.app
        )

    # =====================================================
    # Sales
    # =====================================================

    def open_sales(self):

        self.frame.destroy()

        from gui.sales import SalesWindow

        SalesWindow(
            self.app
        )

    # =====================================================
    # Reports
    # =====================================================

    def open_reports(self):

        self.frame.destroy()

        from gui.reports import ReportsWindow

        ReportsWindow(
            self.app
        )

    # =====================================================
    # Load Dashboard Data
    # =====================================================

    def load_dashboard_data(self):

        try:

            # Get summary information
            total_products = (
                self.dashboard_model
                .get_total_products()
            )

            total_suppliers = (
                self.dashboard_model
                .get_total_suppliers()
            )

            total_customers = (
                self.dashboard_model
                .get_total_customers()
            )

            total_sales = (
                self.dashboard_model
                .get_total_sales()
            )

            # Update summary cards
            self.product_value.configure(
                text=str(total_products)
            )

            self.supplier_value.configure(
                text=str(total_suppliers)
            )

            self.customer_value.configure(
                text=str(total_customers)
            )

            # Display sales amount with Rs.
            self.sales_value.configure(
                text=f"Rs. {total_sales:.2f}"
            )

            # ---------------------------------------------
            # Top Customers
            # ---------------------------------------------

            top_customers = (
                self.dashboard_model
                .get_top_customers()
            )

            # Update customer rows
            for index, row in enumerate(
                self.customer_rows
            ):

                if index < len(top_customers):

                    name = top_customers[index][0]

                    purchase_count = (
                        top_customers[index][1]
                    )

                    total_purchase = float(
                        top_customers[index][2]
                    )

                    self.update_customer_row(
                        row,
                        name,
                        f"{purchase_count} sales | "
                        f"Rs. {total_purchase:.2f}"
                    )

                else:

                    self.update_customer_row(
                        row,
                        "No customer data",
                        "0 purchases"
                    )

            # ---------------------------------------------
            # Top Suppliers
            # ---------------------------------------------

            top_suppliers = (
                self.dashboard_model
                .get_top_suppliers()
            )

            # Update supplier rows
            for index, row in enumerate(
                self.supplier_rows
            ):

                if index < len(top_suppliers):

                    name = top_suppliers[index][0]
                    total_items = top_suppliers[index][1]

                    self.update_supplier_row(
                        row,
                        name,
                        f"{total_items} items"
                    )

                else:

                    self.update_supplier_row(
                        row,
                        "No supplier data",
                        "0 items"
                    )

        except Exception as error:

            # Show database error in terminal
            print(
                "Dashboard data error:",
                error
            )

    # =====================================================
    # Summary Card
    # =====================================================

    def create_card(
        self,
        parent,
        title,
        value,
        column
    ):

        # Create summary card
        card = ctk.CTkFrame(
            parent,
            corner_radius=12
        )

        card.grid(
            row=0,
            column=column,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        # Card title
        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 13)
        )

        title_label.pack(
            pady=(20, 5)
        )

        # Card value
        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 23, "bold")
        )

        value_label.pack(
            pady=(0, 15)
        )

        return value_label

    # =====================================================
    # Customer Row
    # =====================================================

    def create_customer_row(
        self,
        parent,
        name,
        purchases
    ):

        # Create customer row
        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=6
        )

        # Customer name
        name_label = ctk.CTkLabel(
            row,
            text=name,
            font=("Arial", 14, "bold")
        )

        name_label.pack(
            side="left"
        )

        # Purchase information
        purchase_label = ctk.CTkLabel(
            row,
            text=purchases,
            font=("Arial", 12)
        )

        purchase_label.pack(
            side="right"
        )

        return (
            name_label,
            purchase_label
        )

    # =====================================================
    # Update Customer Row
    # =====================================================

    def update_customer_row(
        self,
        row,
        name,
        purchases
    ):

        # Get labels from the row
        name_label, purchase_label = row

        name_label.configure(
            text=name
        )

        purchase_label.configure(
            text=purchases
        )

    # =====================================================
    # Supplier Row
    # =====================================================

    def create_supplier_row(
        self,
        parent,
        name,
        items
    ):

        # Create supplier row
        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=6
        )

        # Supplier name
        name_label = ctk.CTkLabel(
            row,
            text=name,
            font=("Arial", 14, "bold")
        )

        name_label.pack(
            side="left"
        )

        # Stock information
        item_label = ctk.CTkLabel(
            row,
            text=items,
            font=("Arial", 12)
        )

        item_label.pack(
            side="right"
        )

        return (
            name_label,
            item_label
        )

    # =====================================================
    # Update Supplier Row
    # =====================================================

    def update_supplier_row(
        self,
        row,
        name,
        items
    ):

        # Get labels from the row
        name_label, item_label = row

        name_label.configure(
            text=name
        )

        item_label.configure(
            text=items
        )

    # =====================================================
    # Logout
    # =====================================================

    def logout(self):

        # Remove dashboard
        self.frame.destroy()

        # Open login screen
        from gui.login import LoginWindow

        LoginWindow(
            self.app
        )



