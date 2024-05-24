# Lecțiile precedente am vorbit despre variabilele de bază precum ar fi integer, float, boolean și string. În această lecție vom vorbi despre listele din Python și operațiile pe care le puteți face cu ele.
# Listele sunt o colecție de elemente ordonate și pot conține orice tip de date. Listele sunt definite între paranteze drepte [] și elementele sunt separate prin virgulă.
# De exemplu, să creăm o listă cu câteva numere întregi:

numbers = [1, 2, 3, 4, 5]

# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [1, 2, 3, 4, 5]
# Dacă doriți să creați o listă goală, puteți face asta în felul următor:
empty_list = []
# Acum să afișăm lista empty_list
print(empty_list)
# Ar trebui să obțineți []

# Listele pot conține orice tip de date, inclusiv de tipuri diferite
mixed_list = [1, 2.0, "three", True]
# Acum să afișăm lista mixed_list
print(mixed_list)
# Ar trebui să obțineți [1, 2.0, 'three', True]

# Doar pentru că puteți adăuga orice tip de date într-o listă, nu înseamnă că ar trebui să o faceți
# Este recomandat să folosiți listele pentru a stoca elemente de același tip de date, dar dacă aveți nevoie să stocați elemente de tipuri diferite, puteți face asta

# Reamintim că listele pot conține orice tip de date, inclusiv alte liste
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Acum să afișăm lista nested_list
print(nested_list)
# Ar trebui să obțineți [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Listele sunt indexate, ceea ce înseamnă că puteți accesa elementele dintr-o listă folosind un index
# Indexele în Python încep de la 0
# De exemplu, să afișăm primul element din lista numbers
print(numbers[0])
# Ar trebui să obțineți 1
# Să afișăm al doilea element din lista numbers
print(numbers[1])
# Ar trebui să obțineți 2
# Să afișăm ultimul element din lista numbers
print(numbers[-1])
# Ar trebui să obțineți 5

# Indexarea este similară cu cea a string-urilor, deci puteți folosi aceleași metode pentru a accesa elementele dintr-o listă

# Un alt element comun la string-uri și liste este tăierea
# Tăierea vă permite să accesați o secțiune dintr-o listă
# De exemplu, să afișăm primele două elemente din lista numbers
print(numbers[:2])
# Ar trebui să obțineți [1, 2]
# Să afișăm ultimele două elemente din lista numbers
print(numbers[-2:])
# Ar trebui să obțineți [4, 5]

# Listele sunt mutabile, ceea ce înseamnă că puteți modifica elementele dintr-o listă
# De exemplu, să modificăm primul element din lista numbers
numbers[0] = 10
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [10, 2, 3, 4, 5]

# Listele au o lungime, care reprezintă numărul de elemente din listă
# Pentru a obține lungimea unei liste, puteți folosi funcția len()
# De exemplu, să obținem lungimea listei numbers
print(len(numbers))
# Ar trebui să obțineți 5

# Listele au multe metode utile pe care le puteți folosi pentru a efectua diferite operațiuni
# De exemplu, să adăugăm un element la lista numbers
numbers.append(6)
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [10, 2, 3, 4, 5, 6]
# Funcția append() adaugă un element la sfârșitul listei

# De asemenea, puteți adăuga un element la o anumită poziție în listă folosind metoda insert()
# De exemplu, să adăugăm elementul 7 la poziția 2 în lista numbers
numbers.insert(2, 7)
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [10, 2, 7, 3, 4, 5, 6]
# Elementele de la poziția 2 înainte sunt mutate cu o poziție înainte pentru a face loc noului element

# Puteți șterge un element dintr-o listă folosind metoda remove()
# De exemplu, să ștergem elementul 7 din lista numbers
numbers.remove(7)
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [10, 2, 3, 4, 5, 6]

# Dacă doriți să ștergeți un element de la o anumită poziție din listă, puteți folosi cuvântul cheie del
# De exemplu, să ștergem elementul de la poziția 2 din lista numbers
del numbers[2]
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [10, 2, 4, 5, 6]

# Puteți sorta o listă folosind metoda sort()
# De exemplu, să sortăm lista numbers
numbers.sort()
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [2, 4, 5, 6, 10]

# Puteți inversa ordinea elementelor dintr-o listă folosind metoda reverse()
# De exemplu, să inversăm ordinea listei numbers
numbers.reverse()
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [10, 6, 5, 4, 2]

# Altă modalitate de a inversa ordinea elementelor dintr-o listă este de a folosi indexarea cu pași negativi
# De exemplu, să inversăm ordinea listei numbers folosind indexarea cu pași negativi
print(numbers[::-1])
# Ar trebui să obțineți [2, 4, 5, 6, 10]
# Aceeastă metodă este aplicabilă și la string-uri

# Listele pot fi concatenate folosind operatorul +
# De exemplu, să concatenăm lista numbers cu lista [1, 2, 3]
concatenated_list = numbers + [1, 2, 3]
# Acum să afișăm lista concatenated_list
print(concatenated_list)
# Ar trebui să obțineți [10, 6, 5, 4, 2, 1, 2, 3]

# Listele pot fi repetate folosind operatorul *
# De exemplu, să repetăm lista numbers de 3 ori
repeated_list = numbers * 3
# Acum să afișăm lista repeated_list
print(repeated_list)
# Ar trebui să obțineți [10, 6, 5, 4, 2, 10, 6, 5, 4, 2, 10, 6, 5, 4, 2]

# Pentru a adăuga elemente putem folosi și funcția extend()
# De exemplu, să adăugăm lista [1, 2, 3] la lista numbers
numbers.extend([1, 2, 3])
# Acum să afișăm lista numbers
print(numbers)
# Ar trebui să obțineți [10, 6, 5, 4, 2, 1, 2, 3]

# Listele pot fi convertite în string-uri folosind funcția str()
# De exemplu, să convertim lista numbers într-un string
numbers_string = str(numbers)
# Acum să afișăm string-ul numbers_string
print(numbers_string)
# Ar trebui să obțineți '[10, 6, 5, 4, 2]'
# String-ul rezultat conține lista numbers sub formă de string

# Aceasta a fost lecția despre listele din Python și operațiile pe care le puteți face cu ele
