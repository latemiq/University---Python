"""
======================================================
  ZADANIA Z ZAKRESU KLAS I OBIEKTÓW W PYTHONIE
======================================================
Uruchomienie:
  python zadania_oop.py          – menu interaktywne
  python zadania_oop.py --losuj  – losuje i uruchamia jedno zadanie
  python zadania_oop.py --all    – uruchamia wszystkie zadania
"""

import random
import sys
import math

# ──────────────────────────────────────────────────────────────────────────────
#  BLOK 1 – Klasy i obiekty (Zadania 1–7)
# ──────────────────────────────────────────────────────────────────────────────

# ── Zadanie 1 ─────────────────────────────────────────────────────────────────
class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} mówi: Hau!")


def zadanie_1():
    print("\n🐕  Zadanie 1 – Klasa Dog")
    pies = Dog("Reks", 3)
    print(f"  Imię: {pies.name}, Wiek: {pies.age} lat")
    pies.bark()


# ── Zadanie 2 ─────────────────────────────────────────────────────────────────
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def describe(self):
        print(f'  Książka: "{self.title}" – autor: {self.author}')


def zadanie_2():
    print("\n📚  Zadanie 2 – Klasa Book")
    ksiazka = Book("Wiedźmin", "Andrzej Sapkowski")
    ksiazka.describe()


# ── Zadanie 3 ─────────────────────────────────────────────────────────────────
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def zadanie_3():
    print("\n📐  Zadanie 3 – Klasa Rectangle")
    r = Rectangle(5, 3)
    print(f"  Prostokąt {r.width}×{r.height}")
    print(f"  Pole:      {r.area()}")
    print(f"  Obwód:     {r.perimeter()}")


# ── Zadanie 4 ─────────────────────────────────────────────────────────────────
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print("  ❌ Kwota wpłaty musi być dodatnia.")
            return
        self.balance += amount
        print(f"  ✅ Wpłacono {amount:.2f} zł. Saldo: {self.balance:.2f} zł")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("  ❌ Kwota wypłaty musi być dodatnia.")
        elif amount > self.balance:
            print(f"  ❌ Brak środków! Saldo: {self.balance:.2f} zł")
        else:
            self.balance -= amount
            print(f"  ✅ Wypłacono {amount:.2f} zł. Saldo: {self.balance:.2f} zł")


def zadanie_4():
    print("\n🏦  Zadanie 4 – Klasa BankAccount")
    konto = BankAccount("Jan Kowalski", 1000)
    print(f"  Właściciel: {konto.owner}")
    konto.deposit(500)
    konto.withdraw(200)
    konto.withdraw(2000)   # próba wypłaty ponad saldo


# ── Zadanie 5 ─────────────────────────────────────────────────────────────────
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def calculate_bonus(self) -> float:
        return self.salary * 0.10


class Manager(Employee):
    def calculate_bonus(self) -> float:
        return self.salary * 0.20


class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language


def zadanie_5():
    print("\n👔  Zadanie 5 – System pracowników (dziedziczenie + polimorfizm)")
    pracownicy = [
        Employee("Anna Nowak", 5000),
        Manager("Piotr Wiśniewski", 8000),
        Developer("Marta Kowalczyk", 7000, "Python"),
    ]
    for p in pracownicy:
        premia = p.calculate_bonus()
        lang = f" [{p.programming_language}]" if hasattr(p, "programming_language") else ""
        print(f"  {type(p).__name__:<12} {p.name:<20}{lang}  "
              f"→ premia: {premia:.2f} zł")


# ── Zadanie 6 ─────────────────────────────────────────────────────────────────
class Animal:
    def make_sound(self):
        return "Nieznany dźwięk"


class Cat(Animal):
    def make_sound(self):
        return "Miau!"


class Cow(Animal):
    def make_sound(self):
        return "Muuu!"


def zadanie_6():
    print("\n🐾  Zadanie 6 – Klasy zwierząt (polimorfizm)")
    zwierzeta = [Animal(), Cat(), Cow()]
    for z in zwierzeta:
        print(f"  {type(z).__name__:<8} mówi: {z.make_sound()}")


# ── Zadanie 7 ─────────────────────────────────────────────────────────────────
class Counter:
    _count = 0

    def __init__(self):
        Counter._count += 1

    @classmethod
    def how_many(cls) -> int:
        return cls._count


def zadanie_7():
    print("\n🔢  Zadanie 7 – Klasa Counter (atrybut klasy)")
    _ = [Counter() for _ in range(5)]
    print(f"  Utworzono {Counter.how_many()} obiektów klasy Counter")


# ──────────────────────────────────────────────────────────────────────────────
#  BLOK 2 – Zasady OOP (Zadania OOP 1–7)
# ──────────────────────────────────────────────────────────────────────────────

# ── OOP Zadanie 1 ─────────────────────────────────────────────────────────────
class Vehicle:
    def __init__(self, marka: str, predkosc_max: int):
        self.marka = marka
        self.predkosc_max = predkosc_max

    def info(self) -> str:
        return f"Pojazd: {self.marka}, prędkość max: {self.predkosc_max} km/h"


