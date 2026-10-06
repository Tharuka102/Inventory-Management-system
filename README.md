# Smart Inventory & Sales Management System

A desktop-based **Inventory and Sales Management System** developed using **Python, CustomTkinter, and MySQL**.

The system provides a centralized platform for managing products, customers, suppliers, sales transactions, stock levels, and business reports.

---

## 📌 Project Overview

The **Smart Inventory & Sales Management System** was developed as a Python desktop application to simplify inventory and sales management for small and medium-sized businesses.

The application combines inventory management and sales processing into one system. It uses a **MySQL relational database** to store business information and provides a modern graphical interface using **CustomTkinter**.

The project follows a modular structure where the GUI and database logic are separated into different files and classes.

---

## ✨ Features

### 🔐 Login
- User authentication
- Basic application access control

### 📊 Dashboard
- View total products
- View total suppliers
- View total customers
- View total sales
- Central navigation to system modules

### 👥 Customer Management
- Add customers
- Search customers
- Update customer information
- Delete customer records
- Store customer name, phone number and email

### 🚚 Supplier Management
- Add suppliers
- Manage supplied products
- Store supplier contact details
- Track supplied item quantities
- Maintain supplier-product relationships

### 📦 Product Management
- Add products
- Update product information
- Search products
- Manage stock quantity
- Manage cost price
- Manage selling price

### 🛒 Sales Management
- Select customers or process walk-in sales
- Add multiple products to a shopping cart
- Validate available stock
- Automatically generate invoice numbers
- Calculate subtotal
- Apply discounts
- Calculate grand total
- Record payment
- Calculate balance
- Automatically reduce stock after a successful sale

### 📈 Reports
- View sales records
- Search sales
- View invoice numbers
- View customer information
- View subtotal, discount, total, payment and balance
- Calculate basic profit information

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **CustomTkinter** | Modern desktop GUI |
| **MySQL** | Relational database |
| **mysql-connector-python** | Python–MySQL connection |
| **Tkinter ttk** | Table/Treeview presentation |
| **Visual Studio Code** | Development environment |
| **Object-Oriented Programming** | Application structure |

These technologies are based on the technologies documented in the project report.

---

## 🏗️ Project Architecture

The project separates the graphical interface from database operations.

```text
User
  │
  ▼
GUI / CustomTkinter
  │
  ▼
Model Classes
  │
  ▼
MySQL Database
```

The GUI handles user interaction, while model classes handle database operations such as adding, searching, updating and deleting records.

---

## 📁 Project Structure

```text
Smart-Inventory-Sales-Management-System/
│
├── main.py
├── database.py
│
├── models/
│   ├── customer.py
│   ├── supplier.py
│   ├── product.py
│   ├── sales.py
│   ├── report.py
│   └── dashboard.py
│
├── gui/
│   ├── login.py
│   ├── dashboard.py
│   ├── customers.py
│   ├── suppliers.py
│   ├── products.py
│   ├── sales.py
│   └── reports.py
│
└── README.md
```

The structure above follows the project structure documented in the report.

---

## 🗄️ Database

The application uses **MySQL** for persistent data storage.

The database contains seven main tables:

```text
users
customers
suppliers
products
supplier_products
sales
sale_items
```

### Database Relationships

```text
Customers
    │
    └── Sales
          │
          └── Sale Items
                 │
                 └── Products

Suppliers
    │
    └── Supplier Products
                 │
                 └── Products
```

A customer can have multiple sales, a sale can contain multiple sale items, and each sale item is connected to a product.

---

## 🔄 System Flow

```text
Start Application
       │
       ▼
Initialize Database
       │
       ▼
     Login
       │
       ▼
   Dashboard
       │
       ▼
Select Module
       │
       ▼
Perform Operation
       │
       ▼
Save / Read Data
       │
       ▼
      MySQL
       │
       ▼
Display Updated Information
```

---

## 🛒 Sales Process

The sales module is one of the main parts of the system.

```text
Select Customer
       │
       ▼
Select Product
       │
       ▼
Enter Quantity
       │
       ▼
Add Product to Cart
       │
       ▼
Calculate Total
       │
       ▼
Validate Stock
       │
       ▼
Enter Payment
       │
       ▼
Save Sale
       │
       ▼
Reduce Product Stock
       │
       ▼
Generate Sale Record
```

