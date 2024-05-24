# String-urile reprezintă secvențe de caractere, iar în Python sunt reprezentate de obiecte de tip str.
# String-urile pot fi definite în mai multe moduri:
# - folosind ghilimele simple ('...')
# - folosind ghilimele duble ("...")
# - folosind ghilimele triple ('''...''' sau """...""")

# Să creăm un string folosind ghilimele simple
string1 = 'Hello, World!'
# Să afișăm string1
print(string1)
# Ar trebui să obțineți Hello, World!

# Să creăm un string folosind ghilimele duble
string2 = "Hello, World!"
# Să afișăm string2
print(string2)
# Ar trebui să obțineți Hello, World!

# Să creăm un string folosind ghilimele triple
string3 = '''Hello, World!'''
# Să afișăm string3
print(string3)
# Ar trebui să obțineți Hello, World!

# Să creăm un string folosind ghilimele triple
string4 = """Hello, World!"""
# Să afișăm string4
print(string4)
# Ar trebui să obțineți Hello, World!

# Diferența dintre cele trei moduri de a defini un string este că folosind ghilimelele simple sau duble, string-ul nu poate conține mai multe linii, în timp ce folosind ghilimelele triple, string-ul poate conține mai multe linii.
# De asemenea, folosind ghilimelele duble putem include ghilimele simple în string și invers.

# Să creăm un string folosind ghilimele simple
string5 = 'Hello, "World!"'
# Să afișăm string5
print(string5)
# Ar trebui să obțineți Hello, "World!"

# Să creăm un string folosind ghilimele duble
string6 = "Hello, 'World!'"
# Să afișăm string6
print(string6)
# Ar trebui să obțineți Hello, 'World!'

# În cazul în care vom folosi ghilimele simple în interiorul unui string definit cu ghilimele simple, sau ghilimele duble în interiorul unui string definit cu ghilimele duble, va trebui să folosim caracterul de escape `\` înainte de ghilimelele interioare.

# Să creăm un string folosind ghilimele simple
string7 = 'Hello, \'World!\''
# Să afișăm string7
print(string7)
# Ar trebui să obțineți Hello, 'World!'

# Să creăm un string folosind ghilimele duble
string8 = "Hello, \"World!\""
# Să afișăm string8
print(string8)
# Ar trebui să obțineți Hello, "World!"

# Pentru a indica a reprezenta o linie nouă într-un string, putem folosi caracterul special `\n`.

# Să creăm un string care conține o linie nouă
string9 = 'Hello,\nWorld!'
# Să afișăm string9
print(string9)
# Ar trebui să obțineți:
# Hello,
# World!

# Pentru a indica un tab într-un string, putem folosi caracterul special `\t`.

# Să creăm un string care conține un tab
string10 = 'Hello,\tWorld!'
# Să afișăm string10
print(string10)
# Ar trebui să obțineți Hello,	World!

# Putem concatena două string-uri folosind operatorul `+`.

# Să creăm două string-uri
string11 = 'Hello, '
string12 = 'World!'
# Să concatenăm cele două string-uri
string13 = string11 + string12
# Să afișăm string13
print(string13)
# Ar trebui să obțineți Hello, World!

# Putem înmulți un string cu un număr întreg folosind operatorul `*`.

# Să creăm un string
string14 = 'Hello, '
# Să înmulțim string14 cu 3
string15 = string14 * 3
# Să afișăm string15
print(string15)
# Ar trebui să obțineți Hello, Hello, Hello,

# Putem accesa caracterele unui string folosind indexul acestora.

# Să creăm un string
string16 = 'Hello, World!'
# Să afișăm primul caracter al string-ului
print(string16[0])
# Ar trebui să obțineți H

# Numărarea indexului începe de la 0, deci primul caracter al unui string are indexul 0, al doilea caracter are indexul 1, și așa mai departe.
# Dacă dorim să extragem ultimul caracter al unui string, putem folosi indexul -1.

# Să afișăm ultimul caracter al string-ului
print(string16[-1])
# Ar trebui să obțineți !

# Putem extrage o secvență de caractere dintr-un string folosind slicing.
# Slicing-ul se face folosind două puncte `:` între indexul de început și indexul de sfârșit.

# Să extragem primele 5 caractere ale string-ului
print(string16[:5])
# Ar trebui să obțineți Hello

# Slicing-ul poate fi făcut și cu un index de început și un index de sfârșit negativ.

# Să extragem ultimele 6 caractere ale string-ului
print(string16[-6:])
# Ar trebui să obțineți World!

# Putem verifica dacă un string conține un anumit substring folosind operatorul `in`.

# Să verificăm dacă string16 conține substring-ul 'World'
print('World' in string16)
# Ar trebui să obțineți True

# Putem verifica dacă un string nu conține un anumit substring folosind operatorul `not in`.

# Să verificăm dacă string16 nu conține substring-ul 'World'
print('World' not in string16)
# Ar trebui să obțineți False

# Putem verifica dacă lungimea unui string folosind funcția `len`.

# Să afișăm lungimea string-ului
print(len(string16))
# Ar trebui să obțineți 13

# Putem transforma un string în majuscule folosind metoda `upper`.

