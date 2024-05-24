# Mai tot timpul avem nevoie de input de la utilizator. Pentru a obține input de la utilizator în Python, putem folosi funcția `input`.

# Să obținem input de la utilizator
name = input('Introdu numele tău: ')
# Să afișăm numele
print(name)
# Acum, când rulați acest cod, veți vedea un mesaj care vă cere să introduceți numele. După ce introduceți numele și apăsați Enter, numele va fi afișat.

# Funcția `input` întotdeauna returnează un șir de caractere. Dacă doriți să obțineți un alt tip de date, trebuie să convertiți input-ul.
# Funcția `input` poate primi un argument opțional care reprezintă un mesaj pe care îl afișează utilizatorului.
# Să obținem input de la utilizator și să-l convertim într-un număr întreg

# Să obținem input de la utilizator
number = input('Introdu un număr: ')
# Să afișăm tipul lui number
print(type(number))
# Ar trebui să obțineți <class 'str'>
# Acum, când rulați acest cod, veți vedea un mesaj care vă cere să introduceți un număr. După ce introduceți numărul și apăsați Enter, tipul lui number va fi afișat ca fiind un șir de caractere.

# Să convertim number într-un număr întreg
number = int(number)
# Să afișăm tipul lui number
print(type(number))
# Ar trebui să obțineți <class 'int'>

# Asta a fost tot pentru această lecție