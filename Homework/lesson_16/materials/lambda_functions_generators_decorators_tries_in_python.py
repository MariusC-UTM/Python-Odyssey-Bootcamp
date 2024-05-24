# La această lecție, vom explora în detaliu conceptele de funcții lambda, generatori, decoratori și gestionarea excepțiilor în Python, oferind câte trei exemple pentru fiecare.

# Funcții Lambda
# Funcțiile lambda sunt funcții anonime exprimate printr-o singură linie de cod, utilizate pentru operații simple și filtrări.

# Exemplu 1: Calcularea pătratului unui număr
patrat = lambda x: x * x
print(patrat(4))  # 16

# Exemplu 2: Adunarea a două numere
adunare = lambda x, y: x + y
print(adunare(5, 3))  # 8

# Exemplu 3: Filtrarea numerelor pare dintr-o listă
numere = [1, 2, 3, 4, 5]
pare = list(filter(lambda x: x % 2 == 0, numere))
print(pare)  # [2, 4]

# Generatori
# Generatorii sunt funcții care produc o secvență de rezultate pe parcurs, utilizând cuvântul cheie yield.

# Exemplu 1: Generator care returnează numerele până la un limită
def numere_pana_la(n):
    for i in range(n):
        yield i

for numar in numere_pana_la(3):
    print(numar)  # 0, 1, 2

# Exemplu 2: Generator care produce pătratele numerelor
def patrate(n):
    for i in range(1, n + 1):
        yield i * i

print(list(patrate(3)))  # [1, 4, 9]

# Exemplu 3: Generator infinit
def numere_infinite():
    i = 0
    while True:
        yield i
        i += 1

# Decoratori
# Decoratorii sunt funcții care modifică comportamentul altor funcții, adăugând funcționalități înainte și după funcția decorată.

# Exemplu 1: Decorator care afișează timpul de execuție
import time

def timp_executie(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rezultat = func(*args, **kwargs)
        end = time.time()
        print(f"Timp executie: {end - start} secunde")
        return rezultat
    return wrapper

@timp_executie
def suma(a, b):
    return a + b

print(suma(5, 7))

# Exemplu 2: Decorator care afișează un mesaj înainte și după apelul unei funcții
def mesaj(func):
    def wrapper(*args, **kwargs):
        print("Începe funcția")
        rezultat = func(*args, **kwargs)
        print("Termină funcția")
        return rezultat
    return wrapper

@mesaj
def saluta(nume):
    print(f"Salut, {nume}!")

saluta("Ana")

# Exemplu 3: Decorator care convertește rezultatul funcției în majuscule
def uppercase(func):
    def wrapper():
        rezultat = func()
        return rezultat.upper()
    return wrapper

@uppercase
def mesaj():
    return 'salut lume'

print(mesaj())

# Gestionarea excepțiilor
# Gestionarea excepțiilor se face prin blocurile try și except, permițând capturarea și tratarea erorilor.

# Exemplu 1: Capturarea unei erori de împărțire prin zero
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Nu se poate împărți la zero.")

# Exemplu 2: Capturarea și tratarea mai multor tipuri de erori
try:
    x = int('a')
except ValueError:
    print("Conversie nereușită.")
except Exception as e:
    print(f"Eroare necunoscută: {e}")

# Exemplu 3: Utilizarea else și finally în gestionarea excepțiilor
try:
    print("Totul merge bine.")
except Exception as e:
    print(f"Eroare: {e}")
else:
    print("Blocul try a rulat fără erori.")
finally:
    print("Acest bloc se execută întotdeauna.")

# În concluzie, înțelegerea funcțiilor lambda, generatorilor, decoratorilor, și gestionarea excepțiilor
# este crucială pentru scrierea de cod Python eficient, modular și rezistent la erori.
