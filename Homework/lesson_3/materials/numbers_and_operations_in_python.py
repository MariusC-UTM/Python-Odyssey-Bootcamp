# Acum să vorbim despre numere în Python
# Există trei tipuri numerice în Python:
# - int
# - float
# - complex
# Să începem cu int (prescurtare pentru întreg)
# Intregii sunt numere întregi, pozitive sau negative, fără zecimale, de lungime nelimitată
# De exemplu: 1, 100, -567, 100
# Puteți utiliza funcția type() pentru a obține tipul unei variabile
# Să creăm o variabilă numită x și să-i atribuim valoarea 1
x = 1
# Acum să afișăm tipul lui x
print(type(x))
# Ar trebui să obțineți <class 'int'>
# Să creăm acum o variabilă numită y și să-i atribuim valoarea -100
y = -100
# Acum să afișăm tipul lui y
print(type(y))
# Ar trebui să obțineți <class 'int'>
# Și așa cum ați văzut anterior, putem, de asemenea, să afișăm valoarea unei variabile
# Să afișăm valoarea lui x
print(x)
# Ar trebui să obțineți 1
# Acum să afișăm valoarea lui y
print(y)
# Ar trebui să obțineți -100
# Acum să vorbim despre float
# Float (prescurtare pentru număr cu virgulă mobilă) este un număr, pozitiv sau negativ, care conține una sau mai multe zecimale
# De exemplu: 1.0, -100.5, 100.0
# Să creăm o variabilă numită z și să-i atribuim valoarea 1.0
z = 1.0
# Acum să afișăm tipul lui z
print(type(z))

# La fel cum puteți face operații cu numere în matematică, puteți face același lucru în Python
# De exemplu, să creăm o variabilă numită a și să-i atribuim valoarea 5
a = 5
# Acum să creăm o variabilă numită b și să-i atribuim valoarea 2
b = 2
# Acum să afișăm suma lui a și b
print(a + b)
# Ar trebui să obțineți 7
# Acum să afișăm diferența dintre a și b
print(a - b)
# Ar trebui să obțineți 3
# Acum să afișăm produsul lui a și b
print(a * b)
# Ar trebui să obțineți 10
# Acum să afișăm împărțirea lui a și b
print(a / b)
# Ar trebui să obțineți 2.5
# Acum să afișăm restul împărțirii lui a și b
print(a % b)
# Ar trebui să obțineți 1
# Acum să afișăm rezultatul lui a ridicat la puterea lui b
print(a ** b)
# Ar trebui să obțineți 25
# Acum să vorbim despre împărțirea întreagă a lui a și b
print(a // b)
# Ar trebui să obțineți 2

# Acestea sunt operațiile de bază pe care le puteți face cu numere în Python
# Un alt lucru important de știut este că
# Când împărțiți două numere întregi, veți obține întotdeauna un float
# De exemplu, să creăm o variabilă numită c și să-i atribuim valoarea 10
c = 10
# Acum să creăm o variabilă numită d și să-i atribuim valoarea 3
d = 3
# Acum să afișăm împărțirea lui c și d
print(c / d)
# Ar trebui să obțineți 3.3333333333333335
# Acum să afișăm tipul împărțirii lui c și d
print(type(c / d))
# Ar trebui să obțineți <class 'float'> despre acest tip de variabile vom vorbi la următoarele lecții

# Un alt element pe care ar trebui să-l știți sunt literalele numerice
# Puteți utiliza linii de subliniere pentru a face numerele mai ușor de citit
# De exemplu, să creăm o variabilă numită f și să-i atribuim valoarea 1_000_000
f = 1_000_000
# Acum să afișăm valoarea lui f
print(f)
# Ar trebui să obțineți 1000000
# Acum să creăm o variabilă numită g și să-i atribuim valoarea 1_000_000.0
g = 1_000_000.0
# Acum să afișăm valoarea lui g
print(g)
# Ar trebui să obțineți 1000000.0

# Și ca ultim element, să vorbim despre numerele complexe
# Numerele complexe sunt numere cu o parte reală și o parte imaginară
# De exemplu: 1 + 2j, 1 - 2j
# Nu vom intra în prea multă teorie în spatele lor, dar ar trebui să știți că puteți crea un număr complex în Python
# Să creăm o variabilă numită h și să-i atribuim valoarea 1 + 2j
h = 1 + 2j
# Acum să afișăm tipul lui h
print(type(h))
# Ar trebui să obțineți <class 'complex'>
# Acum să afișăm valoarea lui h
print(h)
# Ar trebui să obțineți (1+2j)

# Aceasta este totul despre numere în Python
