# La această lecție vom învăța despre loops în Python sau bucle.
# Loops sunt folosite pentru a executa un bloc de cod de mai multe ori.
# Python are două tipuri de loops: for loop și while loop.

# For loop este utilizat pentru a itera peste o secvență (care poate fi o listă, un tuple, un dicționar, un set sau un string).

# De exemplu, să iterăm printr-o listă:

for i in [1, 2, 3, 4, 5]:
    print(i)
# Aceasta va afișa numerele de la 1 la 5.
# În cazul dat i este o variabilă care ia valoarea fiecărui element din lista pe rând.
# Blocul de cod care urmează după for este executat pentru fiecare element din listă.

# While loop execută un bloc de cod atât timp cât o condiție este adevărată.

# De exemplu:

i = 1
while i <= 5:
    print(i)
    i += 1
# Aceasta va afișa, de asemenea, numerele de la 1 la 5.

# Putem folosi loops și pentru a itera prin dicționare. Când iterăm printr-un dicționar, putem itera prin chei, valori sau ambele.

# De exemplu, să iterăm prin cheile unui dicționar:

person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)
# Aceasta va afișa cheile: name, age și city.

# Pentru a itera prin valorile dicționarului, folosim .values():

for value in person.values():
    print(value)
# Aceasta va afișa valorile: John, 30, New York.

# Putem itera prin perechile de cheie-valoare ale unui dicționar folosind .items():

for key, value in person.items():
    print(key, value)
# Aceasta va afișa perechile de cheie-valoare.

# Buclele pot fi, de asemenea, îmbricate, ceea ce înseamnă că o buclă poate fi plasată în interiorul altei bucle.

# De exemplu, să iterăm printr-o listă de liste:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    print(f"Rândul: {row}")
    for num in row:
        print(f"Număr: {num}")
# Aceasta va afișa fiecare rând și fiecare număr din matrice.

# Folosind bucle, putem executa operații complexe, cum ar fi căutarea de elemente în structuri de date complexe sau aplicarea de logici specifice.

# De exemplu, să căutăm un număr în matrice și să afișăm poziția sa:

num_to_find = 5
for i, row in enumerate(matrix):
    if num_to_find in row:
        print(f"Numărul {num_to_find} găsit la rândul {i}")
        break

# Loops pot fi controlate cu ajutorul instrucțiunilor break și continue.
# Break întrerupe bucla, iar continue trece la următoarea iterație a buclei.

# De exemplu, să afișăm numerele până la 5 folosind break:

for i in range(10):
    if i > 5:
        break
    print(i)

# Continuăm să afișăm numere, dar sărim peste 5 folosind continue:

for i in range(10):
    if i == 5:
        continue
    print(i)

# Buclele pot fi combinate cu instrucțiunile condiționale pentru a crea logici de programare mai complexe.

# De exemplu, să afișăm doar numerele pare dintr-o listă:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)

# În rezumat, buclele sunt un instrument esențial în programare, care ne permit să automatizăm și să repetăm sarcini într-un mod eficient.

# Până acum am folosit funcția range() pentru a genera o secvență de numere.
# range() este o funcție încorporată în Python care generează o secvență de numere întregi.
# Aceasta poate fi folosită în for loops pentru a itera printr-o secvență de numere.
# Dacă vom încerca să afișăm range(5), vom obține doar un obiect range:
    
print(range(5))
# putem să-l convertim într-o listă pentru a vedea numerele:
print(list(range(5)))
# Funcția range() poate primi și un argument de pornire și unul de oprire, precum și un pas.
# De exemplu, range(1, 10, 2) va genera numerele de la 1 la 10 cu un pas de 2:
print(list(range(1, 10, 2)))
# Aceasta va genera [1, 3, 5, 7, 9].
# Dacă nu specificăm un pas, acesta va fi implicit 1.
# Dacă nu specificăm un argument de pornire, acesta va fi implicit 0.
# De exemplu, range(5) este echivalent cu range(0, 5, 1).

# Altă funcție încorporată utilă în Python este enumerate().
# Enumerate() este folosită pentru a itera printr-o secvență împreună cu un index, care începe de la 0.
# De exemplu:

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# Aceasta va afișa indexul și valoarea fiecărui element din listă.
# Enumerate() este utilă atunci când avem nevoie de indexul elementelor în timpul iterației.

# Altă funcție utilă este zip().
# Zip() este folosită pentru a combina două sau mai multe secvențe într-o singură secvență.
# De exemplu:
    
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
# Aceasta va afișa perechile de nume și vârstă.
# Zip() se oprește atunci când cea mai scurtă secvență se termină.
# Dacă secvențele au lungimi diferite, zip() va opri la cea mai scurtă secvență.

