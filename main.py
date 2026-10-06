
import customtkinter as ctk

from database import initialize_database
from gui.login import LoginWindow



# Initialize Database FIRST
# ==========================================
# This starts the database before the program runs.
# The system needs the database to save and get data.

initialize_database()



# CustomTkinter Settings
# ==========================================
# This makes the program follow the computer's
# light or dark mode.

ctk.set_appearance_mode("System")

# This sets the blue color style for the GUI.

ctk.set_default_color_theme("blue")


# Create Main Application
# ==========================================
# This creates the main window of the program.

app = ctk.CTk()

# This sets the name shown on the window.

app.title("Smart Inventory & Sales Management System")

# This sets the width and height of the window.

app.geometry("1000x600")

# This stops the user from changing the window size.

app.resizable(False, False)

# Open Login Window
# ==========================================
# This opens the login page when the program starts.
# The main window is passed to the LoginWindow class.

LoginWindow(app)

# Start Application
# ==========================================
# mainloop keeps the program running.
# It also allows the program to respond to
# buttons, mouse clicks, and keyboard actions.

app.mainloop()

