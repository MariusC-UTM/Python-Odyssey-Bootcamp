# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
print('Lista:', numbers)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
print('Numerele pare din lista:')
for i in numbers:
    if i % 2 == 0:
        print(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
print('While loop:')
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {'Name': 'John',
          'Age': 30,
          'City': 'New York'}
for i, p in enumerate(person.items()):
    print(f'[{i}]: {p[0]} - {p[1]}')
print('or')
for key, value in person.items():
    print(key, value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrice = []
for i in range(1, len(numbers) - 4):
    matrice.append(numbers[0:5])
print('Matrice:')
# for row in matrice:
#     print(f"Rândul: {row}")
#     for num in row:
#         print(f"Număr: {num}")
# or
for i, row in enumerate(matrice):
    # print(f'Row [{i}]: {row}')
    for j, col in enumerate(row):
        print(f'[{i}][{j}]: {col} | ', end='')
    print('')
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
print('Lista 2:')
numbers2 = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers2.append(i)
for i in numbers2:
    print(f'Nr. {i}')
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
print('Lista 3:')
numbers3 = []
for i in range(1, 11):
    if i % 2 == 0 or i % 3 == 0:
        numbers3.append(i)
for i, num in enumerate(numbers3):
    print(f'Nr. {i} este {num}')
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
print('Zip:')
for i, num in enumerate(zip(numbers2, numbers3)):
    print(f'[{i}] - {num}')
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
print('Lista:', numbers)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
# num = 0
# while num <= 50:
#     for i, n in enumerate(numbers):
#         numbers[i] *= 2
#     num = numbers[0]
#     print(f'Lista: {numbers}')
# or
# while numbers[0] <= 50:
#     for i, n in enumerate(numbers):
#         numbers[i] *= 2
#     print(f'Lista: {numbers}')
# or
while numbers and numbers[0] <= 50:
    numbers = [n * 2 for n in numbers]
    print(f'Lista dublata: {numbers}')
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
# i = 1
# max_num = i * i
# pp = []
# while 0 < max_num < 101:
#     pp.append(max_num)
#     i += 1
#     max_num = i * i
# or
pp = []
num = 1
while 0 < num * num < 101:
    pp.append(num * num)
    num += 1
print(f'Lista patrate perfecte: {pp}')
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for, printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1, 11):
    print('7 x', i, '=', 7 * i)

# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
# lst = []
# for i in range(1, 6):
#     sublst = []
#     for j in range(1, 6):
#         sublst.append([i, j])
#     lst.append(sublst.copy())
# print(f'Subliste:')
# for sub in lst:
#     print(sub)
# or
pairs = [[[i, j] for j in range(1, 6)] for i in range(1, 6)]
for sublist in pairs:
    print(sublist)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j.

# CODUL TĂU VINE MAI JOS:
for sublist in pairs:
    for pair in sublist:
        if pair[0] < pair[1]:
            print(f'{pair} ', end = '')
        else:
            print(f'{[0, 0]} ', end = '')
    print('')
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
import random
# lst = []
# for i in range(10):
#     lst.append(random.randint(1, 15))
lst = [random.randint(1, 15) for _ in range(10)]
print(f'Lista cu valori aleatoare: {lst}')

n = 0
i = 0
while i < len(lst):
    num = lst[i]
    if num > 10:
        n = num
        break
    i += 1

if n:
    print(f'Prima valoare mai mare ca 10: {n} pe pozitia {i}.')
else:
    print('Nu exista valori mai mari decat 10.')
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
dim = 0
while dim == 0:
    # dim = input('Introduceti marimea patratului: ')
    dim = 5  # this is done temporarily in order to work without disruptions on the next tasks
    try:
        dim = int(dim)
    except:
        dim = 0

for _ in range(dim):
    for _ in range(dim):
        print('*', end = '')
    print()
print('or')
s = ''
for _ in range(dim):
    for _ in range(dim):
        s += '*'
    s += '\n'
print(s)
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
print('Afisare 1:')
# using numbers and math
i = 1
while len(str(i)) < 7:
    print(str(i))
    i = int(((i + 0.0) + (i % 10 / 10 + 0.1)) * 10)
print('or')
# using strings
string = ''
for i in range(1, 7):
    string += str(i)
    print(string)
print('or')
# using strings with nested loops
for i in range(1, 7):
    string = ''
    for j in range(1, i + 1):
        string += str(j)
    print(string)
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
print('Afisare 2:')
# using numbers and math
i = 54321
while i > 0:
    print(str(i))
    i = i // 10
print('or')
# using strings
string = '54321'
for i in range(len(string), 0, -1):
    print(string[:i])
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
string = ''.join([chr(c) for c in range(ord('a'), ord('g')+1)])
print(string)
for i in range(1, len(string)):
    string = ''.join([chr(c) for c in range(ord('a') + i, ord('g') + 1)])
    print(string)
    i += 1

# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(1, 9):
    string4 = ''
    for j in range(1, 17):
        if (i + j) % 2 == 0:
            string4 += '+'
        else:
            string4 += '-'
    print(string4)
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 6):
    numbers.append(3 ** i)
    print(' '.join(map(str, numbers)))

for i in range(1, 5):
    print(' '.join(map(str, numbers[i:])))
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
