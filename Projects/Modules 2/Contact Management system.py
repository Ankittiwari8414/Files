# Project 2:  Contact Management System
# LAB-50

import os

def menu():
    print("Contact Management System")
    print("1. Add a contact")
    print("2. view all contacts")
    print("3. search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")

# Task 1: Function to load contacts from a file

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            contacts = [line.strip().split(",") for line in file.readlines()]
    return contacts

# Task 2: Function to save contacts to a file

def save_contacts(filename, contacts):
    with open(filename, "w") as file:
        for contact in contacts:
            file.write(",".join(contact) + "\n")

# Task 3: Function to add a contact

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    contacts.append([name, phone])
    print("Contact added successfully.")

# # Task 4: Function to view all contacts

def view_contacts(contacts):
    if contacts:
        print("All Contacts:")
        for contact in contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}")
    else:
        print("No contacts found.")

# Task 5: Function to update a contact

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact[0] == name:
            contact[1] = input(f"Enter new phone for {name} (current: {contact[1]}): ")
            print("Contact updated successfully.")
            return
    print("Contact not found.")

# Task 6: Function to delete a contact

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact[0] == name:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

# Task 7: Main function to run the Contact Management System 

def main():
    filename = "contacts.txt"
    contacts = load_contacts(filename)

    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact = input("Enter the name of the contact to search: ")
            found = False
            for contact in contacts:
                if contact[0] == search_contact:
                    print(f"Found - Name: {contact[0]}, Phone: {contact[1]}")
                    found = True
                    break
            if not found:
                print("Contact not found.")
        elif choice == "4":
            update_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == "5":
            delete_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()