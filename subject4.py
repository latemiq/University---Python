import os
import csv
import json
import struct
import random
import urllib.request
import urllib.error

# ─────────────────────────────────────────────
#  LISTA 1 – Obsługa plików tekstowych
# ─────────────────────────────────────────────

def lista1_zadanie1():
    """Utwórz plik notatka.txt i zapisz trzy linie, potem odczytaj."""
    with open("notatka.txt", "w", encoding="utf-8") as f:
        f.write("To jest pierwsza linia tekstu.\n")
        f.write("Druga linia zawiera trochę więcej słów niż pierwsza.\n")
        f.write("Trzecia i ostatnia linia notatki.\n")
    print("✔ Zapisano plik notatka.txt")
    print("\nZawartość pliku:")
    with open("notatka.txt", "r", encoding="utf-8") as f:
        print(f.read())


def lista1_zadanie2():
    """Policz znaki bez spacji w pliku tekstowym."""
    if not os.path.exists("notatka.txt"):
        print("⚠ Plik notatka.txt nie istnieje. Uruchom najpierw Zadanie 1.")
        return
    with open("notatka.txt", "r", encoding="utf-8") as f:
        text = f.read()
    count = sum(1 for c in text if c != " ")
    print(f"Liczba znaków bez spacji: {count}")


