# Aceasta este a doua sarcină legată de tuples

# Creează un tuple numit `numbers` care să conțină numerele de la 1 la 5

# CODUL TĂU VINE MAI JOS:
numbers = tuple(range(1, 6))
# or
# numbers = (1, 2, 3, 4, 5)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la tuple `numbers`

# CODUL TĂU VINE MAI JOS:
numbers += (6,)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Afișeați primul element din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[0])
# CODUL TĂU VINE MAI SUS:   

# Afișeați ultimul element din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[-1])
# CODUL TĂU VINE MAI SUS:

# Afișeați primele două elemente din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[:2])
# CODUL TĂU VINE MAI SUS:

# Afișeați ultimele două elemente din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers[-2:])
# or
# print(numbers[len(numbers)-2:len(numbers)])
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(len(numbers))
# CODUL TĂU VINE MAI SUS:

# Afișați suma elementelor din tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(sum(numbers))
# CODUL TĂU VINE MAI SUS:

# Schibați elementul de la poziția 2 din tuple `numbers` cu 10

# CODUL TĂU VINE MAI JOS:
numbers = numbers[:2] + (10,) + numbers[3:]
# or
# numbers = tuple(10 if i == 2 else num for i, num in enumerate(numbers))
# or
# numbers = list(numbers)
# numbers[2] = 10
# numbers = tuple(numbers)
# CODUL TĂU VINE MAI SUS:

# Afișați tuple `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Ștergeți tuple `numbers`

# CODUL TĂU VINE MAI JOS:
del numbers
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste
