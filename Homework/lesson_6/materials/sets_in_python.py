# Seturile sunt colectii neordonate de elemente unice. Putem crea un set folosind functia set() sau folosind acoladele {}.
# De exemplu, să creăm un set cu elementele 1, 2, 3 folosind funcția set()

numbers_set = set([1, 2, 3])
# Acum să afișăm setul numbers_set
print(numbers_set)
# Ar trebui să obțineți {1, 2, 3}

# Putem crea același set folosind acoladele {}
numbers_set = {1, 2, 3}
# Acum să afișăm setul numbers_set
print(numbers_set)
# Ar trebui să obțineți {1, 2, 3}

# Seturile nu permit elemente duplicate. Dacă încercați să adăugați un element care există deja în set, acesta nu va fi adăugat
# De exemplu, să adăugăm elementul 1 la setul numbers_set
numbers_set.add(1)
# Acum să afișăm setul numbers_set
print(numbers_set)
# Ar trebui să obțineți {1, 2, 3}

# O metodă utilă pentru seturi este metoda update(), care adaugă elemente dintr-un alt set sau dintr-o altă colecție la setul curent
# De exemplu, să adăugăm elementele 4, 5, 6 la setul numbers_set folosind metoda update()
numbers_set.update({4, 5, 6})
# Acum să afișăm setul numbers_set
print(numbers_set)
# Ar trebui să obțineți {1, 2, 3, 4, 5, 6}

# Putem șterge un element dintr-un set folosind metoda remove()
# De exemplu, să ștergem elementul 1 din setul numbers_set
numbers_set.remove(1)
# Acum să afișăm setul numbers_set
print(numbers_set)
# Ar trebui să obțineți {2, 3, 4, 5, 6}

# Dacă încercați să ștergeți un element care nu există în set, veți obține o eroare
# De exemplu, să încercăm să ștergem elementul 7 din setul numbers_set
numbers_set.remove(7)
# Ar trebui să obțineți KeyError: 7

# Pentru a evita eroarea, puteți folosi metoda discard(), care șterge un element din set dacă acesta există
# Dacă elementul nu există în set, metoda nu va arunca o eroare
# De exemplu, să încercăm să ștergem elementul 7 din setul numbers_set folosind metoda discard()
numbers_set.discard(7)
# Acum să afișăm setul numbers_set
print(numbers_set)
# Ar trebui să obțineți {2, 3, 4, 5, 6}

# Putem șterge un element din set folosind metoda pop(), care va șterge primul element din set
# De exemplu, să ștergem primul element din setul numbers_set
numbers_set.pop()
# Acum să afișăm setul numbers_set
print(numbers_set)
# Ar trebui să obțineți {3, 4, 5, 6}

# Putem verifica dacă un element există într-un set folosind operatorul in
# De exemplu, să verificăm dacă elementul 3 există în setul numbers_set
print(3 in numbers_set)
# Ar trebui să obțineți True

# Putem identifica elementele comune din două seturi folosind metoda intersection()
# De exemplu, să identificăm elementele comune din setul numbers_set și setul {4, 5, 6, 7}
common_elements = numbers_set.intersection({4, 5, 6, 7})
# Acum să afișăm setul common_elements
print(common_elements)
# Ar trebui să obțineți {4, 5, 6}

# Putem identifica elementele unice din două seturi folosind metoda difference()
# De exemplu, să identificăm elementele unice din setul numbers_set și setul {4, 5, 6, 7}
unique_elements = numbers_set.difference({4, 5, 6, 7})
# Acum să afișăm setul unique_elements
print(unique_elements)
# Ar trebui să obțineți {3}

# Putem uni două seturi folosind metoda union()
# De exemplu, să unim setul numbers_set cu setul {7, 8, 9}
union_set = numbers_set.union({7, 8, 9})
# Acum să afișăm setul union_set
print(union_set)
# Ar trebui să obțineți {3, 4, 5, 6, 7, 8, 9}

# Putem verifica dacă un set este submulțimea sau supramulțimea altui set folosind metodele issubset() și issuperset()
# De exemplu, să verificăm dacă setul {4, 5} este submulțimea setului numbers_set
print({4, 5}.issubset(numbers_set))
# Ar trebui să obțineți True

# De asemenea, putem verifica dacă setul numbers_set este supramulțimea setului {4, 5}
print(numbers_set.issuperset({4, 5}))
# Ar trebui să obțineți True

# Putem obține elementele unice unui set compartiv cu alt set folosind metoda symmetric_difference()
# De exemplu, să obținem elementele unice ale setului numbers_set comparativ cu setul {4, 5, 6}
symmetric_difference = numbers_set.symmetric_difference({4, 5, 6})
# Acum să afișăm setul symmetric_difference
print(symmetric_difference)
# Ar trebui să obțineți {3, 7}

# Pentru operațiile cu seturi, putem folosi și operatorii specifici pentru seturi
# Operatorul | reprezintă reuniunea a două seturi
# De exemplu, să calculăm reuniunea setului numbers_set și setul {7, 8, 9}
union_set = numbers_set | {7, 8, 9}
# Acum să afișăm setul union_set
print(union_set)

# Operatorul & reprezintă intersecția a două seturi
# De exemplu, să calculăm intersecția setului numbers_set și setul {4, 5, 6, 7}
common_elements = numbers_set & {4, 5, 6, 7}
# Acum să afișăm setul common_elements
print(common_elements)

# Operatorul - reprezintă diferența a două seturi
# De exemplu, să calculăm diferența setului numbers_set și setul {4, 5, 6, 7}
unique_elements = numbers_set - {4, 5, 6, 7}
# Acum să afișăm setul unique_elements
print(unique_elements)

# Operatorul ^ reprezintă diferența simetrică a două seturi
# De exemplu, să calculăm diferența simetrică a setului numbers_set și setul {4, 5, 6}
symmetric_difference = numbers_set ^ {4, 5, 6}
# Acum să afișăm setul symmetric_difference
print(symmetric_difference)

# Seturile sunt utile pentru a stoca elemente unice și pentru a efectua operații de set pe acestea
# Ele sunt o colecție eficientă pentru a verifica apartenența elementelor la un set și pentru a efectua operații de set

# Asta a fost tot pentru seturi în Python!
