# Orice obiect are un anumit tip. În Python, tipul unui obiect este important deoarece determină ce metode și operații pot fi aplicate pe acel obiect.
# În Python, tipurile de bază despre care am vorbit până acum sunt:
# - int (numere întregi)
# - float (numere reale)
# - str (șiruri de caractere)
# - bool (valori de adevăr sau fals)

# În Python, putem converti un obiect de un anumit tip într-un alt tip folosind funcțiile predefinite de conversie.

# Să convertim un număr întreg într-un număr real
int_number = 10
float_number = float(int_number)
print(float_number)
# Ar trebui să obțineți 10.0

# Să convertim un număr real într-un număr întreg
float_number = 10.5
int_number = int(float_number)
print(int_number)
# Ar trebui să obțineți 10

# Să convertim un număr întreg într-un șir de caractere
int_number = 10
str_number = str(int_number)
print(str_number)
# Ar trebui să obțineți 10

# Să convertim un număr real într-un șir de caractere
float_number = 10.5
str_number = str(float_number)
print(str_number)
# Ar trebui să obțineți 10.5

# Să convertim un șir de caractere într-un număr întreg
str_number = '10'
int_number = int(str_number)
print(int_number)
# Ar trebui să obțineți 10

# Să convertim un șir de caractere într-un număr real
str_number = '10.5'
float_number = float(str_number)
print(float_number)
# Ar trebui să obțineți 10.5

# Conversia pentru variabilele de tip bool este puțin diferită. În Python, orice valoare diferită de 0, None, False sau un șir de caractere gol este considerată adevărată.
# Să convertim un număr întreg într-o valoare de adevăr
int_number = 10
bool_number = bool(int_number)
print(bool_number)
# Ar trebui să obțineți True

# Să convertim un număr real într-o valoare de adevăr
float_number = 10.5
bool_number = bool(float_number)
print(bool_number)
# Ar trebui să obțineți True

# Să convertim un șir de caractere într-o valoare de adevăr
str_number = '10'
bool_number = bool(str_number)
print(bool_number)
# Ar trebui să obțineți True

# Să convertim un șir de caractere gol într-o valoare de adevăr
str_number = ''
bool_number = bool(str_number)
print(bool_number)
# Ar trebui să obțineți False

# Să convertim un șir de caractere într-o valoare de adevăr
str_number = 'False'
bool_number = bool(str_number)
print(bool_number)
# Ar trebui să obțineți True

# Să convertim un șir de caractere într-o valoare de adevăr
str_number = '0'
bool_number = bool(str_number)
print(bool_number)
# Ar trebui să obțineți True

# Vom obține False la conversia numerelor 0 și 0.0 în valori de adevăr
# Să convertim numărul 0 într-o valoare de adevăr
int_number = 0
bool_number = bool(int_number)
print(bool_number)
# Ar trebui să obțineți False

# Să convertim numărul 0.0 într-o valoare de adevăr
float_number = 0.0
bool_number = bool(float_number)
print(bool_number)
# Ar trebui să obțineți False

# Să convertim valoarea None într-o valoare de adevăr
none_value = None
bool_number = bool(none_value)
print(bool_number)
# Ar trebui să obțineți False

# Asta a fost tot pentru această lecție. În următoarea lecție vom tipuri de date mai complexe, cum ar fi liste, tuple și dicționare.