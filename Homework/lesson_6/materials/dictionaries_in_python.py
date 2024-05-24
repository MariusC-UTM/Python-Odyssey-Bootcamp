# Lecția trecută am învățat despre liste și operațiile pe care le putem face cu acestea. Astăzi vom învăța despre dicționare și operațiile pe care le putem face cu acestea.
# Dictioanarele sunt un alt tip de date în Python care sunt folosite pentru a stoca date. Dicționarele sunt similare cu listele, dar în loc de indexe, dicționarele folosesc chei pentru a accesa valorile.
# Dicționarele sunt definite între acolade {} și conțin perechi de cheie-valoare separate prin virgulă.
# De exemplu, să creăm un dicționar cu câteva perechi de cheie-valoare:

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Acum să afișăm dicționarul person
print(person)
# Ar trebui să obțineți {'name': 'John', 'age': 30, 'city': 'New York'}

# Dicționarele pot conține orice tip de date, inclusiv alte dicționare

nested_dict = {
    "person1": {
        "name": "John",
        "age": 30
    },
    "person2": {
        "name": "Jane",
        "age": 25
    }
}

# Acum să afișăm dicționarul nested_dict
print(nested_dict)
# Ar trebui să obțineți {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Jane', 'age': 25}}

# Dicționarele sunt indexate folosind cheile
# De exemplu, să afișăm valoarea asociată cu cheia "name" din dicționarul person
print(person["name"])
# Ar trebui să obțineți John

# Dacă încercați să accesați o cheie care nu există în dicționar, veți obține o eroare
# De exemplu, să încercăm să afișăm valoarea asociată cu o cheie inexistentă

print(person["macaroni"])
# Ar trebui să obțineți KeyError: 'macaroni'

# Dicționarele sunt mutabile, ceea ce înseamnă că puteți modifica valorile asociate cu cheile
# De exemplu, să modificăm valoarea asociată cu cheia "age" din dicționarul person
person["age"] = 35
# Acum să afișăm dicționarul person
print(person)
# Ar trebui să obțineți {'name': 'John', 'age': 35, 'city': 'New York'}

# Dicționarele pot conține orice tip de date, inclusiv liste
# De exemplu, să creăm un dicționar cu o listă de numere întregi

numbers_dict = {
    "numbers": [1, 2, 3, 4, 5]
}

# Acum să afișăm dicționarul numbers_dict
print(numbers_dict)
# Ar trebui să obțineți {'numbers': [1, 2, 3, 4, 5]}

# Dicționarele au o lungime, care reprezintă numărul de perechi de cheie-valoare din dicționar
# Pentru a obține lungimea unui dicționar, puteți folosi funcția len()
print(len(person))
# Ar trebui să obțineți 3

# Pentru a obține toate cheile dintr-un dicționar, puteți folosi metoda keys()
print(person.keys())
# Ar trebui să obțineți dict_keys(['name', 'age', 'city'])

# Pentru a obține toate valorile dintr-un dicționar, puteți folosi metoda values()
print(person.values())
# Ar trebui să obțineți dict_values(['John', 35, 'New York'])

# Pentru a extrage o valoare dintr-un dicționar și a o șterge, puteți folosi metoda pop()
name = person.pop("name")
# Acum să afișăm valoarea extrasă și dicționarul person fără cheia "name"
print(name)
# Ar trebui să obțineți John
print(person)
# Ar trebui să obțineți {'age': 35, 'city': 'New York'}

# Altă metodă utilă pentru lucrul cu dicționarele este metoda get()
# Metoda get() vă permite să obțineți valoarea asociată cu o cheie dintr-un dicționar, dar nu va arunca o eroare dacă cheia nu există
# În schimb, va returna None

age = person.get("age")
# Acum să afișăm valoarea asociată cu cheia "age" și valoarea asociată cu o cheie inexistentă
print(age)
# Ar trebui să obțineți 35
print(person.get("city"))
# Ar trebui să obțineți New York
print(person.get("macaroni"))
# Ar trebui să obțineți None

# Altă metodă utilă pentru lucrul cu dicționarele este metoda update()
# Metoda update() vă permite să actualizați un dicționar cu perechi de cheie-valoare din alt dicționar
# De exemplu, să actualizăm dicționarul person cu perechile de cheie-valoare din dicționarul numbers_dict
person.update(numbers_dict)
# Acum să afișăm dicționarul person actualizat
print(person)
# Ar trebui să obțineți {'age': 35, 'city': 'New York', 'numbers': [1, 2, 3, 4, 5]} 
# Observați că dicționarul person conține acum și perechile de cheie-valoare din dicționarul numbers_dict

# Putem șterge o cheie dintr-un dicționar folosind cuvântul cheie del
# De exemplu, să ștergem cheia "city" din dicționarul person
del person["city"]
# Acum să afișăm dicționarul person fără cheia "city"
print(person)
# Ar trebui să obțineți {'age': 35, 'numbers': [1, 2, 3, 4, 5]}

# Dicționarele pot conține chei și valori de diferite tipuri
# De exemplu, să creăm un dicționar cu chei și valori de diferite tipuri

mixed_dict = {
    "name": "John",
    15 : 30,
    False: True,
    "grades": [85, 90, 88]
}

# Acum să afișăm dicționarul mixed_dict
print(mixed_dict)
# Ar trebui să obțineți {'name': 'John', 15: 30, False: True, 'grades': [85, 90, 88]}
# Observați că dicționarul mixed_dict conține chei și valori de tipuri diferite

# Altă metodă utilă pentru lucrul cu dicționarele este metoda items()
# Metoda items() vă permite să obțineți o listă de perechi de cheie-valoare dintr-un dicționar
# De exemplu, să obținem o listă de perechi de cheie-valoare din dicționarul mixed_dict
print(mixed_dict.items())
# Ar trebui să obțineți dict_items([('name', 'John'), (15, 30), (False, True), ('grades', [85, 90, 88])])

# Altă metodă utilă pentru lucrul cu dicționarele este metoda clear()
# Metoda clear() șterge toate perechile de cheie-valoare dintr-un dicționar
# De exemplu, să ștergem toate perechile de cheie-valoare din dicționarul mixed_dict
mixed_dict.clear()
# Acum să afișăm dicționarul mixed_dict
print(mixed_dict)
# Ar trebui să obțineți {}

# Metod setdefault() adaugă o cheie cu o valoare implicită în dicționar dacă cheia nu există deja

person = {
    "name": "John",
    "age": 30
}

# De exemplu, să adăugăm cheia "city" cu valoarea "New York" în dicționarul person folosind metoda setdefault()
person.setdefault("city", "New York")
# Acum să afișăm dicționarul person
print(person)
# Ar trebui să obțineți {'name': 'John', 'age': 30, 'city': 'New York'}

# Dacă cheia "city" există deja în dicționarul person, metoda setdefault() nu va face nimic
person.setdefault("city", "Los Angeles")
# Acum să afișăm dicționarul person
print(person)
# Ar trebui să obțineți {'name': 'John', 'age': 30, 'city': 'New York'}

# Metoda setdefault() este utilă atunci când doriți să adăugați o cheie cu o valoare implicită într-un dicționar dacă cheia nu există deja

# Acestea sunt câteva dintre operațiile de bază pe care le puteți face cu dicționarele în Python. Dicționarele sunt un instrument puternic pentru stocarea și manipularea datelor în Python și sunt folosite frecvent în programele Python.