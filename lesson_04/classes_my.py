from errno import EOWNERDEAD

from lesson_01.type_strigs import student


class Fruit:
    def __init__(self,name,weight):# konstrurtor
        self.name = name
        self.weight = weight
fruit1 = Fruit("Apple",10)      #создали
fruit2 = Fruit("Banana",20)

print(fruit1.name,fruit1.weight) #посмотрелт
print(fruit2.name,fruit2.weight)

fruit1.weight = 40 # увеличил вес
print(fruit1.name,fruit1.weight)

print("==============================================")

class Fruit:
    def __init__(self, name, day_ripe):
        self.name = name
        self.day_ripe = day_ripe

    def describe(self):
        print(f"This is a {self.name}")

    def wait_a_day(self):
        self.day_ripe -= 1
        print(f"{self.name} day ripe: {self.day_ripe}")

    def is_ripe(self):
        return self.day_ripe <=0

apple = Fruit("Apple",2)
apple.describe()
apple.wait_a_day()
print(apple.is_ripe())
apple.wait_a_day()
print(apple.is_ripe())

print("=================================================")

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

c1= Circle(2)
c2= Circle(5)

print("Area c1",c1.area())
print("Area c2",c2.area())

print("Pi is", Circle.pi)

print("==========================================")


class BankAccount:
    def __init__(self,owner,balance):#скрыли баланс nakö voi owner
        self.owner = owner
        self.__balance = balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}"

    def deposit(self,amount):
        if amount >0:
            self.__balance += amount
            print(f"Deposit {amount}.Balance:{self.__balance}")#положить на боланс
        else:
            print("Deposit can't be negative")

    def withdraw(self,amount):
        if amount >self.__balance:
            print("Not enough money on your account.")
        else:
            self.__balance -= amount
            print(f"Withdraw {amount}.Balance:{self.__balance}")

    def get_balance(self):# vain saa balans
        return self.__balance


account = BankAccount("John",100)
print(account)
account.deposit(100)
print(account)
account.withdraw(250)
account.withdraw(200)
#print(account.__balance)#ei näi balans
print(account.get_balance())#näkö balans

print("===========================================================================")



class Animal:
    def __init__(self,name,):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def swim(self):
        print(f"{self.name} swims around.")

class Dog(Animal):
    def meke_sound(self):
        print(f"{self.name} says: Woof! ")

class Cat(Animal):
    def meke_sound(self):
        print(f"{self.name} says: Meow! ")

    def play(self):
         print(f"{self.name} can play with ball")

dog = Dog("Doggi")
cat = Cat("Sima")
dog.eat()
cat.meke_sound()
dog.swim()
dog.meke_sound()
cat.play()
cat.eat()



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks
    def __str__(self):
        return f"Name: {self.name}, " "Age: {self.age}, Marks: {self.marks}"


student =Student("John",25,100)
print(student)

print("=========================================================================================")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self): #hieno print selvita
        return (
            f"Прямоугольник: ширина = {self.width}, высота = {self.height}\n"
            f"Площадь: {self.area()}\n"
            f"Периметр: {self.perimeter()}"
        )

rect = Rectangle(8, 10)
print(rect.__str__())

print("=========================================================================================")

class Thermometer:
    def __init__(self):
        self.__temperature = -273.15  # Yksityinen ominaisuus, alustettu absoluuttisen nollan arvoon

    def set_temperature(self, temperature):
        if temperature < -273.15:
            print("Virhe: lämpötila ei voi olla alle absoluuttisen nollan (-273.15°C).")
        else:
            self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

# Käyttöesimerkki
thermometer = Thermometer()
print(thermometer.get_temperature())  # Tulostaa: -273.15 (oletusarvo)

thermometer.set_temperature(15)
print(thermometer.get_temperature())  # Tulostaa: 15












