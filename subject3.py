import random
from array import array

# ── helpers ──────────────────────────────────────────────────────────────────

def separator():
    print("\n" + "=" * 55)

def nacisnij_enter():
    input("\n[Enter] – wróć do menu...")

# ── zadania ───────────────────────────────────────────────────────────────────

def zadanie_1():
    separator()
    print("ZADANIE 1 – Tworzenie listy i podstawowy dostęp")
    separator()
    numbers = [3, 7, 2, 9, 5]
    print(f"Lista:           {numbers}")
    print(f"Pierwszy (0):    {numbers[0]}")
    print(f"Trzeci (2):      {numbers[2]}")
    print(f"Ostatni (-1):    {numbers[-1]}")
    print(f"Długość listy:   {len(numbers)}")
    nacisnij_enter()

def zadanie_2():
    separator()
    print("ZADANIE 2 – Dodawanie i usuwanie elementów")
    separator()
    data = []
    print(f"Pusta lista:     {data}")
    data.append(10); print(f"Po append(10):   {data}")
    data.append(20); print(f"Po append(20):   {data}")
    data.append(30); print(f"Po append(30):   {data}")
    data.pop(1);     print(f"Po pop(1):       {data}")
    nacisnij_enter()

def zadanie_3():
    separator()
    print("ZADANIE 3 – Łączenie i powielanie list")
    separator()
    a = [1, 2, 3]
    b = [4, 5]
    polaczona = a + b
    print(f"a = {a},  b = {b}")
    print(f"a + b =          {polaczona}")
    print(f"(a+b) * 3 =      {polaczona * 3}")
    nacisnij_enter()

def zadanie_4():
    separator()
    print("ZADANIE 4 – Modyfikacja elementów w liście")
    separator()
    items = ["apple", "banana", "orange"]
    print(f"Przed:           {items}")
    items[1] = "kiwi"
    items[2] = "grape"
    print(f"Po zmianie:      {items}")
    nacisnij_enter()

def zadanie_5():
    separator()
    print("ZADANIE 5 – Sprawdzanie, czy element jest w liście")
    separator()
    colors = ["red", "green", "blue"]
    print(f"Lista: {colors}")
    for kolor in ("green", "yellow"):
        if kolor in colors:
            print(f"  '{kolor}' – JEST w liście ✓")
        else:
            print(f"  '{kolor}' – NIE MA w liście ✗")
    nacisnij_enter()

def zadanie_6():
    separator()
    print("ZADANIE 6 – Iterowanie po liście")
    separator()
    students = ["Anna", "Piotr", "Marek"]
    for student in students:
        print(f"  Student: {student}")
    nacisnij_enter()

def zadanie_7():
    separator()
    print("ZADANIE 7 – List slicing")
    separator()
    numbers = [10, 20, 30, 40, 50, 60]
    print(f"Lista:              {numbers}")
    print(f"Pierwsze 3 [:3]:    {numbers[:3]}")
    print(f"Ostatnie 3 [-3:]:   {numbers[-3:]}")
    print(f"Co drugi [::2]:     {numbers[::2]}")
    nacisnij_enter()

def zadanie_8():
    separator()
    print("ZADANIE 8 – Sortowanie i odwracanie listy")
    separator()
    points = [9, 1, 7, 3, 5]
    print(f"Przed:           {points}")
    points.sort();    print(f"Po sort():       {points}")
    points.reverse(); print(f"Po reverse():    {points}")
    nacisnij_enter()

def zadanie_9():
    separator()
    print("ZADANIE 9 – Zliczanie i wyszukiwanie elementów")
    separator()
    nums = [2, 3, 2, 5, 2, 7]
    print(f"Lista:                {nums}")
    print(f"Liczba 2 (count):     {nums.count(2)}x")
    print(f"Indeks liczby 5:      {nums.index(5)}")
    nacisnij_enter()

def zadanie_10():
    separator()
    print("ZADANIE 10 – Lista list (macierz)")
    separator()
    matrix = [[1, 2], [3, 4], [5, 6]]
    print(f"Macierz:              {matrix}")
    print(f"Drugi wiersz [1]:     {matrix[1]}")
    print(f"Element matrix[2][1]: {matrix[2][1]}")
    matrix.append([7, 8])
    print(f"Po append([7,8]):     {matrix}")
    nacisnij_enter()

def zadanie_11():
    separator()
    print("ZADANIE 11 – Tablica z modułu array")
    separator()
    arr = array('i', [1, 2, 3, 4])
    print(f"Typ:       {arr.typecode!r} (signed int)")
    print(f"Długość:   {len(arr)}")
    print(f"Elementy:  ", end="")
    for x in arr:
        print(x, end="  ")
    print()
    try:
        arr.append(3.14)
    except TypeError as e:
        print(f"Błąd przy dodaniu 3.14: {e}")
    nacisnij_enter()