The system checks stock availability before saving the transaction. After a successful sale, the product quantity is automatically reduced.

---

## 💰 Sales Calculations

The system supports:

- Subtotal calculation
- Discount calculation
- Grand total calculation
- Payment validation
- Balance calculation
- Profit calculation

Basic profit is calculated using the difference between the selling price and cost price multiplied by the quantity sold.

---

## 🧠 Python Concepts Used

This project demonstrates several important Python programming concepts:

- Variables and data types
- Functions and methods
- Classes and objects
- Object-Oriented Programming
- Lists
- Dictionaries
- Conditional statements
- Loops
- Exception handling
- Type casting
- Database connectivity
- GUI event handling

For example, the sales cart uses dictionaries to store product information such as:

```python
{
    "product_id": 1,
    "product_name": "Product Name",
    "quantity": 2,
    "unit_price": 500.00,
    "cost_price": 400.00,
    "total": 1000.00
}
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-Inventory-Sales-Management-System.git
```

### 2. Open the Project

```bash
cd Smart-Inventory-Sales-Management-System
```

### 3. Install Required Packages

```bash
pip install customtkinter mysql-connector-python
```

If a `requirements.txt` file is available in the repository, you can instead use:

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Make sure MySQL Server is installed and running.

Create/configure the database used by the application:

```text
Database: smart_inventory
Host: localhost
Port: 3306
```

The application's database module handles database initialization and table creation.

### 5. Run the Application

```bash
python main.py
```

---

## 🧪 Testing

The application was tested for major system functions, including:

| Test | Expected Result | Status |
|---|---|---|
| Login with valid credentials | Dashboard opens | ✅ Pass |
| Add customer | Customer stored and displayed | ✅ Pass |
| Search customer | Matching customer displayed | ✅ Pass |
| Update customer | Customer information updated | ✅ Pass |
| Delete customer | Customer removed | ✅ Pass |
| Add product | Product stored | ✅ Pass |
| Search product | Matching products displayed | ✅ Pass |
| Add supplier | Supplier information stored | ✅ Pass |
| Add product to cart | Product appears in cart | ✅ Pass |
| Quantity greater than stock | Transaction rejected | ✅ Pass |
| Payment less than total | Sale rejected | ✅ Pass |
| Save valid sale | Sale stored successfully | ✅ Pass |
| After sale | Stock quantity reduced | ✅ Pass |
| Search sales report | Matching sales displayed | ✅ Pass |

The project report records these functional tests as passing.

---

## 🚀 Future Improvements

Possible future improvements include:

- 👤 Role-based user accounts
- 🔐 Password hashing and stronger authentication
- 🧾 Automatic PDF invoice generation
- 🖨️ Invoice printing
- 📷 Barcode scanner support
- ⚠️ Low-stock alerts
- 📊 Daily, monthly and yearly sales charts
- 📈 Advanced inventory and profit analytics
- 💾 Database backup and restore
- 📤 Excel/PDF report export
- ☁️ Cloud database support
- 👥 Multi-user access
- 📝 Audit logs
- 📱 Responsive interface improvements

These improvements are identified in the project report as possible future development directions.

---

## 🎯 Project Objectives

The main objectives of this project are to:

1. Develop a practical desktop application using Python and CustomTkinter.
2. Store business information in a structured MySQL database.
3. Manage customer, supplier and product records.
4. Process sales transactions and automatically update stock.
5. Generate invoices and calculate sales totals.
6. Provide sales reports and basic business statistics.
7. Demonstrate practical Python and Object-Oriented Programming concepts.

---

## 👨‍💻 Author

**S.G.T.M Samaraweera**

**Student ID:** CIT-26-01-0568

**Programme:** Bachelor of Science Honours in Software Engineering

**Institution:** Sri Lanka Technology Campus (SLTC)

---

## 📄 Project Type

**Academic / Educational Project**

This project was developed as a Python Tkinter-based desktop application for inventory and sales management.

---

## ⭐ Conclusion

The Smart Inventory & Sales Management System provides a centralized solution for managing products, suppliers, customers and sales transactions.

By combining **Python, CustomTkinter and MySQL**, the project demonstrates how a desktop application can be connected to a relational database while applying practical programming concepts such as Object-Oriented Programming, functions, lists, dictionaries, loops, conditional statements, exception handling and database connectivity.

---

⭐ **If you find this project useful, consider giving the repository a star!**
