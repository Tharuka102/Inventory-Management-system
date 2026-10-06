import customtkinter as ctk 
from tkinter import ttk, messagebox 

from models.report import ReportModel 


class ReportsWindow: 

    def __init__(self, app): 

        self.app = app 
        self.report_model = ReportModel() 

        # Store the selected sale ID 
        self.selected_sale_id = None 

        # ========================= 
        # Main Scrollable Frame (Fixes UI clipping)
        # ========================= 

        self.frame = ctk.CTkScrollableFrame( 
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
            text="Reports & Sales History", 
            font=ctk.CTkFont( 
                size=26, 
                weight="bold" 
            ) 
        ) 

        title.pack( 
            pady=(15, 5) 
        ) 

        # Show a short description 
        subtitle = ctk.CTkLabel( 
            self.frame, 
            text="View sales, invoices and profit information" 
        ) 

        subtitle.pack( 
            pady=(0, 10) 
        ) 

        # ========================= 
        # Summary Frame 
        # ========================= 

        summary_frame = ctk.CTkFrame( 
            self.frame 
        ) 

        summary_frame.pack( 
            padx=20, 
            pady=5, 
            fill="x" 
        ) 

        # Show total sales 
        self.sales_card = self.create_summary_card( 
            summary_frame, 
            "Total Sales", 
            "Rs. 0.00", 
            0 
        ) 

        # Show total profit 
        self.profit_card = self.create_summary_card( 
            summary_frame, 
            "Total Profit", 
            "Rs. 0.00", 
            1 
        ) 

        # Show total products 
        self.products_card = self.create_summary_card( 
            summary_frame, 
            "Total Products", 
            "0", 
            2 
        ) 

        # Show total customers 
        self.customers_card = self.create_summary_card( 
            summary_frame, 
            "Total Customers", 
            "0", 
            3 
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

        # Search invoice or customer 
        self.search_entry = ctk.CTkEntry( 
            search_frame, 
            width=300, 
            placeholder_text="Search invoice or customer" 
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
            command=self.search_sales 
        ).pack( 
            side="left", 
            padx=5 
        ) 

        # Show all sales 
        ctk.CTkButton( 
            search_frame, 
            text="Show All", 
            width=100, 
            command=self.load_sales 
        ).pack( 
            side="left", 
            padx=5 
        ) 

        # ========================= 
        # Sales Table Frame 
        # ========================= 

        sales_frame = ctk.CTkFrame( 
            self.frame 
        ) 

        sales_frame.pack( 
            padx=20, 
            pady=5, 
            fill="x", 
            expand=False 
        ) 

        # ========================= 
        # Sales Table 
        # ========================= 

        columns = ( 
            "ID", 
            "Invoice", 
            "Customer", 
            "Subtotal", 
            "Discount", 
            "Total", 
            "Payment", 
            "Balance", 
            "Date" 
        ) 

        # Create sales table with constrained height
        self.sales_table = ttk.Treeview( 
            sales_frame, 
            columns=columns, 
            show="headings",
            height=6
        ) 

        # Add table headings 
        for column in columns: 

            self.sales_table.heading( 
                column, 
                text=column 
            ) 

        # Set ID column width 
        self.sales_table.column( 
            "ID", 
            width=50, 
            anchor="center" 
        ) 

        # Set invoice column width 
        self.sales_table.column( 
            "Invoice", 
            width=110, 
            anchor="center" 
        ) 

        # Set customer column width 
        self.sales_table.column( 
            "Customer", 
            width=150 
        ) 

        # Set subtotal column width 
        self.sales_table.column( 
            "Subtotal", 
            width=100, 
            anchor="center" 
        ) 

        # Set discount column width 
        self.sales_table.column( 
            "Discount", 
            width=90, 
            anchor="center" 
        ) 

        # Set total column width 
        self.sales_table.column( 
            "Total", 
            width=100, 
            anchor="center" 
        ) 

        # Set payment column width 
        self.sales_table.column( 
            "Payment", 
            width=100, 
            anchor="center" 
        ) 

        # Set balance column width 
        self.sales_table.column( 
            "Balance", 
            width=100, 
            anchor="center" 
        ) 

        # Set date column width 
        self.sales_table.column( 
            "Date", 
            width=150, 
            anchor="center" 
        ) 

        # Show sales table 
        self.sales_table.pack( 
            side="left", 
            fill="both", 
            expand=True 
        ) 

        # Create vertical scrollbar 
        scrollbar = ttk.Scrollbar( 
            sales_frame, 
            orient="vertical", 
            command=self.sales_table.yview 
        ) 

        scrollbar.pack( 
            side="right", 
            fill="y" 
        ) 

        # Connect scrollbar with table 
        self.sales_table.configure( 
            yscrollcommand=scrollbar.set 
        ) 

        # ========================= 
        # Select Sale 
        # ========================= 

        # Detect when a sale is selected 
        self.sales_table.bind( 
            "<ButtonRelease-1>", 
            self.select_sale 
        ) 

        # ========================= 
        # Sale Details Frame 
        # ========================= 

        details_frame = ctk.CTkFrame( 
            self.frame 
        ) 

        details_frame.pack( 
            padx=20, 
            pady=5, 
            fill="x" 
        ) 

        # Details section title 
        details_title = ctk.CTkLabel( 
            details_frame, 
            text="Selected Invoice Details", 
            font=ctk.CTkFont( 
                size=16, 
                weight="bold" 
            ) 
        ) 

        details_title.pack( 
            pady=5 
        ) 

        # ========================= 
        # Items Table 
        # ========================= 

        item_columns = ( 
            "Product", 
            "Quantity", 
            "Unit Price", 
            "Cost Price", 
            "Total" 
        ) 

        # Create items table 
        self.items_table = ttk.Treeview( 
            details_frame, 
            columns=item_columns, 
            show="headings", 
            height=4 
        ) 

        # Add item table headings 
        for column in item_columns: 

            self.items_table.heading( 
                column, 
                text=column 
            ) 

        # Set product column width 
        self.items_table.column( 
            "Product", 
            width=220 
        ) 

        # Set quantity column width 
        self.items_table.column( 
            "Quantity", 
            width=100, 
            anchor="center" 
        ) 

        # Set unit price column width 
        self.items_table.column( 
            "Unit Price", 
            width=120, 
            anchor="center" 
        ) 

        # Set cost price column width 
        self.items_table.column( 
            "Cost Price", 
            width=120, 
            anchor="center" 
        ) 

        # Set total column width 
        self.items_table.column( 
            "Total", 
            width=120, 
            anchor="center" 
        ) 

        # Show items table 
        self.items_table.pack( 
            padx=10, 
            pady=5, 
            fill="x" 
        ) 

        # ========================= 
        # Profit Label 
        # ========================= 

        # Show profit of selected sale 
        self.sale_profit_label = ctk.CTkLabel( 
            details_frame, 
            text="Sale Profit: Rs. 0.00", 
            font=ctk.CTkFont( 
                size=14, 
                weight="bold" 
            ) 
        ) 

        self.sale_profit_label.pack( 
            pady=5 
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
            pady=(10, 20) 
        ) 

        # ========================= 
        # Load Data 
        # ========================= 

        # Load summary and sales data 
        self.load_summary() 
        self.load_sales() 

    # ===================================================== 
    # Create Summary Card 
    # ===================================================== 

    def create_summary_card( 
        self, 
        parent, 
        title, 
        value, 
        column 
    ): 

        # Create a card frame 
        card = ctk.CTkFrame( 
            parent, 
            width=220, 
            height=80 
        ) 

        card.grid( 
            row=0, 
            column=column, 
            padx=10, 
            pady=10, 
            sticky="ew" 
        ) 

        # Make the card fill the column 
        parent.grid_columnconfigure( 
            column, 
            weight=1 
        ) 

        # Add card title 
        title_label = ctk.CTkLabel( 
            card, 
            text=title 
        ) 

        title_label.pack( 
            pady=(10, 2) 
        ) 

        # Add card value 
        value_label = ctk.CTkLabel( 
            card, 
            text=value, 
            font=ctk.CTkFont( 
                size=18, 
                weight="bold" 
            ) 
        ) 

        value_label.pack( 
            pady=(0, 10) 
        ) 

        # Return the value label 
        return value_label 

    # ===================================================== 
    # Load Summary 
    # ===================================================== 

    def load_summary(self): 

        try: 

            # Get total sales 
            total_sales = ( 
                self.report_model.get_total_sales() 
            ) 

            # Get total profit 
            total_profit = ( 
                self.report_model.get_total_profit() 
            ) 

            # Get total products 
            total_products = ( 
                self.report_model.get_total_products() 
            ) 

            # Get total customers 
            total_customers = ( 
                self.report_model.get_total_customers() 
            ) 

            # Display total sales in Rs. 
            self.sales_card.configure( 
                text=f"Rs. {total_sales:.2f}" 
            ) 

            # Display total profit in Rs. 
            self.profit_card.configure( 
                text=f"Rs. {total_profit:.2f}" 
            ) 

            # Display product count 
            self.products_card.configure( 
                text=str(total_products) 
            ) 

            # Display customer count 
            self.customers_card.configure( 
                text=str(total_customers) 
            ) 

        except Exception as error: 

            # Show error if summary cannot be loaded 
            messagebox.showerror( 
                "Error", 
                f"Failed to load summary.\n\n{error}" 
            ) 

    # ===================================================== 
    # Load Sales 
    # ===================================================== 

    def load_sales(self): 

        try: 

            # Get all sales from the database 
            sales = self.report_model.get_sales_report() 

            # Clear old table data 
            self.sales_table.delete( 
                *self.sales_table.get_children() 
            ) 

            # Add each sale to the table 
            for sale in sales: 

                sale_id = sale[0] 
                invoice = sale[1] 
                customer = sale[2] 

                # Convert money values to numbers 
                subtotal = float(sale[3]) 
                discount = float(sale[4]) 
                total = float(sale[5]) 
                payment = float(sale[6]) 
                balance = float(sale[7]) 

                sale_date = sale[8] 

                # Insert sale data into table 
                self.sales_table.insert( 
                    "", 
                    "end", 
                    values=( 
                        sale_id, 
                        invoice, 
                        customer, 
                        f"Rs. {subtotal:.2f}", 
                        f"Rs. {discount:.2f}", 
                        f"Rs. {total:.2f}", 
                        f"Rs. {payment:.2f}", 
                        f"Rs. {balance:.2f}", 
                        sale_date 
                    ) 
                ) 

        except Exception as error: 

            # Show error if sales cannot be loaded 
            messagebox.showerror( 
                "Error", 
                f"Failed to load sales.\n\n{error}" 
            ) 

    # ===================================================== 
    # Search Sales 
    # ===================================================== 

    def search_sales(self): 

        # Get search text 
        search_text = ( 
            self.search_entry.get().strip() 
        ) 

        # If search box is empty, show all sales 
        if not search_text: 

            self.load_sales() 
            return 

        try: 

            # Search sales using the entered text 
            sales = ( 
                self.report_model.search_sales_report( 
                    search_text 
                ) 
            ) 

            # Clear old search results 
            self.sales_table.delete( 
                *self.sales_table.get_children() 
            ) 

            # Add search results to the table 
            for sale in sales: 

                sale_id = sale[0] 
                invoice = sale[1] 
                customer = sale[2] 

                subtotal = float(sale[3]) 
                discount = float(sale[4]) 
                total = float(sale[5]) 
                payment = float(sale[6]) 
                balance = float(sale[7]) 

                sale_date = sale[8] 

                # Insert search result into table 
                self.sales_table.insert( 
                    "", 
                    "end", 
                    values=( 
                        sale_id, 
                        invoice, 
                        customer, 
                        f"Rs. {subtotal:.2f}", 
                        f"Rs. {discount:.2f}", 
                        f"Rs. {total:.2f}", 
                        f"Rs. {payment:.2f}", 
                        f"Rs. {balance:.2f}", 
                        sale_date 
                    ) 
                ) 

        except Exception as error: 

            # Show error if search fails 
            messagebox.showerror( 
                "Error", 
                f"Search failed.\n\n{error}" 
            ) 

    # ===================================================== 
    # Select Sale 
    # ===================================================== 

    def select_sale(self, event): 

        # Get selected row 
        selected = self.sales_table.selection() 

        # Stop if no row is selected 
        if not selected: 
            return 

        # Get values from selected row 
        values = self.sales_table.item( 
            selected[0], 
            "values" 
        ) 

        # Store selected sale ID 
        self.selected_sale_id = int( 
            values[0] 
        ) 

        # Load details of selected sale 
        self.load_sale_details( 
            self.selected_sale_id 
        ) 

    # ===================================================== 
    # Load Sale Details 
    # ===================================================== 

    def load_sale_details(self, sale_id): 

        try: 

            # Get items for selected sale 
            items = ( 
                self.report_model.get_sale_items( 
                    sale_id 
                ) 
            ) 

            # Clear old item details 
            self.items_table.delete( 
                *self.items_table.get_children() 
            ) 

            # Add each product to the items table 
            for item in items: 

                product_name = item[0] 
                quantity = item[1] 

                # Convert money values to numbers 
                unit_price = float(item[2]) 
                cost_price = float(item[3]) 
                total = float(item[4]) 

                # Insert product details 
                self.items_table.insert( 
                    "", 
                    "end", 
                    values=( 
                        product_name, 
                        quantity, 
                        f"Rs. {unit_price:.2f}", 
                        f"Rs. {cost_price:.2f}", 
                        f"Rs. {total:.2f}" 
                    ) 
                ) 

            # Calculate profit for selected sale 
            profit = ( 
                self.report_model.get_sale_profit( 
                    sale_id 
                ) 
            ) 

            # Show sale profit in Rs. 
            self.sale_profit_label.configure( 
                text=f"Sale Profit: Rs. {profit:.2f}" 
            ) 

        except Exception as error: 

            # Show error if invoice details cannot be loaded 
            messagebox.showerror( 
                "Error", 
                f"Failed to load invoice details.\n\n{error}" 
            ) 

    # ===================================================== 
    # Back To Dashboard 
    # ===================================================== 

    def back_to_dashboard(self): 

        # Close the reports window 
        self.frame.destroy() 

        # Import dashboard window 
        from gui.dashboard import DashboardWindow 

        # Open dashboard 
        DashboardWindow( 
            self.app 
        )