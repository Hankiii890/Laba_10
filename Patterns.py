#Паттерн Фабрика (Factory)
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def get_animal(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def get_animal(self):
        return "Cat"

    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def get_animal(self):
        return "Dog"

    def make_sound(self):
        return "Woof"

class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type is None:
            return None

        if animal_type == "Cat":
            return Cat()
        elif animal_type == "Dog":
            return Dog()

        return None


#Паттерн Абстрактная фабрика (Abstract Factory)

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

class WinButton(Button):
    def paint(self):
        print("Windows button is painted")

class MacButton(Button):
    def paint(self):
        print("Mac button is painted")

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = None

    def create_ui(self):
        self.button = self.factory.create_button()

    def paint(self):
        self.button.paint()

if __name__ == "__main__":
    app = Application(WinFactory())
    app.create_ui()
    app.paint()

    app = Application(MacFactory())
    app.create_ui()
    app.paint()


#Паттерн Строитель (Builder)

class Product:
    def __init__(self):
        self.product_id = None
        self.product_name = None
        self.product_price = None
        self.product_description = None

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_product_price(self, product_price):
        self.product_price = product_price

    def set_product_description(self, product_description):
        self.product_description = product_description

class ProductBuilder:
    def __init__(self):
        self.product = Product()

    def set_product_id(self, product_id):
        self.product.set_product_id(product_id)
        return self

    def set_product_name(self, product_name):
        self.product.set_product_name(product_name)
        return self

    def set_product_price(self, product_price):
        self.product.set_product_price(product_price)
        return self

    def set_product_description(self, product_description):
        self.product.set_product_description(product_description)
        return self

    def build(self):
        return self.product

product = ProductBuilder() \
            .set_product_id(123) \
            .set_product_name("Fruit Juice") \
            .set_product_price(2.99) \
            .set_product_description("A delicious health drink.") \
            .build()
