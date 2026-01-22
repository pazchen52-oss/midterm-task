class View:
    def get_name(self):
        return input("Enter name: ")

    def get_address(self):
        return input("Enter address: ")

    def get_phone(self):
        return input("Enter phone: ")

    def show_people(self, people):
        print("\n--- People List ---")
        for p in people:
            print(f"{p.name}, {p.address}, {p.phone}")
        print("-------------------\n")

    def menu(self):
        print("1. Add person")
        print("2. Show all people")
        print("3. Exit")
        return input("Choose option: ")