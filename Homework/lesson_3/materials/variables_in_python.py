# Deci, ce este o variabilă? O variabilă este un container pentru o valoare, care poate fi de diferite tipuri.
# În Python, variabilele sunt create atunci când atribuiți o valoare folosind operatorul de atribuire (=).
# Variabila este apoi atribuită valorii. Puteți să vă gândiți la o variabilă ca la o etichetă pentru o valoare.
# Puteți utiliza numele variabilei pentru a accesa valoarea sau pentru a o schimba.
# Dar fiți atenți, există câteva limitări ale numelor de variabile:
# - Pot conține doar litere, cifre și linii de subliniere.
# - Nu pot începe cu o cifră.
# - Nu pot conține spații.
# - Nu pot fi un cuvânt cheie Python.
# - Ar trebui să fie descriptive, fără a fi prea lungi.
# Dar mai puține vorbe, să creăm câteva variabile:
# Să creăm o variabilă numită grade și să-i atribuim valoarea 9
grade = 9
# Acum să imprimăm valoarea gradei
# Puteți utiliza funcția print pentru a imprima valoarea unei variabile
print(grade)
# Puteți, de asemenea, să schimbați valoarea unei variabile
grade = 10
# Acum să imprimăm din nou valoarea gradei
print(grade)
# Puteți, de asemenea, să atribuiți o variabilă altei variabile
# Să creăm o variabilă numită grade2 și să-i atribuim valoarea gradei
grade2 = grade
# Acum să imprimăm valoarea grade2
print(grade2)
# Puteți, de asemenea, să atribuiți o variabilă valorii unei expresii

# Rețineți că variabilele sunt practic memorie în computerul dvs.
# Și așa cum puteți crea variabile, le puteți și șterge
# Puteți șterge o variabilă folosind cuvântul cheie del
# Să ștergem variabila grade
del grade
# Acum să încercăm să imprimăm valoarea gradei
print(grade)
# Ar trebui să obțineți o eroare
# Asta pentru că variabila grade nu mai există
# Puteți, de asemenea, să ștergeți mai multe variabile în același timp
# Să creăm două variabile numite x și y
x = 5
y = 10
# Acum să ștergem ambele
del x, y
# Acum să încercăm să imprimăm valoarea lui x
print(x)
# Ar trebui să obțineți o eroare
# Asta pentru că variabila x nu mai există
# Și același lucru se aplică și pentru y
# Asta e tot pentru variabile
# Să trecem la următorul subiect
