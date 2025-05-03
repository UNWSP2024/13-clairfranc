# Claire Francis, May 1, 2025, Week13_program4
#Write a program that creates a database named phonebook.db.
# The database should have a table named Entries, with columns for a person’s name and phone number.
# Next, write a CRUD application that lets the user add rows to the Entries table,
# look up a person’s phone number, change a person’s phone number, and delete specified rows.


import sqlite3

def initialize_db():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Entries (name TEXT PRIMARY KEY, phone TEXT NOT NULL)""")
    conn.commit()
    conn.close()

def add_entry(name, phone):
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Entries (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Entry added successfully.")
    except sqlite3.IntegrityError:
        print("Error: An entry with that name already exists.")
    conn.close()

def lookup_entry(name):
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute("SELECT phone FROM Entries WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print(f"{name}'s phone number is {result[0]}")
    else:
        print("Entry not found.")

def update_entry(name, new_phone):
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Entries SET phone = ? WHERE name = ?", (new_phone, name))
    if cursor.rowcount == 0:
        print("No such entry found to update.")
    else:
        print("Phone number updated.")
    conn.commit()
    conn.close()

def delete_entry(name):
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Entries WHERE name = ?", (name,))
    if cursor.rowcount == 0:
        print("No such entry found to delete.")
    else:
        print("Entry deleted.")
    conn.commit()
    conn.close()

def menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Entry")
        print("2. Look Up Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            add_entry(name, phone)
        elif choice == '2':
            name = input("Enter name to look up: ").strip()
            lookup_entry(name)
        elif choice == '3':
            name = input("Enter name to update: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            update_entry(name, new_phone)
        elif choice == '4':
            name = input("Enter name to delete: ").strip()
            delete_entry(name)
        elif choice == '5':
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_db()
    menu()