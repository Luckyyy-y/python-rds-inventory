from datetime import datetime
import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG


# This will display all items in the database.
def view_items(database):
    cursor = database.cursor()

    cursor.execute(
        "SELECT itemid, purchasedate, purchaseprice, saleprice FROM item"
    )

    items = cursor.fetchall()

    if len(items) == 0:
        print("\nNo items were found.")
    else:
        print("\nSaved Items")

        for item in items:
            item_id = item[0]
            purchase_date = item[1]
            purchase_price = item[2]
            sale_price = item[3]

            if sale_price is None:
                sale_price = "Not sold"
            else:
                sale_price = f"${sale_price:.2f}"

            print(
                f"ID: {item_id} | "
                f"Date: {purchase_date} | "
                f"Purchase Price: ${purchase_price:.2f} | "
                f"Sale Price: {sale_price}"
            )

    cursor.close()


# This part will add an item to the database.
def add_item(database):
    date_input = input(
        "\nEnter the purchase date (YYYY-MM-DD): "
    )

    purchase_date = datetime.strptime(
        date_input, "%Y-%m-%d"
    ).date()

    purchase_price = float(
        input("Enter the purchase price: $")
    )

    sale_input = input(
        "Enter the sale price or leave it blank: $"
    )

    if sale_input == "":
        sale_price = None
    else:
        sale_price = float(sale_input)

    if purchase_price < 0:
        raise ValueError

    if sale_price is not None and sale_price < 0:
        raise ValueError

    cursor = database.cursor()

    cursor.execute(
        """
        INSERT INTO item
        (purchasedate, purchaseprice, saleprice)
        VALUES (%s, %s, %s)
        """,
        (purchase_date, purchase_price, sale_price),
    )

    database.commit()
    cursor.close()

    print("\nItem added successfully.")


# This part will calculate the profit from all sold items in the database.
def calculate_profit(database):
    cursor = database.cursor()

    cursor.execute(
        """
        SELECT SUM(saleprice - purchaseprice)
        FROM item
        WHERE saleprice IS NOT NULL
        """
    )

    profit = cursor.fetchone()[0]

    if profit is None:
        profit = 0

    print(f"\nTotal profit: ${profit:.2f}")
    cursor.close()


# Display Main menu.
def show_menu():
    print("\nCollectible Tracking System")
    print("iv - items view")
    print("ia - item add")
    print("ic - item calculate")
    print("q  - quit")


# It will run the program until q is selected.
def main():
    database = None

    try:
        database = mysql.connector.connect(**DB_CONFIG)

        while True:
            show_menu()
            choice = input("Select an option: ").lower()

            try:
                if choice == "iv":
                    view_items(database)
                elif choice == "ia":
                    add_item(database)
                elif choice == "ic":
                    calculate_profit(database)
                elif choice == "q":
                    print("\nProgram closed.")
                    break
                else:
                    print("\nInvalid option.")

            except ValueError:
                print("\nPlease enter a valid date or price.")

            except Error as error:
                print("\nDatabase error:", error)

    except Error as error:
        print("\nCould not connect to the database:", error)

    finally:
        if database is not None and database.is_connected():
            database.close()


if __name__ == "__main__":
    main()
