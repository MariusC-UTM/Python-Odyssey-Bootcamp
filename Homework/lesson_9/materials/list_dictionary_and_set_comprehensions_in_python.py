# La această lecție vom învăța despre list comprehensions în Python.
# List comprehensions sunt o metodă concisă și eficientă de a crea liste în Python.

# Structura de bază a unei list comprehension este:
# [expr for item in iterable if condition]

# De exemplu, să creăm o listă cu pătratele numerelor de la 1 la 5 folosind list comprehension:
squares = [i**2 for i in range(1, 6)]
print(squares)
# Aceasta va afișa: [1, 4, 9, 16, 25]

# Putem adăuga și condiții în list comprehension pentru a filtra elementele.

# De exemplu, să creăm o listă cu numerele pare de la 1 la 10:

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)
# Aceasta va afișa: [2, 4, 6, 8, 10]

# List comprehensions pot fi folosite și pentru a itera prin structuri de date complexe, cum ar fi listele de liste.

# De exemplu, să aplatizăm o listă de liste într-o singură listă:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)
# Aceasta va afișa: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehensions pot include structuri condiționale complexe, cum ar fi condiții multiple și blocuri if-else.

# De exemplu, să creăm o listă care conține "mic" pentru numerele mai mici decât 5, "mare" pentru numerele mai mari sau egale cu 5 și mai mici decât 10:

size = ["mic" if num < 5 else "mare" for num in range(1, 10)]
print(size)
# Aceasta va afișa: ['mic', 'mic', 'mic', 'mic', 'mare', 'mare', 'mare', 'mare', 'mare']

# List comprehensions nu sunt limitate doar la liste. Ele pot fi folosite pentru a crea și alte tipuri de structuri de date, cum ar fi dicționare sau seturi.

# De exemplu, să creăm un dicționar care mappează numerele de la 1 la 5 la pătratele lor:

squares_dict = {i: i**2 for i in range(1, 6)}
print(squares_dict)
# Aceasta va afișa: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Similar, putem crea un set care conține pătratele numerelor de la 1 la 5:

squares_set = {i**2 for i in range(1, 6)}
print(squares_set)
# Aceasta va afișa: {1, 4, 9, 16, 25}

# În concluzie, list comprehensions sunt un mod puternic și expresiv de a genera structuri de date în Python.
# Ele permit crearea de liste, dicționare și seturi într-un mod concis și clar, reducând nevoia de bucle for explicite și facilitând citirea codului.