class Car(Vehicle):
    def __init__(self, marka: str, predkosc_max: int, liczba_drzwi: int):
        super().__init__(marka, predkosc_max)
        self.liczba_drzwi = liczba_drzwi

    def info(self) -> str:
        return (f"Samochód: {self.marka}, "
                f"prędkość max: {self.predkosc_max} km/h, "
                f"drzwi: {self.liczba_drzwi}")


class Bike(Vehicle):
    def __init__(self, marka: str, predkosc_max: int, typ: str):
        super().__init__(marka, predkosc_max)
        self.typ = typ

    def info(self) -> str:
        return (f"Rower: {self.marka}, "
                f"prędkość max: {self.predkosc_max} km/h, "
                f"typ: {self.typ}")


def zadanie_oop_1():
    print("\n🚗  OOP Zadanie 1 – System pojazdów")
    pojazdy = [
        Car("Toyota", 200, 4),
        Car("Fiat 500", 160, 2),
        Bike("Trek", 45, "górski"),
        Bike("Giant", 55, "szosowy"),
    ]
    for p in pojazdy:
        print(f"  {p.info()}")


# ── OOP Zadanie 2 ─────────────────────────────────────────────────────────────
class Dog2(Animal):
    def make_sound(self):
        return "Hau!"


def animal_sound(animal: Animal):
    print(f"  {type(animal).__name__:<6} → {animal.make_sound()}")


def zadanie_oop_2():
    print("\n🦁  OOP Zadanie 2 – Zwierzęta w zoo")
    zoo = [Dog2(), Cat(), Cow()]
    for z in zoo:
        animal_sound(z)


# ── OOP Zadanie 3 ─────────────────────────────────────────────────────────────
class SecureBankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Kwota musi być dodatnia.")
        self.__balance += amount
        print(f"  ✅ Wpłata {amount:.2f} zł  │  Saldo: {self.__balance:.2f} zł")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Kwota musi być dodatnia.")
        if amount > self.__balance:
            print(f"  ❌ Za mało środków (saldo: {self.__balance:.2f} zł)")
        else:
            self.__balance -= amount
            print(f"  ✅ Wypłata {amount:.2f} zł │  Saldo: {self.__balance:.2f} zł")

    def get_balance(self) -> float:
        return self.__balance


def zadanie_oop_3():
    print("\n🔒  OOP Zadanie 3 – Konto bankowe z enkapsulacją")
    konto = SecureBankAccount("Alicja", 500)
    konto.deposit(300)
    konto.withdraw(100)
    konto.withdraw(800)
    print(f"  Aktualne saldo: {konto.get_balance():.2f} zł")


# ── OOP Zadanie 4 ─────────────────────────────────────────────────────────────
class SmartThermometer:
    ABSOLUTE_ZERO = -273.15

    def __init__(self):
        self.__temperature = 20.0

    def set_temperature(self, value: float):
        if value < self.ABSOLUTE_ZERO:
            print(f"  ❌ Temperatura {value}°C jest poniżej zera absolutnego "
                  f"({self.ABSOLUTE_ZERO}°C)!")
        else:
            self.__temperature = value
            print(f"  🌡️  Ustawiono temperaturę: {self.__temperature}°C")

    def get_temperature(self) -> float:
        return self.__temperature


def zadanie_oop_4():
    print("\n🌡️   OOP Zadanie 4 – SmartThermometer")
    t = SmartThermometer()
    t.set_temperature(36.6)
    t.set_temperature(-300)   # poniżej zera absolutnego
    t.set_temperature(-273.15)
    print(f"  Bieżąca temperatura: {t.get_temperature()}°C")


