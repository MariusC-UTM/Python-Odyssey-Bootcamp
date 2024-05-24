# La această lecție, vom explora conceptele de polimorfism, metode speciale și compoziție a claselor în Python, cu multiple exemple pentru a clarifica ideile.

# Polimorfism
# Polimorfismul permite obiectelor de diferite clase să fie tratate prin aceeași interfață, 
# mai ales când acestea implementează aceeași metodă. Aceasta este o componentă cheie în flexibilitatea programării orientate pe obiecte.

class Caine:
    def vorbeste(self):
        return "Ham!"

class Pisica:
    def vorbeste(self):
        return "Miau!"

def sunet_animal(animal):
    print(animal.vorbeste())

sunet_animal(Caine())
sunet_animal(Pisica())
# Aceasta va afișa:
# Ham!
# Miau!

# Metode speciale (Magic Methods)
# Python folosește metode speciale, cum ar fi __init__, __str__, __len__, __del__, __call__, __getitem__, __setitem__, __eq__, __add__, __iter__  etc., pentru a permite claselor 
# să implementeze și să interacționeze cu comportamentele limbajului sau operatorii integrati.

class Carte:
    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor

    def __str__(self):
        return f"{self.titlu} de {self.autor}"

    def __len__(self):
        return len(self.titlu)
    
    def __del__(self):
        print("Cartea a fost ștearsă")

    def __call__(self):
        return f"{self.titlu} de {self.autor}"
    
    def __getitem__(self, index):
        return self.titlu[index]
    
    def __setitem__(self, index, valoare):
        self.titlu = self.titlu[:index] + valoare + self.titlu[index+1:]

    def __eq__(self, alta_carte):
        return self.titlu == alta_carte.titlu and self.autor == alta_carte.autor
    
    def __add__(self, alta_carte):
        return Carte(f"{self.titlu} și {alta_carte.titlu}", f"{self.autor} și {alta_carte.autor}")
    
    def __iter__(self):
        return iter(self.titlu)
    

carte = Carte("OOP în Python", "Ion Popescu")
print(carte)  # Apelul metodei __str__
print(len(carte))  # Apelul metodei __len__
del carte  # Apelul metodei __del__
# print(carte)  # Va genera eroare deoarece obiectul nu mai există
carte = Carte("OOP în Python", "Ion Popescu")
print(carte())  # Apelul metodei __call__
print(carte[0])  # Apelul metodei __getitem__
carte[0] = "P"
carte2 = Carte("OOP în Python", "Ion Popescu")
print(carte == carte2)  # Apelul metodei __eq__
carte3 = carte + carte2
print(carte3)  # Apelul metodei __add__
for litera in carte:
    print(litera)  # Apelul metodei __iter__
# Aceasta va afișa:
# OOP în Python de Ion Popescu
# 14
# Cartea a fost ștearsă
# OOP în Python de Ion Popescu
# O
# True
# OOP în Python și OOP în Python de Ion Popescu și Ion Popescu
# O
# O
# P

# Compoziție a claselor
# Compoziția este un principiu de design OOP unde clasele pot conține instanțe ale altor clase, 
# ceea ce permite o structură mai flexibilă și modulară.

class Autor:
    def __init__(self, nume):
        self.nume = nume

class Carte:
    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor  # Autor este o instanță a clasei Autor

ion = Autor("Ion Popescu")
carte = Carte("OOP în Python", ion)
print(f"{carte.titlu} scrisă de {carte.autor.nume}")
# Aceasta va afișa: OOP în Python scrisă de Ion Popescu

# În concluzie, polimorfismul, metodele speciale și compoziția sunt concepte esențiale în programarea orientată pe obiecte.
# Acestea permit crearea de cod reutilizabil, flexibil și intuitiv, facilitând structurarea și extensia aplicațiilor.
