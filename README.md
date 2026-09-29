# Kiosk-Project
A Python-based Kiosk Manager that helps small businesses manage inventory, process sales, search products, generate sales reports, and save inventory and sales data using text files.
# 🛒 Kiosk Manager

## 📌 Project Overview

**Kiosk Manager** is a beginner-friendly Python application designed to help small kiosk businesses manage their daily inventory and sales.

The system allows a kiosk owner to view and update stock, process customer sales, search for products, and generate a sales report. It also uses file handling to save inventory and sales information so that important data is not lost when the program closes.

## ✨ Features

* 👤 **Kiosk Setup**

  * Enter the kiosk owner's name and kiosk name.
  * Displays a formatted welcome message.

* 📦 **Inventory Management**

  * View all available products, prices, and quantities.
  * Restock existing products.
  * Add new products to the inventory.

* 🛍️ **Product Sales**

  * Select a product and quantity to sell.
  * Checks whether enough stock is available.
  * Automatically reduces stock after a successful sale.
  * Calculates the total price.
  * Records each sale.

* 📊 **Sales Report**

  * Displays all sales made during the current session.
  * Calculates total revenue.
  * Shows the number of unique products sold.
  * Identifies the best-selling product.

* 🔎 **Product Search**

  * Search for products using part of their name.
  * Search is case-insensitive.
  * Displays matching products, prices, and quantities.

* 💾 **File Storage**

  * Saves the current inventory to `inventory.txt`.
  * Loads saved inventory when the program starts.
  * Saves sales to `sales.txt` without overwriting previous sales history.

* ✅ **Input Validation**

  * Checks that menu choices are numbers.
  * Handles invalid menu choices without crashing the program.

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* Lists
* Tuples
* Sets
* Functions
* Loops
* Conditional statements
* String methods
* F-strings
* File handling
* Basic input validation

## 📂 Project Structure

```text
Kiosk-Manager/
│
├── Kiosk.py
├── inventory.txt
├── sales.txt
└── README.md
```

> `inventory.txt` and `sales.txt` are created automatically when the program saves data.

## ▶️ How to Run

1. Make sure **Python 3** is installed on your computer.
2. Clone or download this repository.
3. Open the project folder in your terminal or VS Code.
4. Run:

```bash
python Kiosk.py
```

5. Enter the kiosk and owner's names.
6. Use the menu to manage inventory and sales.

## 📋 Main Menu

```text
1) View Stock
2) Add/Restock a Product
3) Sell a Product
4) View Sales Report
5) Search Products
6) Exit
```

## 💡 Example

A user can:

```text
View Stock
     ↓
Restock Bread
     ↓
Sell 3 Bread
     ↓
Generate Sales Report
     ↓
Exit
     ↓
Inventory & Sales Saved
```

When the program is opened again, the saved inventory is loaded automatically.

## 🎯 Learning Objectives

This project was created to apply Python programming concepts in a practical business scenario. It demonstrates how basic programming structures can be combined to create a functional inventory and sales management system.

The project particularly focuses on understanding **functions, data structures, loops, conditionals, input validation, and file handling**.

## 👩‍💻 Author

**Nelly Gitonga**

This project was developed as part of a Python learning and capstone project.