# ── OOP Zadanie 5 ─────────────────────────────────────────────────────────────
class Shape:
    def area(self) -> float:
        return 0.0


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class RectangleShape(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


def zadanie_oop_5():
    print("\n🔷  OOP Zadanie 5 – System kształtów")
    ksztalty = [
        Circle(5),
        RectangleShape(4, 6),
        Triangle(3, 8),
    ]
    for k in ksztalty:
        print(f"  {type(k).__name__:<16} pole = {k.area():.4f}")


# ── OOP Zadanie 6 ─────────────────────────────────────────────────────────────
class EBook:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.liczba_stron = pages
        self.__current_page = 0
        self.__is_open = False

    def open_book(self):
        self.__is_open = True
        self.__current_page = 1
        print(f"  📖 Otwarto książkę \"{self.title}\" (strona {self.__current_page})")

    def read_page(self):
        if not self.__is_open:
            print("  ❌ Najpierw otwórz książkę!")
            return
        if self.__current_page > self.liczba_stron:
            print("  📕 Koniec książki!")
            return
        print(f"  📄 Czytasz stronę {self.__current_page}/{self.liczba_stron}")
        self.__current_page += 1


def zadanie_oop_6():
    print("\n📱  OOP Zadanie 6 – E-book reader")
    ebook = EBook("Python dla każdego", 3)
    ebook.read_page()       # bez otwarcia
    ebook.open_book()
    for _ in range(5):      # 3 strony + 2 nadmiarowe
        ebook.read_page()


# ── OOP Zadanie 7 ─────────────────────────────────────────────────────────────
class EmployeeBase:
    def __init__(self, imie: str):
        self.imie = imie

    def calculate_salary(self) -> float:
        return 0.0


class FullTimeEmployee(EmployeeBase):
    def __init__(self, imie: str, stala_pensja: float):
        super().__init__(imie)
        self.stala_pensja = stala_pensja

    def calculate_salary(self) -> float:
        return self.stala_pensja


class PartTimeEmployee(EmployeeBase):
    def __init__(self, imie: str, stawka_godzinowa: float, godziny: int):
        super().__init__(imie)
        self.stawka_godzinowa = stawka_godzinowa
        self.godziny = godziny

    def calculate_salary(self) -> float:
        return self.stawka_godzinowa * self.godziny


def zadanie_oop_7():
    print("\n💼  OOP Zadanie 7 – System pracowników")
    pracownicy = [
        FullTimeEmployee("Katarzyna", 6000),
        FullTimeEmployee("Marek", 7500),
        PartTimeEmployee("Zofia", 40, 80),
        PartTimeEmployee("Tomasz", 55, 60),
    ]
    for p in pracownicy:
        wynagrodzenie = p.calculate_salary()
        print(f"  {type(p).__name__:<20} {p.imie:<12} "
              f"→ wynagrodzenie: {wynagrodzenie:.2f} zł")


# ──────────────────────────────────────────────────────────────────────────────
#  REJESTR WSZYSTKICH ZADAŃ
# ──────────────────────────────────────────────────────────────────────────────

ZADANIA = {
    "1":     (zadanie_1,     "Klasa Dog – atrybut i metoda"),
    "2":     (zadanie_2,     "Klasa Book – konstruktor i describe()"),
    "3":     (zadanie_3,     "Klasa Rectangle – pole i obwód"),
    "4":     (zadanie_4,     "Klasa BankAccount – wpłata/wypłata"),
    "5":     (zadanie_5,     "System pracowników – dziedziczenie"),
    "6":     (zadanie_6,     "Zwierzęta – polimorfizm"),
    "7":     (zadanie_7,     "Counter – atrybut klasy"),
    "oop1":  (zadanie_oop_1, "OOP: System pojazdów"),
    "oop2":  (zadanie_oop_2, "OOP: Zwierzęta w zoo"),
    "oop3":  (zadanie_oop_3, "OOP: Konto z enkapsulacją"),
    "oop4":  (zadanie_oop_4, "OOP: SmartThermometer"),
    "oop5":  (zadanie_oop_5, "OOP: System kształtów"),
    "oop6":  (zadanie_oop_6, "OOP: E-book reader"),
    "oop7":  (zadanie_oop_7, "OOP: System pracowników"),
}


def pokaz_menu():
    print("\n" + "═" * 55)
    print("   ZADANIA OOP W PYTHONIE – wybierz opcję")
    print("═" * 55)
    for klucz, (_, opis) in ZADANIA.items():
        print(f"  [{klucz:>4}]  {opis}")
    print("  [all ]  Uruchom wszystkie zadania")
    print("  [los ]  Wylosuj zadanie")
    print("  [q   ]  Wyjście")
    print("═" * 55)


def uruchom_zadanie(klucz: str):
    if klucz in ZADANIA:
        fn, opis = ZADANIA[klucz]
        print(f"\n{'─'*55}")
        print(f"  ▶  {opis}")
        print("─" * 55)
        fn()
        print()
    else:
        print(f"  ❌ Nieznane zadanie: {klucz}")


def main():
    args = sys.argv[1:]

    # ── tryb --all ─────────────────────────────────────────────────────────
    if "--all" in args:
        print("\n🚀  Uruchamiam wszystkie zadania…")
        for klucz in ZADANIA:
            uruchom_zadanie(klucz)
        return

    # ── tryb --losuj ───────────────────────────────────────────────────────
    if "--losuj" in args:
        klucz = random.choice(list(ZADANIA.keys()))
        _, opis = ZADANIA[klucz]
        print(f"\n🎲  Wylosowano: [{klucz}] {opis}")
        uruchom_zadanie(klucz)
        return

    # ── tryb interaktywny ──────────────────────────────────────────────────
    while True:
        pokaz_menu()
        wybor = input("  Twój wybór: ").strip().lower()

        if wybor in ("q", "quit", "exit"):
            print("\n  Do zobaczenia! 👋\n")
            break
        elif wybor == "all":
            for klucz in ZADANIA:
                uruchom_zadanie(klucz)
        elif wybor == "los":
            klucz = random.choice(list(ZADANIA.keys()))
            _, opis = ZADANIA[klucz]
            print(f"\n  🎲 Wylosowano: [{klucz}] {opis}")
            uruchom_zadanie(klucz)
        else:
            uruchom_zadanie(wybor)

        input("  [Enter] – powrót do menu…")


if __name__ == "__main__":
    main()