def zadanie_12():
    separator()
    print("ZADANIE 12 – Modyfikowanie i iteracja po tablicy array")
    separator()
    arr = array('d', [1.5, 2.5, 3.5])
    print(f"Przed:     {list(arr)}")
    arr[1] = 4.5;    print(f"Po arr[1]=4.5:  {list(arr)}")
    arr.append(5.5); print(f"Po append(5.5): {list(arr)}")
    print("Elementy: ", end="")
    for x in arr:
        print(x, end="  ")
    print()
    print(f"Min: {min(arr)}   Max: {max(arr)}")
    nacisnij_enter()

def zadanie_13():
    separator()
    print("ZADANIE 13 – Krotka z 5 liczbami")
    separator()
    t = (4, 8, 15, 16, 23)
    print(f"Krotka:          {t}")
    print(f"Pierwszy:        {t[0]}")
    print(f"Ostatni:         {t[-1]}")
    print(f"Długość:         {len(t)}")
    print(f"Czy 10 w krotce: {10 in t}")
    nacisnij_enter()

def zadanie_14():
    separator()
    print("ZADANIE 14 – Slicing krotki")
    separator()
    t = (5, 10, 15, 20, 25, 30)
    print(f"Krotka:                   {t}")
    print(f"Indeksy 1–4 [1:4]:        {t[1:4]}")
    print(f"Co drugi [::2]:           {t[::2]}")
    print(f"Odwrócona [::-1]:         {t[::-1]}")
    nacisnij_enter()

def zadanie_15():
    separator()
    print("ZADANIE 15 – count() i index() na krotce")
    separator()
    numbers = (2, 4, 2, 6, 2, 8)
    print(f"Krotka:                {numbers}")
    print(f"Wystąpienia 2:         {numbers.count(2)}")
    print(f"Indeks pierwszego 6:   {numbers.index(6)}")
    try:
        numbers.index(100)
    except ValueError:
        print("Element 100 nie istnieje w krotce – obsłużono ValueError ✓")
    nacisnij_enter()

def zadanie_16():
    separator()
    print("ZADANIE 16 – Rozpakowywanie krotki studenta")
    separator()
    student = ("Anna", "Kowalska", 21, "Informatyka", 4.5)
    imie, nazwisko, wiek, kierunek, srednia = student
    print(f"Student: {imie} {nazwisko}, kierunek: {kierunek}, średnia: {srednia}")
    bez_sredniej = student[:4]
    print(f"Krotka bez średniej: {bez_sredniej}")
    try:
        student[2] = 22  # type: ignore
    except TypeError:
        print("Próba zmiany wieku – krotka jest niemutowalna – obsłużono TypeError ✓")
    nacisnij_enter()

def zadanie_17():
    separator()
    print("ZADANIE 17 – Rozpakowywanie z * i filtrowanie parzystych")
    separator()
    data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    start, *middle, end = data
    print(f"start={start}, end={end}, middle={middle}")
    parzyste = ()
    for x in data:
        if x % 2 == 0:
            parzyste += (x,)
    print(f"Parzyste:        {parzyste}")
    print(f"Długość:         {len(parzyste)}")
    print(f"Powielona x2:    {parzyste * 2}")
    nacisnij_enter()

def zadanie_18():
    separator()
    print("ZADANIE 18 – Operacje na uczestnikach kursów")
    separator()
    python_course = {"Anna", "Jan", "Maria", "Tomasz"}
    sql_course    = {"Maria", "Tomasz", "Karolina", "Piotr"}
    print(f"Python:          {sorted(python_course)}")
    print(f"SQL:             {sorted(sql_course)}")
    print(f"Oba kursy (∩):   {sorted(python_course & sql_course)}")
    print(f"Tylko Python:    {sorted(python_course - sql_course)}")
    print(f"Wszyscy (∪):     {sorted(python_course | sql_course)}")
    print(f"Tylko jeden (△): {sorted(python_course ^ sql_course)}")
    nacisnij_enter()

def zadanie_19():
    separator()
    print("ZADANIE 19 – Zarządzanie magazynem")
    separator()
    warehouse = {"laptop", "mysz", "klawiatura"}
    print(f"Start:                {sorted(warehouse)}")
    warehouse.add("monitor")
    print(f"Po add(monitor):      {sorted(warehouse)}")
    warehouse.update(["drukarka", "skaner"])
    print(f"Po update([...]):     {sorted(warehouse)}")
    warehouse.remove("mysz")
    print(f"Po remove(mysz):      {sorted(warehouse)}")
    warehouse.discard("tablet")
    print(f"Po discard(tablet):   {sorted(warehouse)}  (brak błędu)")
    usuniety = warehouse.pop()
    print(f"Pop() usunął:         '{usuniety}'")
    print(f"Po pop():             {sorted(warehouse)}")
    warehouse.clear()
    print(f"Po clear():           {warehouse}")
    nacisnij_enter()

