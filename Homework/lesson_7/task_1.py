# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 6
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
    print('Numar pozitiv.')
else:
    print('Numar negativ sau 0.')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
    print('Numar par.')
else:
    print('Numar impar sau 0.')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 != 0:
    print('Numar impar.')
else:
    print('Numar par sau 0.')
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = 'Text in Python.'
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.find('Python') > -1:
    print(f'Cuvantul \'Python\' se afla in textul \'{text}\'.')
else:
    print(f'Cuvantul \'Python\' nu se afla in textul \'{text}\'.')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.find('Jave') > -1:
    print(f'Cuvantul \'Java\' se afla in textul \'{text}\'.')
else:
    print(f'Cuvantul \'Java\' nu se afla in textul \'{text}\'.')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.find('Python') > -1:
    print(f'Cuvantul \'Python\' se afla in textul \'{text}\'.')
elif text.find('Java') > -1:
    print(f'Cuvantul \'Java\' se afla in textul \'{text}\'.')
else:
    print(f'Cuvantul \'Python\' si cuvantul \'Java\' nu se afla in textul \'{text}\'.')
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.find('Python') > -1 and text.find('Jave') > -1:
    print(f'Cuvantul \'Python\' si cuvantul \'Java\' se afla in textul \'{text}\'.')
elif text.find('Python') > -1:
    print(f'Cuvantul \'Python\' se afla in textul \'{text}\'.')
elif text.find('Java') > -1:
    print(f'Cuvantul \'Java\' se afla in textul \'{text}\'.')
else:
    print(f'Cuvantul \'Python\' si cuvantul \'Java\' nu se afla in textul \'{text}\'.')
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = input('Introduceti un numar intre 1 si 5 (inclusive): ')
try:
    number = int(number)
except:
    pass
if type(number) is str:
    print('Nu ati introdus un numar.')
elif number == 1:
    print('Ati introdus numarul Unu.')
elif number == 2:
    print('Ati introdus numarul Doi.')
elif number == 3:
    print('Ati introdus numarul Trei.')
elif number == 4:
    print('Ati introdus numarul Patru.')
elif number == 5:
    print('Ati introdus numarul Cinci.')
elif number < 1 or number > 5:
    print('Ati introdus un numar in afara celor specificate.')
# CODUL TĂU VINE MAI SUS:
