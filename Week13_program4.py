# Claire Francis, May 1, 2025, Week13_program4
#Write a program that creates a database named phonebook.db.
# The database should have a table named Entries, with columns for a person’s name and phone number.
# Next, write a CRUD application that lets the user add rows to the Entries table,
# look up a person’s phone number, change a person’s phone number, and delete specified rows.


import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Entries')
cursor.execute('''CREATE TABLE IF NOT EXISTS Entries (name TEXT PRIMARY KEY, number INTEGER NOT NULL)''')
conn.commit()

def add_contact(name, number):
    try:
        cursor.execute('INSERT INTO Entries (name, number) VALUES (?,?)', (name, number))
        conn.commit()
        print(f"Added {name} with phone {number}")
    except sqlite3.IntegrityError:
        print(f'Contact for {name} already exists.')

def search_number(name):
    cursor.execute('SELECT number FROM Entries WHERE name = ?', (name,))
    result = cursor.fetchone()
    if result:
        print(f"{name}'s phone number is {result[0]}")
    else:
        print(f"No contact found for {name}")

def update_number(name, new_number):
    cursor.execute('UPDATE Entries SET number = ? WHERE name = ?', (new_number, name))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Updated {name}' phone number to {new_number}")
    else:
        print(f"No contact found for {name}")

def delete_contact(name):
    cursor.execute('DELETE FROM Entries WHERE name = ?', (name,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Deleted contact for {name}")
    else:
        print(f"No contact found for {name}")

def main():
    while True:
        print("Phonebook Menu:")
        print("1. Add Contact")
        print("2. Search for Phone Number")
        print("3. Update Phone Number")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == '2':
            name = input("Enter name to search for: ")
            search_number(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            new_number = input("Enter new phone number: ")
            update_number(name, new_number)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting phonebook.")
            break
        else:
            print("Invalid contact. Try again.")

    conn.close()
if __name__ == '__main__':
    main()