def zadanie_20():
    separator()
    print("ZADANIE 20 – Analiza liter w tekście")
    separator()
    text = "programowanie w pythonie"
    znaki = set(text)
    print(f"Tekst:                   \"{text}\"")
    print(f"Unikalne znaki (raw):    {znaki}")
    znaki.discard(" ")
    print(f"Bez spacji:              {znaki}")
    print(f"Litera 'p' w zbiorze:    {'p' in znaki}")
    print(f"Liczba unikalnych znaków: {len(znaki)}")
    nacisnij_enter()

def zadanie_21():
    separator()
    print("ZADANIE 21 – Analiza zainteresowań studentów")
    separator()
    s1 = {"AI", "Python", "Data Science"}
    s2 = {"Python", "Cybersecurity", "Networks"}
    s3 = {"AI", "Networks", "Robotics"}
    print(f"Student1: {s1}")
    print(f"Student2: {s2}")
    print(f"Student3: {s3}")
    wszystkie    = s1 | s2 | s3
    wspolne_1_3  = s1 & s3
    unikalne_s2  = s2 - s1 - s3
    # zainteresowania dokładnie u 1 studenta
    dokladnie_1 = set()
    for x in wszystkie:
        if sum(x in s for s in (s1, s2, s3)) == 1:
            dokladnie_1.add(x)
    print(f"\nWszystkie unikalne:         {sorted(wszystkie)}")
    print(f"Wspólne s1 ∩ s3:            {sorted(wspolne_1_3)}")
    print(f"Unikalne dla s2:            {sorted(unikalne_s2)}")
    print(f"Dokładnie u 1 studenta:     {sorted(dokladnie_1)}")
    nacisnij_enter()

# ── słownik zadań ─────────────────────────────────────────────────────────────

ZADANIA = {
    1:  zadanie_1,
    2:  zadanie_2,
    3:  zadanie_3,
    4:  zadanie_4,
    5:  zadanie_5,
    6:  zadanie_6,
    7:  zadanie_7,
    8:  zadanie_8,
    9:  zadanie_9,
    10: zadanie_10,
    11: zadanie_11,
    12: zadanie_12,
    13: zadanie_13,
    14: zadanie_14,
    15: zadanie_15,
    16: zadanie_16,
    17: zadanie_17,
    18: zadanie_18,
    19: zadanie_19,
    20: zadanie_20,
    21: zadanie_21,
}

OPISY = {
    1:  "Tworzenie listy i podstawowy dostęp",
    2:  "Dodawanie i usuwanie elementów",
    3:  "Łączenie i powielanie list",
    4:  "Modyfikacja elementów",
    5:  "Sprawdzanie elementu w liście (in)",
    6:  "Iterowanie po liście",
    7:  "List slicing",
    8:  "Sortowanie i odwracanie",
    9:  "count() i index()",
    10: "Lista list – macierz 2D",
    11: "Tablica array – tworzenie",
    12: "Tablica array – modyfikacja i iteracja",
    13: "Krotka z 5 liczbami",
    14: "Slicing krotki",
    15: "count() i index() na krotce",
    16: "Rozpakowywanie krotki studenta",
    17: "Rozpakowywanie z * i filtrowanie",
    18: "Operacje na zbiorach (kursy)",
    19: "Zarządzanie magazynem (zbiory)",
    20: "Analiza liter w tekście",
    21: "Analiza zainteresowań studentów",
}

# ── menu główne ───────────────────────────────────────────────────────────────

def wyswietl_menu():
    print("\n" + "=" * 55)
    print("  MENU – Zadania Python (Listy, Krotki, Zbiory)")
    print("=" * 55)
    for nr, opis in OPISY.items():
        print(f"  {nr:>2}. {opis}")
    print("-" * 55)
    print("   R – Losowe zadanie")
    print("   W – Wyjście")
    print("=" * 55)

def main():
    print("\n" + "★" * 55)
    print("  Witaj w interaktywnych ćwiczeniach z Pythona!")
    print("★" * 55)

    while True:
        wyswietl_menu()
        wybor = input("  Twój wybór: ").strip().upper()

        if wybor == "W":
            print("\nDo zobaczenia! 👋\n")
            break

        if wybor == "R":
            nr = random.randint(1, 21)
            print(f"\n  🎲 Wylosowano zadanie {nr}: {OPISY[nr]}")
            ZADANIA[nr]()
            continue

        try:
            nr = int(wybor)
            if nr in ZADANIA:
                ZADANIA[nr]()
            else:
                print(f"  ⚠  Wpisz liczbę 1–21, R lub W.")
        except ValueError:
            print(f"  ⚠  Nieprawidłowy wybór. Wpisz liczbę 1–21, R lub W.")

if __name__ == "__main__":
    main()