class Contact:
    def __init__(self, name, age, address, job, email):
        self.name = name
        self.age = age
        self.address = address
        self.job = job
        self.email = email

class Addressbook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def find_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "No matching contact found."

    def display_contacts(self):
        for contact in self.contacts.values():
            print(f"Name: {contact.name}, Age: {contact.age}, Address: {contact.address}, Job: {contact.job}, Email: {contact.email}")

# Tạo một đối tượng Contact
c = Contact("James", 17, "Norway", "Engineer", "caom2111@gmail.com")

# Tạo một danh bạ
address_book = Addressbook()

# Thêm liên hệ vào danh bạ
address_book.add_contact(c)

# In ra thông tin liên hệ
address_book.display_contacts(c)
