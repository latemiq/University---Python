import re
import random
from functools import reduce

# ─────────────────────────────────────────────
#  ROZWIĄZANIA — REGEX
# ─────────────────────────────────────────────

def regex_1():
    """Walidacja kodów produktów (PROD-XXXX)"""
    tekst = "Zamówienia: PROD-1234, PROD-9999, PROD-12, PROD-ABCD"
    wyniki = re.findall(r'PROD-\d{4}', tekst)
    print(f"Tekst: {tekst}")
    print(f"Poprawne kody: {wyniki}")

def regex_2():
    """Ekstrakcja cen (liczba + spacja + 'zł')"""
    tekst = "Produkty kosztują: 10 zł, 99 zł, 5zl, 100 zł"
    wyniki = re.findall(r'\d+ zł', tekst)
    print(f"Tekst: {tekst}")
    print(f"Poprawne ceny: {wyniki}")

def regex_3():
    """Analiza logów (INFO, ERROR, WARNING)"""
    tekst = "INFO Start systemu\nERROR Brak pliku\nWARNING Niski poziom baterii\nDEBUG Dane testowe"
    wyniki = re.findall(r'INFO|ERROR|WARNING', tekst)
    print(f"Tekst:\n{tekst}")
    print(f"\nZnalezione poziomy: {wyniki}")

def regex_4():
    """Wyszukiwanie dat w formacie DD-MM-YYYY"""
    tekst = "Daty: 01-12-2023, 1-1-2020, 31-01-2022"
    wyniki = re.findall(r'\d{2}-\d{2}-\d{4}', tekst)
    print(f"Tekst: {tekst}")
    print(f"Poprawne daty: {wyniki}")

def regex_5():
    """Hashtagi"""
    tekst = "Post: #python #AI #data_science #123"
    wyniki = re.findall(r'#\w+', tekst)
    print(f"Tekst: {tekst}")
    print(f"Hashtagi: {wyniki}")

def regex_6():
    """ID użytkownika (user_ + cyfry)"""
    tekst = "user_123 user_abc user_456 admin_789"
    wyniki = re.findall(r'user_\d+', tekst)
    print(f"Tekst: {tekst}")
    print(f"Poprawne ID: {wyniki}")

def regex_7():
    """Zdania zaczynające się wielką literą"""
    tekst = "ala ma kota. Ala ma psa. kot śpi. Pies biega."
    wyniki = re.findall(r'[A-Z][^.]+\.', tekst)
    print(f"Tekst: {tekst}")
    print(f"Zdania z wielką literą: {wyniki}")

def regex_8():
    """Długie słowa (min. 5 znaków)"""
    tekst = "To jest przykładowe zdanie testowe programowanie"
    wyniki = re.findall(r'\b\w{5,}\b', tekst)
    print(f"Tekst: {tekst}")
    print(f"Słowa ≥5 znaków: {wyniki}")

def regex_9():
    """Podwójne litery"""
    tekst = "anna kot pies letter book moon"
    wyniki = re.findall(r'\b\w*(.)\1\w*\b', tekst)
    slowa = re.findall(r'\b\w*(.)\1\w*\b', tekst)
    # Lepiej — zwróćmy całe słowa
    slowa = [s for s in tekst.split() if re.search(r'(.)\1', s)]
    print(f"Tekst: {tekst}")
    print(f"Słowa z podwójnymi literami: {slowa}")

def regex_10():
    """Wersje oprogramowania (v + cyfry + . + cyfry)"""
    tekst = "Wersje: v1.0, v2.10, v10.5, version1.2"
    wyniki = re.findall(r'v\d+\.\d+', tekst)
    print(f"Tekst: {tekst}")
    print(f"Poprawne wersje: {wyniki}")

def regex_11():
    """HTML — tagi otwierające"""
    tekst = "<div><p>Hello</p><a href=\"#\">Link</a></div>"
    wyniki = re.findall(r'<\w+[^>]*>', tekst)
    print(f"Tekst: {tekst}")
    print(f"Tagi otwierające: {wyniki}")

