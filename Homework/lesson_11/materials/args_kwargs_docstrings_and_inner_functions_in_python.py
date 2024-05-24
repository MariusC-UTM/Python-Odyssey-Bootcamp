# La această lecție vom explora avansat conceptele *args, **kwargs, docstrings și funcții interne în Python.

# *args - permite pasarea unui număr variabil de argumente poziționale la o funcție.
def sumare(*numere):
    suma = 0
    for numar in numere:
        suma += numar
    return suma

print(sumare(5, 10, 15))  # Aceasta va afișa: 30

# **kwargs - permite pasarea unui număr variabil de argumente de tip cheie-valoare (or basically un dicționar) la o funcție.
def descriere_obiect(**caracteristici):
    for cheie, valoare in caracteristici.items():
        print(f"{cheie} este {valoare}")

descriere_obiect(culoare="albastru", greutate="20 kg", forma="rotund")
# Aceasta va afișa:
# culoare este albastru
# greutate este 20 kg
# forma este rotund

# Docstrings - oferă o descriere a funcției, parametrilor săi, comportamentului și valorii returnate.
def impartire(a, b):
    """
    Împarte primul argument prin al doilea și returnează rezultatul.
    
    Parameters:
        a (int/float): Numărătorul.
        b (int/float): Numitorul, trebuie să fie diferit de zero.

    Return:
        float: Rezultatul împărțirii a și b.

    Raise:
        ZeroDivisionError: dacă b este zero.
    """
    if b == 0:
        raise ZeroDivisionError("Numitorul nu poate fi zero.")
    return a / b

# Google docstring style
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""

# Numpydoc docstring style
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""

# reST docstring style
"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""

print(impartire(10, 2))  # Aceasta va afișa: 5.0

# Funcții interne - funcții definite în interiorul altor funcții, utile pentru încapsularea logicii.
def proceseaza_date(n):
    def patrat(x):
        return x * x

    def cub(x):
        return x * x * x

    return patrat(n), cub(n)

print(proceseaza_date(3))  # Aceasta va afișa: (9, 27)

# Funcțiile interne pot fi folosite pentru a crea închideri (closures), care sunt funcții dinamice generatoare de funcții.
def multiplicator(factor):
    def inmulteste_cu_factor(n):
        return n * factor
    return inmulteste_cu_factor

dublare = multiplicator(2)
triplare = multiplicator(3)

print(dublare(5))  # Aceasta va afișa: 10
print(triplare(5))  # Aceasta va afișa: 15

# În concluzie, funcțiile în Python pot fi extrem de flexibile și puternice, permițând manipularea avansată a argumentelor,
# documentarea clară prin docstrings și structurarea codului prin utilizarea funcțiilor interne.
