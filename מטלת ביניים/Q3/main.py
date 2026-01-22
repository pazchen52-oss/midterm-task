from Dog import Dog
from Cat import Cat
from animal import Animal

def main():
    animals = [Dog(), Cat()]  
    for animal in animals:
        if isinstance(animal, Animal):  
            print(animal.speak())
        else:
            print("Not an Animal")

if __name__ == "__main__":
    main()