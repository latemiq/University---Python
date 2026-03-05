import math
import random


# ==============================
# ===== DZIAŁ 1 – Typy danych ===
# ==============================

def dzial1():
    while True:
        print("\n=== DZIAŁ 1 – Typy danych, zmienne, konwersje ===")
        print("1  - Kalkulator BMI")
        print("2  - Dochód rodzinny")
        print("3  - Konwersja wzrostu na stopy i cale")
        print("4  - Dystans do horyzontu")
        print("5  - Pole i obwód koła")
        print("6  - Kalkulator kosztów transportu")
        print("7  - Obliczanie VAT")
        print("8  - Sprawdzanie zwolnienia podatkowego")
        print("9  - Walidator hasła")
        print("10 - Sprawdzanie numeru rejestracyjnego")
        print("11 - Weryfikacja prędkości na autostradzie")
        print("12 - Ekstrakcja danych pracownika")
        print("13 - Formatowanie numeru telefonu")
        print("14 - Kod SWIFT/BIC Extractor")
        print("15 - Zamiana zmiennych")
        print("16 - Symulator rzutu kością (vs. komputer)")
        print("17 - Suma trzech rzutów kośćmi")
        print("18 - Konwersja systemów liczbowych")
        print("19 - Tłumacz kodów znaków")
        print("20 - Ukryte słowo")
        print("0  - Powrót")

        wybor = input("Wybierz zadanie: ").strip()

        if wybor == "1":
            # Kalkulator BMI
            try:
                wzrost = int(input("Wzrost (cm): "))
                waga = float(input("Waga (kg): "))
                bmi = waga / (wzrost / 100) ** 2
                print(f"BMI: {bmi:.2f}")
            except (ValueError, ZeroDivisionError):
                print("Błędne dane!")

        elif wybor == "2":
            # Dochód rodzinny
            try:
                ojciec = float(input("Dochód ojca: "))
                matka = float(input("Dochód matki: "))
                osoby = int(input("Liczba członków rodziny: "))
                calkowity = ojciec + matka
                na_osobe = calkowity / osoby
                print(f"Całkowity dochód rodziny: {calkowity:.2f}")
                print(f"Dochód na osobę: {na_osobe:.2f}")
            except (ValueError, ZeroDivisionError):
                print("Błędne dane!")

        elif wybor == "3":
            # Konwersja wzrostu na stopy i cale
            try:
                cm = float(input("Podaj wzrost w cm: "))
                stopy = cm // 30.48
                cale = (cm % 30.48) // 2.54
                print(f"{int(stopy)} stóp {int(cale)} cali")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "4":
            # Dystans do horyzontu
            try:
                h = float(input("Wysokość obserwatora (m): "))
                d = 3.57 * math.sqrt(h)
                print(f"Odległość do horyzontu: {d:.2f} km")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "5":
            # Pole i obwód koła
            try:
                r = float(input("Promień koła: "))
                pole = math.pi * r ** 2
                obwod = 2 * math.pi * r
                print(f"Pole: {pole:.2f}, Obwód: {obwod:.2f}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "6":
            # Kalkulator kosztów transportu
            try:
                dystans = float(input("Dystans (km): "))
                cena = float(input("Cena paliwa za litr: "))
                spalanie = float(input("Spalanie na 100 km: "))
                zuzycie = dystans * spalanie / 100
                koszt = zuzycie * cena
                print(f"Całkowite zużycie paliwa: {zuzycie:.2f} l")
                print(f"Całkowity koszt: {koszt:.2f}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "7":
            # Obliczanie VAT
            try:
                netto = float(input("Kwota netto: "))
                vat = 0.23 * netto
                brutto = netto + vat
                print(f"VAT: {vat:.2f}")
                print(f"Brutto: {brutto:.2f}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "8":
            # Sprawdzanie zwolnienia podatkowego
            try:
                wiek = int(input("Podaj wiek: "))
                zwolnienie = wiek <= 26
                print(f"Zwolnienie podatkowe: {zwolnienie}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "9":
            # Walidator hasła
            haslo = input("Podaj hasło: ")
            poprawne = len(haslo) >= 8
            print(f"Hasło poprawne (min. 8 znaków): {poprawne}")

        elif wybor == "10":
            # Sprawdzanie numeru rejestracyjnego z Krakowa
            nr = input("Numer rejestracyjny: ").upper()
            z_krakowa = nr[:2] == "KR" or nr[:2] == "KK"
            print(f"Rejestracja z Krakowa: {z_krakowa}")

        elif wybor == "11":
            # Weryfikacja prędkości na autostradzie
            try:
                speed = int(input("Podaj prędkość w km/h: "))
                poprawna = speed >= 40 and speed <= 140
                print(poprawna)
            except ValueError:
                print("Błędne dane!")

        elif wybor == "12":
            # Ekstrakcja danych pracownika
            txt = "Mr. John May, born on 1998-02-16"
            print("Tekst źródłowy:", txt)
            imie = txt[4:8].strip()
            nazwisko = txt[9:12].strip()
            inicjaly = imie[0] + nazwisko[0]
            data_urodzenia = txt[-10:]
            print("Imię:", imie)
            print("Nazwisko:", nazwisko)
            print("Inicjały:", inicjaly)
            print("Data urodzenia:", data_urodzenia)

        elif wybor == "13":
            # Formatowanie numeru telefonu
            numer = input("Podaj 9-cyfrowy numer telefonu: ").strip()
            if len(numer) == 9 and numer.isdigit():
                print(f"{numer[:3]}-{numer[3:6]}-{numer[6:]}")
            else:
                print("Błędny numer!")

        elif wybor == "14":
            # Kod SWIFT/BIC Extractor
            swift = input("Podaj 8-znakowy kod SWIFT: ").strip()
            if len(swift) == 8:
                bank = swift[:4]
                kraj = swift[4:6]
                print("Kod banku:", bank)
                print("Kod kraju:", kraj)
            else:
                print("Niepoprawny kod SWIFT! (wymagane dokładnie 8 znaków)")

        elif wybor == "15":
            # Zamiana zmiennych
            x = 7
            y = 34
            print(f"Przed zamianą: x = {x}, y = {y}")
            temp = x
            x = y
            y = temp
            print(f"Po zamianie:   x = {x}, y = {y}")

        elif wybor == "16":
            # Symulator rzutu kością
            try:
                typ = int(input("Twoja próba odgadnięcia (1-6): "))
                kostka = random.randint(1, 6)
                print(f"Wynik kostki: {kostka}")
                print(f"Trafiono: {typ == kostka}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "17":
            # Suma trzech rzutów kośćmi
            rzuty = [random.randint(1, 6) for _ in range(3)]
            suma = sum(rzuty)
            print(f"Rzuty: {rzuty}")
            print(f"Suma: {suma}")

        elif wybor == "18":
            # Konwersja systemów liczbowych
            try:
                liczba = int(input("Podaj liczbę całkowitą: "))
                print(f"Binarnie:        {bin(liczba)[2:]}")
                print(f"Szesnastkowo:    {hex(liczba)[2:].upper()}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "19":
            # Tłumacz kodów znaków
            znaki = input("Podaj znaki: ")
            kody = [ord(c) for c in znaki]
            print(f"Kody znaków: {kody}")

        elif wybor == "20":
            # Ukryte słowo
            try:
                kody = input("Podaj listę kodów znaków, oddzielone przecinkami: ")
                lista = [int(k.strip()) for k in kody.split(",")]
                tekst = "".join([chr(k) for k in lista])
                print(f"Odkodowany tekst: {tekst}")
            except ValueError:
                print("Błędne dane! Podaj liczby oddzielone przecinkami.")

        elif wybor == "0":
            break
        else:
            print("Nieprawidłowy wybór!")


# ==============================
# ===== DZIAŁ 2 – Instrukcje warunkowe ===
# ==============================

def dzial2():
    while True:
        print("\n=== DZIAŁ 2 – Instrukcje warunkowe ===")
        print("1  - Kontrola prędkości pojazdu")
        print("2  - Sprawdzanie parzystości")
        print("3  - Symulacja płatności")
        print("4  - Zaliczenie testu")
        print("5  - Wynagrodzenie z premią")
        print("6  - Opis rozmiaru odzieży")
        print("7  - Prosty kalkulator 4 operacji")
        print("8  - Obliczanie zużycia paliwa")
        print("9  - Określanie kwartału roku")
        print("10 - Klasyfikacja wieku")
        print("11 - Logowanie użytkownika")
        print("12 - Uprawnienie do zniżki")
        print("13 - Czy obie osoby są pełnoletnie")
        print("14 - Sprawdzanie czy liczba nie jest ujemna")
        print("15 - Walidacja kodu EAN-13")
        print("0  - Powrót")

        wybor = input("Wybierz zadanie: ").strip()

        if wybor == "1":
            # Kontrola prędkości pojazdu
            try:
                predkosc = int(input("Podaj prędkość (km/h): "))
                if predkosc > 140:
                    print("Przekroczenie prędkości!")
                else:
                    print("Jazda zgodna z przepisami.")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "2":
            # Sprawdzanie parzystości
            try:
                l = int(input("Podaj liczbę całkowitą: "))
                if l % 2 == 0:
                    print("Liczba parzysta")
                else:
                    print("Liczba nieparzysta")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "3":
            # Symulacja płatności
            try:
                stan = 500
                print(f"Stan konta: {stan} zł")
                kwota = float(input("Kwota zakupów: "))
                if kwota <= stan:
                    print("Płatność zaakceptowana")
                else:
                    print("Brak środków")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "4":
            # Zaliczenie testu
            try:
                poprawne = int(input("Liczba poprawnych odpowiedzi: "))
                wszystkie = int(input("Liczba wszystkich pytań: "))
                procent = poprawne / wszystkie * 100
                print(f"Wynik: {procent:.1f}%")
                if procent >= 50:
                    print("Zaliczone")
                else:
                    print("Nie zaliczone")
            except (ValueError, ZeroDivisionError):
                print("Błędne dane!")

        elif wybor == "5":
            # Wynagrodzenie z premią
            pensja = 5000
            premia = input("Czy pracownik otrzymuje premię? (tak/nie): ").strip().lower()
            if premia == "tak":
                pensja *= 1.15
                print(f"Pensja z premią 15%: {pensja:.2f} zł")
            else:
                print(f"Pensja końcowa: {pensja:.2f} zł")

        elif wybor == "6":
            # Opis rozmiaru odzieży
            rozmiar = input("Podaj rozmiar (S/M/L/XL): ").strip().upper()
            if rozmiar == "S":
                print("Small size")
            elif rozmiar == "M":
                print("Medium size")
            elif rozmiar == "L":
                print("Large size")
            elif rozmiar == "XL":
                print("Extra large size")
            else:
                print("Incorrect symbol")

        elif wybor == "7":
            # Kalkulator czterech operacji
            try:
                a = float(input("Podaj pierwszą liczbę: "))
                b = float(input("Podaj drugą liczbę: "))
                op = input("Podaj operację (+, -, *, /): ").strip()
                if op == "+":
                    print(f"Wynik: {a + b}")
                elif op == "-":
                    print(f"Wynik: {a - b}")
                elif op == "*":
                    print(f"Wynik: {a * b}")
                elif op == "/":
                    if b == 0:
                        print("Błąd: dzielenie przez zero!")
                    else:
                        print(f"Wynik: {a / b}")
                else:
                    print("Błędna operacja!")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "8":
            # Obliczanie zużycia paliwa
            try:
                tryb = input("Tryb jazdy (A=7l/100km / M=9l/100km / E=6l/100km): ").strip().upper()
                if tryb == "A":
                    spalanie = 7
                elif tryb == "M":
                    spalanie = 9
                elif tryb == "E":
                    spalanie = 6
                else:
                    print("Nieznany tryb jazdy!")
                    continue
                dystans = float(input("Dystans (km): "))
                zuzycie = dystans * spalanie / 100
                print(f"Zużycie paliwa: {zuzycie:.2f} l")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "9":
            # Kwartał roku
            try:
                miesiac = int(input("Numer miesiąca (1-12): "))
                if 1 <= miesiac <= 3:
                    print("I kwartał")
                elif 4 <= miesiac <= 6:
                    print("II kwartał")
                elif 7 <= miesiac <= 9:
                    print("III kwartał")
                elif 10 <= miesiac <= 12:
                    print("IV kwartał")
                else:
                    print("Błędny miesiąc! Podaj liczbę od 1 do 12.")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "10":
            # Klasyfikacja wieku
            try:
                wiek = int(input("Podaj wiek: "))
                if wiek < 13:
                    print("Child")
                elif wiek < 20:
                    print("Teen")
                elif wiek < 65:
                    print("Adult")
                else:
                    print("Senior")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "11":
            # Logowanie użytkownika
            login_ok = "admin"
            haslo_ok = "1234"
            l = input("Login: ").strip()
            h = input("Hasło: ").strip()
            if l == login_ok and h == haslo_ok:
                print("Zalogowano poprawnie")
            else:
                print("Błędne dane logowania")

        elif wybor == "12":
            # Uprawnienie do zniżki
            try:
                wiek = int(input("Podaj wiek: "))
                if wiek < 18 or wiek >= 65:
                    print("Przysługuje zniżka")
                else:
                    print("Brak zniżki")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "13":
            # Czy obie osoby są pełnoletnie
            try:
                im1 = input("Imię pierwszej osoby: ").strip()
                w1 = int(input(f"Wiek {im1}: "))
                im2 = input("Imię drugiej osoby: ").strip()
                w2 = int(input(f"Wiek {im2}: "))
                if w1 >= 18 and w2 >= 18:
                    print(f"Obie osoby ({im1} i {im2}) są pełnoletnie.")
                else:
                    print("Przynajmniej jedna osoba jest niepełnoletnia.")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "14":
            # Sprawdzanie czy liczba nie jest ujemna
            try:
                x = int(input("Podaj pierwszą liczbę: "))
                y = int(input("Podaj drugą liczbę: "))
                przynajmniej_jedna_nieujemna = not (x < 0) or not (y < 0)
                if przynajmniej_jedna_nieujemna:
                    print("Przynajmniej jedna liczba nie jest ujemna:", True)
                else:
                    print("Obie liczby są ujemne:", False)
            except ValueError:
                print("Błędne dane!")

        elif wybor == "15":
            # Walidacja kodu EAN-13
            kod = input("Podaj kod EAN-13: ").strip()
            if len(kod) != 13 or not kod.isdigit():
                print("Niepoprawny kod EAN-13 (musi mieć dokładnie 13 cyfr).")
            elif kod[:3] == "590":
                print("Kod poprawny – produkt z Polski (590).")
            else:
                print("Kod poprawny, ale nie pochodzi z Polski.")

        elif wybor == "0":
            break
        else:
            print("Nieprawidłowy wybór!")


# ==============================
# ===== DZIAŁ 3 – Pętle =========
# ==============================

def dzial3():
    while True:
        print("\n=== DZIAŁ 3 – Pętle (for / while) ===")
        print("1  - Liczby od 1 do 10")
        print("2  - Liczby parzyste od 1 do 20 (w jednej linii)")
        print("3  - Suma liczb od 1 do n")
        print("4  - Litery słowa w oddzielnych liniach")
        print("5  - Tabliczka mnożenia 1-5")
        print("6  - Liczenie znaków bez len()")
        print("7  - Średnia z 5 liczb")
        print("8  - Największa z siedmiu liczb")
        print("9  - Sumowanie liczb aż do zera")
        print("10 - Gwiazdkowy wykres poziomy")
        print("11 - Ile razy litera 'a'")
        print("12 - Program zgaduje liczbę użytkownika (1-10)")
        print("0  - Powrót")

        wybor = input("Wybierz zadanie: ").strip()

        if wybor == "1":
            # Liczby od 1 do 10
            for i in range(1, 11):
                print(i)

        elif wybor == "2":
            # Liczby parzyste od 1 do 20 w jednej linii
            for i in range(2, 21, 2):
                print(i, end=" ")
            print()

        elif wybor == "3":
            # Suma od 1 do n
            try:
                n = int(input("Podaj n: "))
                suma = 0
                for i in range(1, n + 1):
                    suma += i
                print(f"Suma liczb od 1 do {n}: {suma}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "4":
            # Litery słowa w oddzielnych liniach
            s = input("Podaj słowo: ")
            for litera in s:
                print(litera)

        elif wybor == "5":
            # Tabliczka mnożenia 1-5
            print("   ", end="")
            for j in range(1, 6):
                print(f"{j:4}", end="")
            print()
            print("   " + "-" * 20)
            for i in range(1, 6):
                print(f"{i} |", end="")
                for j in range(1, 6):
                    print(f"{i * j:4}", end="")
                print()

        elif wybor == "6":
            # Liczenie znaków bez len()
            tekst = input("Podaj tekst: ")
            licznik = 0
            for _ in tekst:
                licznik += 1
            print(f"Liczba znaków: {licznik}")

        elif wybor == "7":
            # Średnia z 5 liczb
            try:
                suma = 0
                for i in range(1, 6):
                    suma += float(input(f"Liczba {i}: "))
                print(f"Średnia: {suma / 5:.2f}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "8":
            # Największa z 7 liczb
            try:
                maxl = None
                for i in range(1, 8):
                    l = int(input(f"Liczba {i}: "))
                    if maxl is None or l > maxl:
                        maxl = l
                print(f"Największa liczba: {maxl}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "9":
            # Sumowanie aż do zera
            try:
                suma = 0
                print("Wpisuj liczby (0 aby zakończyć):")
                while True:
                    l = int(input("Liczba: "))
                    if l == 0:
                        break
                    suma += l
                print(f"Suma: {suma}")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "10":
            # Gwiazdkowy wykres poziomy
            try:
                n = int(input("Podaj n: "))
                print("*" * n)
            except ValueError:
                print("Błędne dane!")

        elif wybor == "11":
            # Ile razy litera 'a'
            tekst = input("Podaj tekst: ")
            licznik = 0
            for znak in tekst:
                if znak.lower() == "a":
                    licznik += 1
            print(f"Litera 'a' wystąpiła: {licznik} raz(y)")

        elif wybor == "12":
            # Komputer zgaduje liczbę użytkownika
            print("Wymyśl liczbę od 1 do 10 i zapamiętaj ją.")
            proby = 0
            while True:
                los = random.randint(1, 10)
                proby += 1
                print(f"Próba {proby}: czy to {los}?")
                odpowiedz = input("Czy to twoja liczba? (tak/nie): ").strip().lower()
                if odpowiedz == "tak":
                    print(f"Zgadłem w {proby} próbach!")
                    break

        elif wybor == "0":
            break
        else:
            print("Nieprawidłowy wybór!")


# ==============================
# ===== DZIAŁ 4 – Funkcje =======
# ==============================

def dzial4():
    while True:
        print("\n=== DZIAŁ 4 – Funkcje ===")
        print("1  - Wbudowane funkcje (max, min, len)")
        print("2  - Definiowanie funkcji i return (evenOdd)")
        print("3  - Funkcje z modułów (math, random)")
        print("4  - Argument domyślny")
        print("5  - Argumenty słowami kluczowymi (keyword arguments)")
        print("6  - Przepływ danych – obiekty zmienne i niezmienne")
        print("7  - Zagnieżdżone funkcje (inner/nested)")
        print("8  - Rekursja (silnia)")
        print("9  - Organizacja kodu w moduły (opis + kod)")
        print("10 - Konstrukcja if __name__ == '__main__'")
        print("0  - Powrót")

        wybor = input("Wybierz zadanie: ").strip()

        if wybor == "1":
            # Wbudowane funkcje
            print("Największa spośród 7,5,6,3,8,2:", max(7, 5, 6, 3, 8, 2))
            print("Najmniejsza spośród 4,7,2,3,9,8:", min(4, 7, 2, 3, 9, 8))
            print("Długość frazy 'computer science':", len("computer science"))

        elif wybor == "2":
            # Even/Odd
            def evenOdd(x):
                if x % 2 == 0:
                    return "Even"
                else:
                    return "Odd"

            print("evenOdd(16):", evenOdd(16))
            print("evenOdd(7):", evenOdd(7))

        elif wybor == "3":
            # math i random
            print(f"math.sqrt(7)  = {math.sqrt(7):.6f}")
            print(f"math.log(5)   = {math.log(5):.6f}")
            print(f"Rzut kostką (random.randint(1,6)): {random.randint(1, 6)}")

        elif wybor == "4":
            # Argument domyślny
            def myFun(x, y=50):
                print(f"x = {x}, y = {y}")

            print("myFun(10)      ->", end=" ")
            myFun(10)
            print("myFun(10, 20)  ->", end=" ")
            myFun(10, 20)

        elif wybor == "5":
            # Keyword arguments
            def student(fname, lname):
                print(fname, lname)

            print("student(fname='Geeks', lname='Practice')  ->", end=" ")
            student(fname="Geeks", lname="Practice")
            print("student(lname='Practice', fname='Geeks')  ->", end=" ")
            student(lname="Practice", fname="Geeks")

        elif wybor == "6":
            # Mutable / Immutable
            def modify_list(lst):
                lst[0] = 20

            def modify_int(x):
                x = 20

            lista = [1, 2, 3]
            print("Lista przed wywołaniem funkcji:", lista)
            modify_list(lista)
            print("Lista po wywołaniu funkcji:    ", lista)
            print("(Lista jest obiektem zmiennym – zmiana jest widoczna na zewnątrz)")
            print()
            a = 10
            print("Zmienna int przed wywołaniem funkcji:", a)
            modify_int(a)
            print("Zmienna int po wywołaniu funkcji:    ", a)
            print("(int jest obiektem niezmiennym – oryginalna wartość nie zmienia się)")

        elif wybor == "7":
            # Zagnieżdżone funkcje
            def outer():
                msg = "Hello"

                def inner():
                    print("Wiadomość z funkcji wewnętrznej:", msg)

                inner()

            outer()

        elif wybor == "8":
            # Rekursja – silnia
            def factorial(n):
                if n == 0:
                    return 1
                return n * factorial(n - 1)

            print(f"4! = {factorial(4)}")
            print(f"5! = {factorial(5)}")

        elif wybor == "9":
            # Moduły
            print("=== Zadanie 9: Organizacja kodu w moduły ===")
            print()
            print("Utwórz plik 'converters.py' z następującą zawartością:")
            print("-" * 50)
            print("""
def cm_to_inches(cm):
    return cm / 2.54

def feet_inches_to_cm(feet, inches):
    return feet * 30.48 + inches * 2.54
""")
            print("-" * 50)
            print("Następnie w głównym pliku programu napisz:")
            print("""
import converters

print(converters.cm_to_inches(180))
print(converters.feet_inches_to_cm(5, 11))
""")
            print("-" * 50)
            print("Demonstracja funkcji (uruchomiona bezpośrednio):")

            def cm_to_inches(cm):
                return cm / 2.54

            def feet_inches_to_cm(feet, inches):
                return feet * 30.48 + inches * 2.54

            try:
                cm = float(input("Podaj centymetry do konwersji na cale: "))
                print(f"{cm} cm = {cm_to_inches(cm):.2f} cali")
                f = int(input("Podaj stopy: "))
                i = int(input("Podaj cale: "))
                print(f"{f} stóp {i} cali = {feet_inches_to_cm(f, i):.2f} cm")
            except ValueError:
                print("Błędne dane!")

        elif wybor == "10":

            def add(a, b):
                return a + b

            def subtract(a, b):
                return a - b

            def main():
                print("Testowanie funkcji add i subtract:")
                print(f"add(5, 3)      = {add(5, 3)}")
                print(f"subtract(5, 3) = {subtract(5, 3)}")

            print("Konstrukcja if __name__ == '__main__': gwarantuje,")
            print("że kod testujący uruchomi się tylko przy bezpośrednim wykonaniu pliku.")
            print()
            main()

        elif wybor == "0":
            break
        else:
            print("Nieprawidłowy wybór!")


# ==============================
# ===== GŁÓWNE MENU ===========
# ==============================

def main():
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║       SYSTEM ZADAŃ PYTHON            ║")
        print("╠══════════════════════════════════════╣")
        print("║  1 - Dział 1: Typy danych            ║")
        print("║  2 - Dział 2: Instrukcje warunkowe   ║")
        print("║  3 - Dział 3: Pętle (for/while)      ║")
        print("║  4 - Dział 4: Funkcje                ║")
        print("║  0 - Wyjście                         ║")
        print("╚══════════════════════════════════════╝")

        dzial = input("Wybierz dział: ").strip()

        if dzial == "1":
            dzial1()
        elif dzial == "2":
            dzial2()
        elif dzial == "3":
            dzial3()
        elif dzial == "4":
            dzial4()
        elif dzial == "0":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór!")


if __name__ == "__main__":
    main()