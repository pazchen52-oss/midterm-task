from view import View
from model import Model

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):
        while True:
            choice = self.view.menu()

            if choice == "1":
                name = self.view.get_name()
                address = self.view.get_address()
                phone = self.view.get_phone()
                self.model.add(name, address, phone)

            elif choice == "2":
                people = self.model.get_all()
                self.view.show_people(people)

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")