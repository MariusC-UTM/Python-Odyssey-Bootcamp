# Acum vom vorbi despre tuple și operațiile pe care le puteți face cu ele
# Un tuple este o colecție ordonată și neindexată de elemente, care pot fi de orice tip de date
# Un tuple este definit între paranteze rotunde () și elementele sunt separate prin virgulă
# De exemplu, să creăm un tuple cu câteva numere întregi:
numbers = (1, 2, 3, 4, 5)
# Acum să afișăm tuple numbers
print(numbers)
# Ar trebui să obțineți (1, 2, 3, 4, 5)

# Dacă doriți să creați un tuple gol, puteți face asta în felul următor:
empty_tuple = ()
# Acum să afișăm tuple empty_tuple
print(empty_tuple)
# Ar trebui să obțineți ()

# Un tuple poate conține orice tip de date, inclusiv de tipuri diferite
mixed_tuple = (1, 2.0, "three", True)
# Acum să afișăm tuple mixed_tuple
print(mixed_tuple)
# Ar trebui să obțineți (1, 2.0, 'three', True)

# La fel ca și listele, tuple-urile pot conține orice tip de date, inclusiv alte tuple-uri
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# Acum să afișăm tuple nested_tuple
print(nested_tuple)
# Ar trebui să obțineți ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Tuple-urile sunt indexate, ceea ce înseamnă că puteți accesa elementele dintr-un tuple folosind un index
# Indexele în Python încep de la 0
# De exemplu, să afișăm primul element din tuple numbers
print(numbers[0])
# Ar trebui să obțineți 1
# Să afișăm al doilea element din tuple numbers
print(numbers[1])
# Ar trebui să obțineți 2
# Să afișăm ultimul element din tuple numbers
print(numbers[-1])
# Ar trebui să obțineți 5

# Indexarea este similară cu cea a listelor, deci puteți folosi aceleași metode pentru a accesa elementele dintr-un tuple

# Un alt element comun la liste și tuple este tăierea
# Tăierea vă permite să accesați o secțiune dintr-un tuple
# De exemplu, să afișăm primele două elemente din tuple numbers
print(numbers[:2])
# Ar trebui să obțineți (1, 2)
# Să afișăm ultimele două elemente din tuple numbers
print(numbers[-2:])
# Ar trebui să obțineți (4, 5)

# Tuple-urile sunt imutabile, ceea ce înseamnă că nu puteți modifica elementele dintr-un tuple
# De exemplu, să încercăm să modificăm primul element din tuple numbers
numbers[0] = 10
# Ar trebui să obțineți un mesaj de eroare de genul:
# TypeError: 'tuple' object does not support item assignment

# Dacă doriți să modificați un tuple, trebuie să transformați tuple-ul într-o listă, să modificați lista și apoi să transformați lista înapoi într-un tuple
# De exemplu, să transformăm tuple numbers într-o listă
numbers_list = list(numbers)
# Acum să modificăm primul element din numbers_list
numbers_list[0] = 10
# Acum să transformăm numbers_list înapoi într-un tuple
numbers = tuple(numbers_list)
# Acum să afișăm tuple numbers
print(numbers)
# Ar trebui să obțineți (10, 2, 3, 4, 5)

# Pentru a adăuga elemente la un tuple, puteți folosi operatorul +
# De exemplu, să adăugăm numărul 6 la tuple numbers
numbers = numbers + (6,)
# Acum să afișăm tuple numbers
print(numbers)
# Ar trebui să obțineți (10, 2, 3, 4, 5, 6)

# Pentru a calcula suma elementelor dintr-un tuple, puteți folosi funcția sum()
# De exemplu, să calculăm suma elementelor din tuple numbers
print(sum(numbers))
# Ar trebui să obțineți 30

# Pentru a șterge un tuple, puteți folosi instrucțiunea del
# De exemplu, să ștergem tuple numbers
del numbers
# Acum să încercăm să afișăm tuple numbers
print(numbers)
# Ar trebui să obțineți un mesaj de eroare de genul:
# NameError: name 'numbers' is not defined

# Tuple-urile au o lungime, care reprezintă numărul de elemente din tuple
# Pentru a obține lungimea unui tuple, puteți folosi funcția len()
# De exemplu, să obținem lungimea tuple-ului numbers
print(len(numbers))
# Ar trebui să obțineți 5

# Aceasta a fost lecția despre tuple și operațiile pe care le puteți face cu ele