def regex_12():
    """Numery telefonu (3-3-3 cyfry)"""
    tekst = "Kontakt: 123-456-789, 12-123-123, 987-654-321"
    wyniki = re.findall(r'\d{3}-\d{3}-\d{3}', tekst)
    print(f"Tekst: {tekst}")
    print(f"Poprawne numery: {wyniki}")

def regex_13():
    """Czyszczenie tekstu — znaki specjalne → spacje"""
    tekst = "Hello!!! Python@@2025 ##AI"
    wynik = re.sub(r'[^\w\s]', ' ', tekst)
    print(f"Tekst przed: {tekst}")
    print(f"Tekst po:    {wynik}")

def regex_14():
    """Zmiana formatu daty DD-MM-YYYY → YYYY/MM/DD"""
    tekst = "Data: 01-12-2023"
    wynik = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3/\2/\1', tekst)
    print(f"Tekst przed: {tekst}")
    print(f"Tekst po:    {wynik}")

def regex_15():
    """Imiona i nazwiska → lista krotek"""
    tekst = "Jan Kowalski, Anna Nowak, Piotr Zieliński"
    wyniki = re.findall(r'([A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]+)\s([A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]+)', tekst)
    print(f"Tekst: {tekst}")
    print(f"Krotki: {wyniki}")

# ─────────────────────────────────────────────
#  ROZWIĄZANIA — FUNKCJE WYŻSZEGO RZĘDU
# ─────────────────────────────────────────────

def wyzsze_1():
    """Funkcja jako argument"""
    def operacja(f, x):
        return f(x)

    def potroj(x):
        return x * 3

    wynik = operacja(potroj, 7)
    print(f"operacja(potroj, 7) = {wynik}")

def wyzsze_2():
    """Funkcje jako obiekty — lista funkcji"""
    def powitanie():
        print("Witaj w Pythonie")

    def pozegnanie():
        print("Do widzenia!")

    alias = powitanie
    lista_funkcji = [alias, pozegnanie]

    for f in lista_funkcji:
        f()

def wyzsze_3():
    """Przekazywanie funkcji — formatuj(tekst, funkcja)"""
    def formatuj(tekst, funkcja):
        return funkcja(tekst)

    def male_litery(t):
        return t.lower()

    def odwroc(t):
        return t[::-1]

    print(f"male_litery: {formatuj('Python', male_litery)}")
    print(f"odwroc:      {formatuj('Python', odwroc)}")

def wyzsze_4():
    """Funkcja zwracająca funkcję — mnożnik"""
    def stworz_mnoznik(n):
        def mnoz(x):
            return x * n
        return mnoz

    podwoj = stworz_mnoznik(2)
    potroj = stworz_mnoznik(3)

    print(f"podwoj(10) = {podwoj(10)}")
    print(f"potroj(10) = {potroj(10)}")

def wyzsze_5():
    """Lambda i map — kwadraty"""
    liczby = [2, 4, 6, 8]
    kwadraty = list(map(lambda x: x ** 2, liczby))
    print(f"Lista:    {liczby}")
    print(f"Kwadraty: {kwadraty}")

def wyzsze_6():
    """filter — liczby > 10"""
    lista = [3, 8, 11, 14, 18, 21]
    wynik = list(filter(lambda x: x > 10, lista))
    print(f"Lista:        {lista}")
    print(f"Większe od 10: {wynik}")

def wyzsze_7():
    """reduce — iloczyn"""
    lista = [1, 2, 3, 4, 5]
    iloczyn = reduce(lambda a, b: a * b, lista)
    print(f"Lista:   {lista}")
    print(f"Iloczyn: {iloczyn}")

def wyzsze_8():
    """sorted z key — według długości słów"""
    slowa = ["kot", "samochód", "dom", "programowanie", "pies"]
    posortowane = sorted(slowa, key=len)
    print(f"Przed: {slowa}")
    print(f"Po:    {posortowane}")