# Să transformăm string16 în majuscule
print(string16.upper())
# Ar trebui să obțineți HELLO, WORLD!

# Putem transforma un string în minuscule folosind metoda `lower`.

# Să transformăm string16 în minuscule
print(string16.lower())
# Ar trebui să obțineți hello, world!

# Putem înlocui un substring dintr-un string cu un alt substring folosind metoda `replace`.

# Să înlocuim 'World' din string16 cu 'Python'
print(string16.replace('World', 'Python'))
# Ar trebui să obțineți Hello, Python!

# Putem transforma un string într-o listă de cuvinte folosind metoda `split`.

# Să transformăm string16 într-o listă de cuvinte (mai multe despre liste la următoarea lecție)
print(string16.split())
# Ar trebui să obțineți ['Hello,', 'World!']

# Atât timp cât o variabilă este de tip str, putem aplica metodele specifice string-urilor pe acea variabilă.
# Inclusiv și o porțiune dintr-un string poate fi considerată un string, deci putem aplica metodele specifice string-urilor pe acea porțiune.

# Să extragem primele 5 caractere ale string-ului și să le transformăm în majuscule
print(string16[:5].upper())
# Ar trebui să obțineți HELLO

# Să extragem ultimele 6 caractere ale string-ului și să le transformăm în minuscule
print(string16[-6:].lower())

# Există mai multe tipuri de string-uri, unul dintre ele fiind f-string-urile.
# f-string-urile sunt string-uri care conțin expresii Python între acolade `{}`.
# Aceste expresii sunt evaluate și apoi înlocuite cu rezultatul evaluării lor.

# Să creăm un f-string
name = 'John'
age = 25
f_string = f'My name is {name} and I am {age} years old.'
# Să afișăm f_string
print(f_string)
# Ar trebui să obțineți My name is John and I am 25 years old.

# În f-string-uri putem folosi și metode specifice string-urilor.

# Să afișăm f_string în majuscule
print(f_string.upper())
# Ar trebui să obțineți MY NAME IS JOHN AND I AM 25 YEARS OLD.

# Pentru a verifica dacă un string se începe sau se termină cu un anumit substring, putem folosi metodele `startswith` și `endswith`.

# Să verificăm dacă f_string începe cu 'My'
print(f_string.startswith('My'))
# Ar trebui să obțineți True

# Să verificăm dacă f_string se termină cu 'old.'
print(f_string.endswith('old.'))
# Ar trebui să obțineți True

# Pentru a găsi indexul unui substring într-un string, putem folosi metoda `find`.

# Să găsim indexul la care se află 'name' în f_string
print(f_string.find('name'))
# Ar trebui să obțineți 8

# Dacă substring-ul nu se găsește în string, metoda `find` va returna -1.

# Să găsim indexul la care se află 'Python' în f_string
print(f_string.find('Python'))
# Ar trebui să obțineți -1

# Pentru a număra de câte ori apare un substring într-un string, putem folosi metoda `count`.

# Să numărăm de câte ori apare 'a' în f_string
print(f_string.count('a'))
# Ar trebui să obțineți 3

# Altă metodă utilă este `strip`, care elimină spațiile albe de la început și sfârșitul unui string.

# Să eliminăm spațiile albe de la început și sfârșitul f_string
print(f_string.strip())
# Ar trebui să obțineți My name is John and I am 25 years old.

# Dacă dorim să eliminăm spațiile albe doar de la începutul unui string, putem folosi metoda `lstrip`.

# Să eliminăm spațiile albe de la începutul f_string
print(f_string.lstrip())
# Ar trebui să obțineți My name is John and I am 25 years old.

# Dacă dorim să eliminăm spațiile albe doar de la sfârșitul unui string, putem folosi metoda `rstrip`.

# Să eliminăm spațiile albe de la sfârșitul f_string
print(f_string.rstrip())
# Ar trebui să obțineți My name is John and I am 25 years old.

# Altă metodă de a identifica indexul unui substring într-un string este metoda `index`.

# Să găsim indexul la care se află 'name' în f_string
print(f_string.index('name'))
# Ar trebui să obțineți 8

# Dacă substring-ul nu se găsește în string, metoda `index` va arunca o excepție comparativ cu metoda `find` care va returna -1.

# Altă metodă de a folosi variabile într-un string este folosind metoda `format`.

# Să creăm un string folosind metoda `format`
name = 'John'
age = 25
format_string = 'My name is {} and I am {} years old.'.format(name, age)
# Să afișăm format_string
print(format_string)
# Ar trebui să obțineți My name is John and I am 25 years old.

# Putem folosi și indexul variabilelor în metoda `format`.

# Să creăm un string folosind metoda `format`
name = 'John'
age = 25
format_string = 'My name is {0} and I am {1} years old.'.format(name, age)
# Să afișăm format_string
print(format_string)
# Ar trebui să obțineți My name is John and I am 25 years old.

# Putem folosi și nume pentru variabile în metoda `format`.

# Să creăm un string folosind metoda `format`
name = 'John'
age = 25
format_string = 'My name is {name} and I am {age} years old.'.format(name=name, age=age)
# Să afișăm format_string
print(format_string)
# Ar trebui să obțineți My name is John and I am 25 years old.

# Asta a fost tot pentru această lecție.