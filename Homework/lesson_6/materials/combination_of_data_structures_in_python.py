# Până acum am vorbit despre o mulțime de tipuri de date diferite în Python, cum ar fi integer, float, boolean, string, list, set și dictionary. 
# În această lecție, vom vorbi despre cum putem combina aceste tipuri de date pentru a crea structuri de date mai complexe.

# Liste de liste
# O modalitate de a combina structurile de date în Python este de a crea liste de liste.
# De exemplu, să creăm o listă de liste care conține numere întregi:
numbers_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Acum să afișăm lista numbers_list
print(numbers_list)
# Ar trebui să obțineți [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Pentru a accesa elementele dintr-o listă de liste, putem folosi indexarea multiplă.
# De exemplu, să afișăm primul element din prima listă din numbers_list:
print(numbers_list[0][0])
# Ar trebui să obțineți 1
# Să afișăm al doilea element din a doua listă din numbers_list:
print(numbers_list[1][1])
# Ar trebui să obțineți 5

# Liste de dicționare
# Putem crea, de asemenea, liste de dicționare în Python.
# De exemplu, să creăm o listă de dicționare care conține informații despre persoane:
people_list = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Alice", "age": 35}
]
# Acum să afișăm lista people_list
print(people_list)
# Ar trebui să obțineți [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}, {'name': 'Alice', 'age': 35}]
# Pentru a accesa elementele dintr-o listă de dicționare, putem folosi indexarea multiplă și cheile dicționarelor.
# De exemplu, să afișăm numele primei persoane din people_list:
print(people_list[0]["name"])
# Ar trebui să obțineți John
# Să afișăm vârsta celei de-a doua persoane din people_list:
print(people_list[1]["age"])
# Ar trebui să obțineți 25

# Dicționare de liste
# Putem crea, de asemenea, dicționare de liste în Python.
# De exemplu, să creăm un dicționar care conține liste de numere întregi:
numbers_dict = {
    "evens": [2, 4, 6, 8, 10],
    "odds": [1, 3, 5, 7, 9]
}
# Acum să afișăm dicționarul numbers_dict
print(numbers_dict)
# Ar trebui să obțineți {'evens': [2, 4, 6, 8, 10], 'odds': [1, 3, 5, 7, 9]}
# Pentru a accesa elementele dintr-un dicționar de liste, putem folosi cheile dicționarului și indexarea listei.
# De exemplu, să afișăm primul număr par din numbers_dict:
print(numbers_dict["evens"][0])
# Ar trebui să obțineți 2
# Să afișăm ultimul număr impar din numbers_dict:
print(numbers_dict["odds"][-1])
# Ar trebui să obțineți 9

# Tuple în dicționare
# Putem crea dicționare care au ca chei tuple în Python.
# De exemplu, să creăm un dicționar care conține tuple ca chei și numere întregi ca valori:
tuple_dict = {
    (1, 2): 3,
    (4, 5): 6,
    (7, 8): 9
}
# Acum să afișăm dicționarul tuple_dict
print(tuple_dict)
# Ar trebui să obțineți {(1, 2): 3, (4, 5): 6, (7, 8): 9}
# Pentru a accesa elementele dintr-un dicționar cu chei de tip tuple, putem folosi cheile tuple.
# De exemplu, să afișăm valoarea asociată cu cheia (4, 5) din tuple_dict:
print(tuple_dict[(4, 5)])
# Ar trebui să obțineți 6

# Seturi de dicționare
# Putem crea seturi de dicționare în Python.
# De exemplu, să creăm un set de dicționare care conține informații despre persoane:
people_set = {
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Alice", "age": 35}
}
# Acum să încercăm să afișăm setul people_set
print(people_set)
# Ar trebui să obțineți un mesaj de eroare de genul:
# TypeError: unhashable type: 'dict'    
# Seturile din Python trebuie să conțină elemente care sunt hashable, ceea ce înseamnă că trebuie să fie imutabile.
# Deoarece dicționarele sunt mutabile, nu pot fi adăugate într-un set.
# Dacă doriți să creați un set de dicționare, puteți folosi tuple-uri în loc de dicționare.

# Seturi de tuple
# Putem crea seturi de tuple în Python.
# De exemplu, să creăm un set de tuple care conține informații despre persoane:
people_set = {
    ("John", 30),
    ("Jane", 25),
    ("Alice", 35)
}
# Acum să afișăm setul people_set
print(people_set)
# Ar trebui să obțineți {('John', 30), ('Jane', 25), ('Alice', 35)}
# Seturile de tuple sunt utile atunci când doriți să creați un set de elemente care sunt imutabile.

# Ideea principală a acestei lecții este că puteți combina diferite tipuri de date în Python pentru a crea structuri de date mai complexe.
# Aceste structuri de date combinate vă pot ajuta să organizați și să manipulați datele într-un mod mai eficient și mai flexibil.