def lista1_zadanie3():
    """Wyświetl linie dłuższe niż 20 znaków."""
    if not os.path.exists("notatka.txt"):
        print("⚠ Plik notatka.txt nie istnieje. Uruchom najpierw Zadanie 1.")
        return
    print("Linie dłuższe niż 20 znaków:")
    with open("notatka.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            stripped = line.rstrip("\n")
            if len(stripped) > 20:
                print(f"  [{i}] {stripped}")


def lista1_zadanie4():
    """Dopisz nowe dane do pliku bez nadpisywania."""
    if not os.path.exists("notatka.txt"):
        print("⚠ Plik notatka.txt nie istnieje. Uruchom najpierw Zadanie 1.")
        return
    nowe_dane = ["Dopisana linia A", "Dopisana linia B", "Dopisana linia C"]
    with open("notatka.txt", "a", encoding="utf-8") as f:
        for d in nowe_dane:
            f.write(d + "\n")
    print("✔ Dopisano nowe dane.")
    print("\nAktualna zawartość pliku:")
    with open("notatka.txt", "r", encoding="utf-8") as f:
        print(f.read())


def lista1_zadanie5():
    """Otwórz plik – obsłuż błąd jeśli nie istnieje."""
    nazwa = input("Podaj nazwę pliku do odczytu: ").strip()
    try:
        with open(nazwa, "r", encoding="utf-8") as f:
            print(f"\nZawartość pliku '{nazwa}':")
            print(f.read())
    except FileNotFoundError:
        print(f"❌ Błąd: plik '{nazwa}' nie istnieje.")


def lista1_zadanie6():
    """Wczytaj plik i zapisz jego zawartość WIELKIMI LITERAMI do nowego pliku."""
    if not os.path.exists("notatka.txt"):
        print("⚠ Plik notatka.txt nie istnieje. Uruchom najpierw Zadanie 1.")
        return
    with open("notatka.txt", "r", encoding="utf-8") as f:
        content = f.read()
    with open("notatka_upper.txt", "w", encoding="utf-8") as f:
        f.write(content.upper())
    print("✔ Zapisano plik notatka_upper.txt (wielkie litery).")
    print("\nZawartość:")
    with open("notatka_upper.txt", "r", encoding="utf-8") as f:
        print(f.read())


def lista1_zadanie7():
    """Sprawdź czy dane.txt istnieje – usuń lub poinformuj."""
    if os.path.exists("dane.txt"):
        os.remove("dane.txt")
        print("✔ Plik dane.txt istniał i został usunięty.")
    else:
        print("ℹ Plik dane.txt nie istnieje.")


def lista1_zadanie8():
    """Program rejestrujący wyniki studentów."""
    PLIK = "studenci.txt"

    def dodaj_studenta():
        imie = input("  Imię: ").strip()
        nazwisko = input("  Nazwisko: ").strip()
        try:
            wynik = float(input("  Wynik: ").strip())
        except ValueError:
            print("  ❌ Nieprawidłowy wynik.")
            return
        with open(PLIK, "a", encoding="utf-8") as f:
            f.write(f"{imie},{nazwisko},{wynik}\n")
        print(f"  ✔ Dodano studenta {imie} {nazwisko}.")

    def wyswietl_studentow():
        try:
            with open(PLIK, "r", encoding="utf-8") as f:
                linie = f.readlines()
            if not linie:
                print("  Brak studentów w pliku.")
                return
            print(f"\n  {'Imię':<12} {'Nazwisko':<15} {'Wynik':>6}")
            print("  " + "-" * 35)
            for linia in linie:
                czesc = linia.strip().split(",")
                if len(czesc) == 3:
                    print(f"  {czesc[0]:<12} {czesc[1]:<15} {czesc[2]:>6}")
        except FileNotFoundError:
            print("  Brak pliku studenci.txt – nie ma jeszcze żadnych danych.")

    def sredni_wynik():
        try:
            with open(PLIK, "r", encoding="utf-8") as f:
                linie = f.readlines()
            wyniki = []
            for linia in linie:
                czesc = linia.strip().split(",")
                if len(czesc) == 3:
                    try:
                        wyniki.append(float(czesc[2]))
                    except ValueError:
                        pass
            if wyniki:
                print(f"  Średni wynik: {sum(wyniki)/len(wyniki):.2f}")
            else:
                print("  Brak danych do obliczenia średniej.")
        except FileNotFoundError:
            print("  Brak pliku studenci.txt.")

    while True:
        print("\n  [1] Dodaj studenta  [2] Wyświetl studentów  [3] Średni wynik  [0] Powrót")
        wybor = input("  > ").strip()
        if wybor == "1":
            dodaj_studenta()
        elif wybor == "2":
            wyswietl_studentow()
        elif wybor == "3":
            sredni_wynik()
        elif wybor == "0":
            break
        else:
            print("  Nieznana opcja.")


# ─────────────────────────────────────────────
#  LISTA 2 – CSV / JSON / Binary
# ─────────────────────────────────────────────

def lista2_zadanie1():
    """Utwórz plik students.csv z danymi."""
    wiersze = [
        ["name", "age", "grade"],
        ["Anna", 21, 4.5],
        ["Jan", 22, 3.8],
        ["Ola", 20, 5.0],
    ]
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(wiersze)
    print("✔ Plik students.csv został utworzony.")
    with open("students.csv", "r", encoding="utf-8") as f:
        print(f.read())


def lista2_zadanie2():
    """Dodaj dwóch nowych studentów do students.csv."""
    if not os.path.exists("students.csv"):
        print("⚠ Plik students.csv nie istnieje. Uruchom najpierw Zadanie 1.")
        return
    nowi = [["Piotr", 23, 4.2], ["Maria", 21, 4.7]]
    with open("students.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(nowi)
    print("✔ Dodano Piotr i Maria.")
    with open("students.csv", "r", encoding="utf-8") as f:
        print(f.read())


def lista2_zadanie3():
    """Wczytaj students.csv, wyświetl studentów i oblicz średnią."""
    if not os.path.exists("students.csv"):
        print("⚠ Plik students.csv nie istnieje. Uruchom najpierw Zadanie 1.")
        return
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        studenci = list(reader)
    print(f"\n{'Imię':<10} {'Wiek':>5} {'Ocena':>7}")
    print("-" * 25)
    oceny = []
    for s in studenci:
        print(f"{s['name']:<10} {s['age']:>5} {s['grade']:>7}")
        try:
            oceny.append(float(s['grade']))
        except ValueError:
            pass
    if oceny:
        print(f"\nŚrednia ocena: {sum(oceny)/len(oceny):.2f}")


def lista2_zadanie4():
    """Zapisz do top_students.csv studentów z oceną ≥ 4.5."""
    if not os.path.exists("students.csv"):
        print("⚠ Plik students.csv nie istnieje. Uruchom najpierw Zadanie 1.")
        return
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        top = [s for s in reader if float(s['grade']) >= 4.5]
    with open("top_students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "grade"])
        writer.writeheader()
        writer.writerows(top)
    print(f"✔ Zapisano {len(top)} studentów do top_students.csv:")
    for s in top:
        print(f"  {s['name']}, ocena: {s['grade']}")


def _pobierz_fakt():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read().decode())
    except urllib.error.URLError as e:
        print(f"❌ Błąd połączenia z API: {e}")
        return None


def lista2_zadanie5():
    """Pobierz jeden losowy fakt i zapisz do fact.json."""
    print("Łączenie z API...")
    fakt = _pobierz_fakt()
    if fakt is None:
        return
    with open("fact.json", "w", encoding="utf-8") as f:
        json.dump(fakt, f, indent=2, ensure_ascii=False)
    print("✔ Zapisano fact.json")
    print(f"  Fakt: {fakt.get('text', '')}")


def lista2_zadanie6():
    """Pobierz 5 faktów i zapisz jako listę do facts.json."""
    print("Pobieranie 5 faktów z API...")
    fakty = []
    for i in range(5):
        print(f"  [{i+1}/5]", end=" ", flush=True)
        fakt = _pobierz_fakt()
        if fakt:
            fakty.append(fakt)
            print("✔")
        else:
            print("✗")
    with open("facts.json", "w", encoding="utf-8") as f:
        json.dump(fakty, f, indent=2, ensure_ascii=False)
    print(f"\n✔ Zapisano {len(fakty)} faktów do facts.json")


def lista2_zadanie7():
    """Wczytaj facts.json i wyświetl id oraz text każdego faktu."""
    if not os.path.exists("facts.json"):
        print("⚠ Plik facts.json nie istnieje. Uruchom najpierw Zadanie 6.")
        return
    with open("facts.json", "r", encoding="utf-8") as f:
        fakty = json.load(f)
    for i, fakt in enumerate(fakty, 1):
        print(f"\n[{i}] ID: {fakt.get('id', 'brak')}")
        print(f"    {fakt.get('text', 'brak')}")


def lista2_zadanie8():
    """Zapisz liczby [10,20,30,40,50] do pliku binarnego."""
    liczby = [10, 20, 30, 40, 50]
    with open("numbers.bin", "wb") as f:
        for n in liczby:
            f.write(struct.pack("i", n))
    print(f"✔ Zapisano {liczby} do numbers.bin")


def lista2_zadanie9():
    """Odczytaj numbers.bin i wyświetl liczby, sumę i średnią."""
    if not os.path.exists("numbers.bin"):
        print("⚠ Plik numbers.bin nie istnieje. Uruchom najpierw Zadanie 8.")
        return
    liczby = []
    with open("numbers.bin", "rb") as f:
        while True:
            bajty = f.read(4)
            if not bajty:
                break
            liczby.append(struct.unpack("i", bajty)[0])
    print(f"Liczby:  {liczby}")
    print(f"Suma:    {sum(liczby)}")
    print(f"Średnia: {sum(liczby)/len(liczby):.2f}")


# ─────────────────────────────────────────────
#  MENU GŁÓWNE
# ─────────────────────────────────────────────

LISTA1 = {
    "1": ("Utwórz plik notatka.txt",            lista1_zadanie1),
    "2": ("Policz znaki bez spacji",             lista1_zadanie2),
    "3": ("Wyświetl linie > 20 znaków",          lista1_zadanie3),
    "4": ("Dopisz dane do pliku",                lista1_zadanie4),
    "5": ("Obsługa błędu – plik nie istnieje",   lista1_zadanie5),
    "6": ("Kopiuj plik WIELKIMI LITERAMI",        lista1_zadanie6),
    "7": ("Sprawdź i usuń dane.txt",             lista1_zadanie7),
    "8": ("Program rejestrujący studentów",      lista1_zadanie8),
}

LISTA2 = {
    "1": ("Utwórz students.csv",                 lista2_zadanie1),
    "2": ("Dodaj nowych studentów do CSV",       lista2_zadanie2),
    "3": ("Odczytaj CSV i oblicz średnią",       lista2_zadanie3),
    "4": ("Filtruj top_students.csv (≥4.5)",     lista2_zadanie4),
    "5": ("Pobierz jeden fakt z API",            lista2_zadanie5),
    "6": ("Pobierz 5 faktów z API",              lista2_zadanie6),
    "7": ("Odczytaj facts.json",                 lista2_zadanie7),
    "8": ("Zapisz liczby do pliku binarnego",    lista2_zadanie8),
    "9": ("Odczytaj plik binarny",               lista2_zadanie9),
}


def pokaz_menu_listy(lista, numer_listy):
    print(f"\n{'═'*42}")
    print(f"  LISTA {numer_listy}")
    print(f"{'═'*42}")
    for k, (nazwa, _) in lista.items():
        print(f"  [{k}] {nazwa}")
    print(f"  [R] Losowe zadanie z tej listy")
    print(f"  [0] Powrót")
    print(f"{'─'*42}")


def uruchom_zadanie(lista, klucz):
    if klucz in lista:
        nazwa, fn = lista[klucz]
        print(f"\n{'─'*42}")
        print(f"  ▶ Zadanie {klucz}: {nazwa}")
        print(f"{'─'*42}")
        fn()
        print(f"{'─'*42}")
        input("  [Enter] aby kontynuować...")
    else:
        print("  ❌ Nieznane zadanie.")


def menu_listy(lista, numer_listy):
    while True:
        pokaz_menu_listy(lista, numer_listy)
        wybor = input("  Wybierz zadanie: ").strip().upper()
        if wybor == "0":
            break
        elif wybor == "R":
            klucz = random.choice(list(lista.keys()))
            print(f"\n  🎲 Wylosowano zadanie {klucz}: {lista[klucz][0]}")
            uruchom_zadanie(lista, klucz)
        else:
            uruchom_zadanie(lista, wybor)


def glowne_menu():
    while True:
        print(f"\n{'═'*42}")
        print("  ZADANIA – OBSŁUGA PLIKÓW W PYTHONIE")
        print(f"{'═'*42}")
        print("  [1] Lista 1 – Pliki tekstowe")
        print("  [2] Lista 2 – CSV / JSON / Binary")
        print("  [R] Losowe zadanie z obu list")
        print("  [0] Wyjście")
        print(f"{'─'*42}")
        wybor = input("  Wybierz: ").strip().upper()

        if wybor == "1":
            menu_listy(LISTA1, 1)
        elif wybor == "2":
            menu_listy(LISTA2, 2)
        elif wybor == "R":
            wszystkie = [(k, v, 1) for k, v in LISTA1.items()] + \
                        [(k, v, 2) for k, v in LISTA2.items()]
            klucz, (nazwa, fn), numer = random.choice(wszystkie)
            print(f"\n  🎲 Wylosowano: Lista {numer}, Zadanie {klucz}: {nazwa}")
            print(f"{'─'*42}")
            fn()
            print(f"{'─'*42}")
            input("  [Enter] aby kontynuować...")
        elif wybor == "0":
            print("\n  Do zobaczenia! 👋")
            break
        else:
            print("  ❌ Nieznana opcja.")


if __name__ == "__main__":
    glowne_menu()