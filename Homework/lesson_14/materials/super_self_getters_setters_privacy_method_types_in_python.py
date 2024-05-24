# La această lecție, vom explora conceptele avansate ale programării orientate pe obiecte în Python, cum ar fi super() și self, getter/setter și property, privatizarea, și tipurile de metode.

# super() și self
# super() este folosită pentru a accesa metodele clasei părinte, iar self reprezintă instanța curentă a clasei.
# Prin intermediul super() putem accesa metodele clasei părinte, chiar dacă acestea sunt suprascrise în clasa copil.
# Iar prin intermediul self putem accesa atributele și metodele instanței curente a clasei.

class Parinte:
    def __init__(self, nume):
        self.nume = nume

    def afiseaza(self):
        print(f"Numele părintelui este {self.nume}")

class Copil(Parinte):
    def __init__(self, nume, nume_copil):
        super().__init__(nume)  # Accesează constructorul clasei părinte
        self.nume_copil = nume_copil

    def afiseaza(self):
        super().afiseaza()  # Accesează metoda clasei părinte
        print(f"Numele copilului este {self.nume_copil}")

c = Copil("Ion", "Mara")
c.afiseaza()
# Aceasta va afișa:
# Numele părintelui este Ion
# Numele copilului este Mara

# Getter, Setter și Property
# Getter și setter sunt metode utilizate pentru a accesa și a modifica atributele unei clase, respectând principiul incapsulării.

class Persoana:
    def __init__(self, nume):
        self._nume = nume  # Notația _ sugerează că atributul este privat

    @property
    def nume(self):
        return self._nume

    @nume.setter
    def nume(self, valoare):
        self._nume = valoare

p = Persoana("Ana")
print(p.nume)  # Apelul getter
p.nume = "Ioana"  # Apelul setter
print(p.nume)
# Aceasta va afișa:
# Ana
# Ioana

# Privacy (Privatizarea)
# Privatizarea în Python este mai mult o convenție, indicată prin prefixul cu unul sau două underscore (_ sau __).

class ContBancar:
    def __init__(self, suma):
        self.__suma = suma  # Atribut privat

    def afiseaza_suma(self):
        print(f"Suma din cont este {self.__suma}")

cont = ContBancar(1000)
cont.afiseaza_suma()
# Accesul direct la __suma va genera eroare: print(cont.__suma)

# Tipurile de metode: metode de instanță, metode de clasă și metode statice

class Exemplu:
    valoare = "valoare de clasă"

    def metoda_instanței(self):
        print(f"Apelat dintr-o instanță, {self.valoare}")

    @classmethod
    def metoda_clasei(cls):
        print(f"Apelat din clasă, {cls.valoare}")

    @staticmethod
    def metoda_statica():
        print("Apelat static, nu are acces la 'self' sau 'cls'")

e = Exemplu()
e.metoda_instanței()
Exemplu.metoda_clasei()
Exemplu.metoda_statica()
# Aceasta va afișa:
# Apelat dintr-o instanță, valoare de clasă
# Apelat din clasă, valoare de clasă
# Apelat static, nu are acces la 'self' sau 'cls'

# În concluzie, înțelegerea acestor concepte avansate în OOP permite scrierea de cod Python mai sigur, 
# modular și ușor de întreținut, oferind programatorilor instrumentele necesare pentru a construi aplicații robuste și eficiente.
