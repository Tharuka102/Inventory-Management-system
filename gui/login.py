import customtkinter as ctk
from tkinter import messagebox

from database import get_connection


class LoginWindow:

    def __init__(self, app):

        self.app = app

        # Main Frame
        self.frame = ctk.CTkFrame(
            app,
            fg_color="transparent"
        )

        self.frame.pack(
            expand=True
        )

        # Welcome Text
        welcome = ctk.CTkLabel(
            self.frame,
            text="Welcome Back!",
            font=("Arial", 32, "bold")
        )

        welcome.pack(
            pady=(40, 5)
        )

        system_name = ctk.CTkLabel(
            self.frame,
            text="Smart Inventory & Sales Management System",
            font=("Arial", 15)
        )

        system_name.pack(
            pady=(0, 10)
        )

        subtitle = ctk.CTkLabel(
            self.frame,
            text="Please login to continue",
            font=("Arial", 14)
        )

        subtitle.pack(
            pady=(0, 30)
        )

        # Username
        username_label = ctk.CTkLabel(
            self.frame,
            text="Username",
            font=("Arial", 14, "bold")
        )

        username_label.pack(
            anchor="w",
            padx=50
        )

        self.username = ctk.CTkEntry(
            self.frame,
            width=350,
            height=45,
            placeholder_text="Enter username"
        )

        self.username.pack(
            pady=(5, 15)
        )

        # Password
        password_label = ctk.CTkLabel(
            self.frame,
            text="Password",
            font=("Arial", 14, "bold")
        )

        password_label.pack(
            anchor="w",
            padx=50
        )

        self.password = ctk.CTkEntry(
            self.frame,
            width=350,
            height=45,
            placeholder_text="Enter your password",
            show="*"
        )

        self.password.pack(
            pady=(5, 25)
        )

        # Login Button
        login_button = ctk.CTkButton(
            self.frame,
            text="Login",
            width=350,
            height=45,
            font=("Arial", 16, "bold"),
            command=self.login
        )

        login_button.pack(
            pady=(0, 30)
        )

        # Error Message
        self.error_label = ctk.CTkLabel(
            self.frame,
            text="",
            font=("Arial", 13)
        )

        self.error_label.pack(
            pady=5
        )

        # Project Watermark
        watermark = ctk.CTkLabel(
            self.frame,
            text="Smart Inventory & Sales Management System\n"
                 "Tharuka Madusanka | ID: CIT-26-01-0568",
            font=("Arial", 10),
            text_color="gray"
        )

        watermark.pack(
            pady=(5, 10)
        )

        # Footer
        footer = ctk.CTkLabel(
            self.frame,
            text="© 2026 Smart Inventory System",
            font=("Arial", 11)
        )

        footer.pack(
            pady=(0, 25)
        )

    # Login Function
    def login(self):

        username = self.username.get().strip()
        password = self.password.get()

        # Check empty fields
        if username == "" or password == "":

            self.error_label.configure(
                text="Please enter username and password."
            )

            return

        connection = None
        cursor = None

        try:

            # Connect to MySQL
            connection = get_connection()

            cursor = connection.cursor()

            # Check user
            query = """
                SELECT id, username
                FROM users
                WHERE username = %s
                AND password = %s
            """

            cursor.execute(
                query,
                (username, password)
            )

            user = cursor.fetchone()

            # Login Success
            if user:

                self.open_dashboard()

            # Login Failed
            else:

                self.error_label.configure(
                    text="Invalid username or password."
                )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                f"Could not connect to database.\n\n{error}"
            )

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    # Open Dashboard
    def open_dashboard(self):

        self.frame.destroy()

        from gui.dashboard import DashboardWindow

        DashboardWindow(self.app)