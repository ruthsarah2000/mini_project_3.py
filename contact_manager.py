import re
import json

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def display_menu(self):
        print("\nWelcome to the Contact Management System!\n")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

    def add_contact(self):
        print("\nAdding a new contact:")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        additional_info = input("Enter additional information: ")
        self.contacts[email] = {'name': name, 'phone': phone, 'email': email, 'additional_info': additional_info}
        print("Contact added successfully!")

    def edit_contact(self):
        print("\nEditing an existing contact:")
        email = input("Enter email address of the contact to edit: ")
        if email in self.contacts:
            print("Current details:")
            print(self.contacts[email])
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            additional_info = input("Enter new additional information (leave blank to keep current): ")
            if name:
                self.contacts[email]['name'] = name
            if phone:
                self.contacts[email]['phone'] = phone
            if email:
                self.contacts[email]['email'] = email
            if additional_info:
                self.contacts[email]['additional_info'] = additional_info
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        print("\nDeleting a contact:")
        email = input("Enter email address of the contact to delete: ")
        if email in self.contacts:
            del self.contacts[email]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def search_contact(self):
        print("\nSearching for a contact:")
        email = input("Enter email address of the contact to search: ")
        if email in self.contacts:
            print("Contact details:")
            print(self.contacts[email])
        else:
            print("Contact not found.")

    def display_all_contacts(self):
        print("\nAll contacts:")
        for email, details in self.contacts.items():
            print(f"Email: {email}")
            print("Details:", details)
            print()

    def export_contacts(self):
        print("\nExporting contacts to a text file:")
        file_name = input("Enter the file name to save contacts: ")
        with open(file_name, 'w') as file:
            json.dump(self.contacts, file)
        print("Contacts exported successfully!")

    def import_contacts(self):
        print("\nImporting contacts from a text file:")
        file_name = input("Enter the file name to import contacts from: ")
        try:
            with open(file_name, 'r') as file:
                self.contacts.update(json.load(file))
            print("Contacts imported successfully!")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON data.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.edit_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                self.search_contact()
            elif choice == '5':
                self.display_all_contacts()
            elif choice == '6':
                self.export_contacts()
            elif choice == '7':
                self.import_contacts()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run()
