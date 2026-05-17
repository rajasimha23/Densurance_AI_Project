import sqlite3

DB_FILE = "risk.db"
TABLE_NAME = "assessments"


def fetch_all():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def fetch_last_n(n):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT * FROM {TABLE_NAME}
        ORDER BY rowid DESC
        LIMIT ?
    """, (n,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def fetch_row_by_id(row_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT * FROM {TABLE_NAME}
        WHERE rowid = ?
    """, (row_id,))

    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Row not found")

    conn.close()


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Fetch all rows")
        print("2. Fetch last N rows")
        print("3. Fetch row by ID")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            fetch_all()

        elif choice == "2":
            n = int(input("Enter N: "))
            fetch_last_n(n)

        elif choice == "3":
            row_id = int(input("Enter row id: "))
            fetch_row_by_id(row_id)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()