# La această lecție vom învăța despre funcții în Python.
# Funcțiile sunt blocuri de cod reutilizabile care sunt executate când sunt apelate.

# O funcție simplă care nu primește argumente și nu returnează valori:
def salutare():
    print("Salut!")

salutare()
# Aceasta va afișa: Salut!

# Funcțiile pot primi argumente, care sunt valori transmise funcției la apelare.

# De exemplu, o funcție care primește un nume și afișează un mesaj:
def salut_nume(nume):
    print(f"Salut, {nume}!")

salut_nume("Ana")
# Aceasta va afișa: Salut, Ana!

# Argumentele pot fi și de tip keyword, permițând specificarea lor prin nume, nu doar prin poziție.

# De exemplu, o funcție care primește nume și vârstă ca argumente:
def afiseaza_informatii(nume, varsta):
    print(f"Nume: {nume}, Varsta: {varsta}")

afiseaza_informatii(varsta=30, nume="Ion")
# Aceasta va afișa: Nume: Ion, Varsta: 30

# Funcțiile pot avea argumente implicite (default), care iau o valoare predefinită dacă nu sunt specificate la apel.

# De exemplu, o funcție care salută și are un mesaj implicit:
def salut(mesaj="Salutare!"):
    print(mesaj)

salut()
# Aceasta va afișa: Salutare!
salut("Bună ziua!")
# Aceasta va afișa: Bună ziua!

# O funcție care realizează o operațiune matematică și returnează rezultatul:
def adunare(a, b):
    return a + b

rezultat = adunare(5, 3)
print(rezultat)
# Aceasta va afișa: 8

# Funcțiile pot efectua orice tip de calcul sau logică, nu doar operațiuni matematice simple.

# De exemplu, o funcție care calculează factorialul unui număr:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# Aceasta va afișa: 120

# Funcțiile pot returna mai multe valori folosind tuple.

# De exemplu, o funcție care returnează suma și produsul a două numere:
def calculeaza_suma_si_produs(a, b):
    suma = a + b
    produs = a * b
    return suma, produs  # returnează un tuple

suma, produs = calculeaza_suma_si_produs(3, 4)
print(f"Suma: {suma}, Produs: {produs}")
# Aceasta va afișa: Suma: 7, Produs: 12

# Funcțiile pot interacționa cu diferite tipuri de date și structuri.

# De exemplu, o funcție care inversează un string și verifică dacă este un palindrom:
def este_palindrom(s):
    invers = s[::-1]
    return invers == s, invers  # returnează un tuple cu două valori: boolean și string

palindrom, invers = este_palindrom("radar")
print(f"Invers: {invers}, Palindrom: {palindrom}")
# Aceasta va afișa: Invers: radar, Palindrom: True

# În concluzie, funcțiile în Python sunt instrumente flexibile care pot fi personalizate cu ajutorul argumentelor poziționale, 
# argumentelor de tip keyword și argumentelor implicite, facilitând scrierea de cod modular și reutilizabil.