# ─────────────────────────────────────────────
#  DANE MENU
# ─────────────────────────────────────────────

LISTA_REGEX = [
    (1,  "Walidacja kodów produktów",          regex_1),
    (2,  "Ekstrakcja cen",                      regex_2),
    (3,  "Analiza logów",                       regex_3),
    (4,  "Wyszukiwanie dat DD-MM-YYYY",         regex_4),
    (5,  "Hashtagi",                            regex_5),
    (6,  "ID użytkownika",                      regex_6),
    (7,  "Zdania z wielką literą",              regex_7),
    (8,  "Długie słowa (min. 5 znaków)",        regex_8),
    (9,  "Podwójne litery",                     regex_9),
    (10, "Wersje oprogramowania",               regex_10),
    (11, "HTML tagi otwierające",               regex_11),
    (12, "Numery telefonu 3-3-3",               regex_12),
    (13, "Czyszczenie tekstu",                  regex_13),
    (14, "Zmiana formatu daty",                 regex_14),
    (15, "Imiona i nazwiska → krotki",          regex_15),
]

LISTA_WYZSZE = [
    (1, "Funkcja jako argument",                wyzsze_1),
    (2, "Funkcje jako obiekty",                 wyzsze_2),
    (3, "Przekazywanie funkcji",                wyzsze_3),
    (4, "Funkcja zwracająca funkcję",           wyzsze_4),
    (5, "Lambda i map",                         wyzsze_5),
    (6, "filter",                               wyzsze_6),
    (7, "reduce — iloczyn",                     wyzsze_7),
    (8, "sorted z key",                         wyzsze_8),
]

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

SEP = "─" * 50

def drukuj_liste(lista, nazwa):
    print(f"\n{'═'*50}")
    print(f"  {nazwa}")
    print(f"{'═'*50}")
    for nr, opis, _ in lista:
        print(f"  {nr:>2}. {opis}")
    print(SEP)

def uruchom_zadanie(lista, wybor):
    for nr, opis, fn in lista:
        if nr == wybor:
            print(f"\n{SEP}")
            print(f"  Zadanie {nr}: {opis}")
            print(SEP)
            fn()
            print(SEP)
            return
    print("  ⚠ Nie ma takiego numeru zadania.")

def podmenu(lista, nazwa):
    while True:
        drukuj_liste(lista, nazwa)
        print("  [0] Wróć do głównego menu")
        print("  [L] Losuj zadanie")
        wybor = input("\n  Twój wybór: ").strip().upper()

        if wybor == "0":
            break
        elif wybor == "L":
            nr, opis, fn = random.choice(lista)
            print(f"\n{SEP}")
            print(f"  🎲 Wylosowane: zadanie {nr} — {opis}")
            print(SEP)
            fn()
            print(SEP)
            input("  [Enter] aby kontynuować...")
        else:
            try:
                uruchom_zadanie(lista, int(wybor))
                input("  [Enter] aby kontynuować...")
            except ValueError:
                print("  ⚠ Podaj numer lub L.")

# ─────────────────────────────────────────────
#  GŁÓWNA PĘTLA
# ─────────────────────────────────────────────

def main():
    print("\n" + "═"*50)
    print("  ZADANIA PYTHON — interaktywne menu")
    print("═"*50)

    while True:
        print(f"\n{SEP}")
        print("  Wybierz listę zadań:")
        print("  [1] Regex (15 zadań)")
        print("  [2] Funkcje wyższego rzędu (8 zadań)")
        print("  [0] Wyjście")
        print(SEP)

        wybor = input("  Twój wybór: ").strip()

        if wybor == "1":
            podmenu(LISTA_REGEX, "ZADANIA — REGEX")
        elif wybor == "2":
            podmenu(LISTA_WYZSZE, "ZADANIA — FUNKCJE WYŻSZEGO RZĘDU")
        elif wybor == "0":
            print("\n  Do widzenia! 👋\n")
            break
        else:
            print("  ⚠ Wpisz 1, 2 lub 0.")

if __name__ == "__main__":
    main()
