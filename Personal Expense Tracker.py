import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# 1. Initialize CSV file if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
        print("✅ Expense file created!")

# 2. Add an expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

# 3. Show all expenses
def show_expenses():
    try:
        df = pd.read_csv(FILE_NAME)
        if df.empty:
            print("❌ No expenses recorded yet.")
            return
        print("\n📄 All Expenses:")
        print(df)
    except FileNotFoundError:
        print("❌ No expense file found. Add an expense first.")

# 4. Show monthly summary with chart
def monthly_summary():
    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty or len(df) == 0:
            print("❌ No data found. Add some expenses first.")
            return

        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        df = df.dropna(subset=["Date", "Amount"])

        # Ensure Amount column is numeric
        df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce')
        df = df.dropna(subset=["Amount"])

        if df.empty:
            print("❌ No valid data to summarize.")
            return

        df["Month"] = df["Date"].dt.strftime("%Y-%m")

        summary = df.groupby("Month")["Amount"].sum()
        print("\n📊 Monthly Summary:")
        print(summary)

        # Plot
        summary.plot(kind="bar", color="skyblue")
        plt.title("Monthly Expense Summary")
        plt.xlabel("Month")
        plt.ylabel("Total Amount")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("❌ No data found. Add some expenses first.")

# 5. Menu system
def menu():
    initialize_file()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
