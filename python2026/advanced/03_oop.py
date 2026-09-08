# ─────────────────────────────────────────────
# ADV 03 — Object-Oriented Programming (OOP)
# ─────────────────────────────────────────────#
# WHAT IS OOP?
#   Object-Oriented Programming is a way of organising code
#   around "objects" — bundles of data (attributes) and
#   behaviour (methods). A class is the blueprint; an object
#   is a specific instance built from that blueprint.
#   OOP makes large programs easier to understand, extend,
#   and maintain through: Encapsulation, Inheritance, Polymorphism.
# ─────────────────────────────────────────────
# ── 1. Class basics ──────────────────────────

class Dog:
    # Class variable — shared by ALL instances
    species = "Canis lupus familiaris"

    # __init__ is the constructor
    def __init__(self, name, breed, age):
        # Instance variables — unique per object
        self.name  = name
        self.breed = breed
        self.age   = age

    # Instance method — self refers to the current object
    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} ({self.breed}), {self.age} year(s) old")

    # __str__ — called by print() and str()
    def __str__(self):
        return f"Dog({self.name!r})"

    # __repr__ — unambiguous representation (for debugging)
    def __repr__(self):
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"


buddy = Dog("Buddy", "Labrador", 3)
luna  = Dog("Luna",  "Poodle",   2)

buddy.bark()          # Buddy says: Woof!
luna.describe()       # Luna (Poodle), 2 year(s) old
print(buddy)          # Dog('Buddy')
print(repr(buddy))    # Dog(name='Buddy', breed='Labrador', age=3)
print(Dog.species)    # Canis lupus familiaris
print(buddy.species)  # also works


# ── 2. Inheritance ───────────────────────────

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")

    def __str__(self):
        return f"{type(self).__name__}({self.name!r})"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"


class Duck(Animal):
    def speak(self):
        return f"{self.name} says: Quack!"


animals = [Cat("Whiskers"), Duck("Donald"), Cat("Felix")]
for animal in animals:
    print(animal.speak())   # polymorphism — same method, different behaviour


# ── 3. super() ───────────────────────────────

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)     # call parent __init__
        self.battery_kwh = battery_kwh

    def info(self):
        base = super().info()                   # call parent info()
        return f"{base} (Electric, {self.battery_kwh} kWh)"


car = ElectricCar("Tesla", "Model 3", 2024, 82)
print(car.info())    # 2024 Tesla Model 3 (Electric, 82 kWh)


# ── 4. Encapsulation ─────────────────────────
# Python uses conventions, not strict access modifiers.
# _single_underscore  → "protected" (internal use, still accessible)
# __double_underscore → "private"   (name-mangled, harder to access)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner    = owner
        self._balance = balance   # "protected"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @property                      # getter — accessed like an attribute
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)    # 1300  — calls the getter
acc.balance = 2000    # calls the setter
print(acc.balance)    # 2000


# ── 5. Class methods & Static methods ────────

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):   # alternative constructor
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(r):             # utility — no self/cls needed
        return r > 0


c1 = Circle(5)
c2 = Circle.from_diameter(10)          # classmethod
print(c1.area())                        # 78.53975
print(c2.radius)                        # 5.0
print(Circle.is_valid_radius(-1))       # False


# ── 6. Dataclasses (Python 3.7+) ─────────────
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0                     # default value

    def distance_to_origin(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


p = Point(3, 4)
print(p)                               # Point(x=3, y=4, z=0.0)
print(p.distance_to_origin())          # 5.0

# Dataclasses auto-generate __init__, __repr__, __eq__
p2 = Point(3, 4)
print(p == p2)    # True


# ── 7. Multiple inheritance & MRO ────────────

class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):    # inherits from both B and C
    pass

d = D()
print(d.hello())           # B  — Method Resolution Order: D → B → C → A
print(D.__mro__)           # shows the full lookup chain

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   __init__              — constructor
#   __str__ / __repr__    — string representations
#   Inheritance / super() — code reuse
#   @property             — controlled attribute access
#   @classmethod          — factory methods
#   @staticmethod         — utility functions
#   @dataclass            — auto-generated boilerplate
#   MRO                   — Method Resolution Order
# ─────────────────────────────────────────────
