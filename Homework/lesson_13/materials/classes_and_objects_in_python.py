# La această lecție vom explora conceptele de bazație ale programării orientate pe obiecte în Python, inclusiv clase, __init__, moștenire și suprascrierea metodelor.

# Clasele sunt modele pentru crearea de obiecte și oferă structură pentru stocarea datelor și comportamentelor (metode).

# Crearea unei clase simple cu un constructor __init__:
class Masina:
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model

    def afiseaza_informatii(self):
        print(f"Mașina este un {self.marca} {self.model}.")

masina_me = Masina("Toyota", "Corolla")
masina_me.afiseaza_informatii()
# Aceasta va afișa: Mașina este un Toyota Corolla.

# Nu e neapărat necesar ca metodele să aibă parametrul self, dar acesta este necesar pentru a accesa atributele și metodele obiectului.
# Atributele sunt variabile care sunt legate de obiect și sunt accesibile prin self.
# De asemenea nu e neaepărat necesar prezența constructorului __init__, dar este recomandat pentru inițializarea obiectelor.

# Crearea unei clase simple fără constructor:
class Masina:
    def seteaza_marca(self, marca):
        self.marca = marca

    def seteaza_model(self, model):
        self.model = model

    def afiseaza_informatii(self):
        print(f"Mașina este un {self.marca} {self.model}.")

masina_me = Masina()
masina_me.seteaza_marca("Toyota")
masina_me.seteaza_model("Corolla")
masina_me.afiseaza_informatii()
# Aceasta va afișa: Mașina este un Toyota Corolla.

# Crearea unei clase fără a utiliza self:
class Masina:
    def seteaza_marca(marca):
        return marca

    def seteaza_model(model):
        return model

    def afiseaza_informatii(marca, model):
        print(f"Mașina este un {marca} {model}.")

masina_me = Masina()
marca = masina_me.seteaza_marca("Toyota")
model = masina_me.seteaza_model("Corolla")
masina_me.afiseaza_informatii(marca, model)
# Aceasta va afișa: Mașina este un Toyota Corolla.

# Moștenirea permite crearea de noi clase care preiau atribute și metode de la o clasă existentă.

# Crearea unei subclase care moștenește clasa Masina:
class MasinaElectrica(Masina):
    def __init__(self, marca, model, autonomie):
        super().__init__(marca, model)  # Apelarea constructorului clasei părinte
        self.autonomie = autonomie

    def afiseaza_autonomie(self):
        print(f"Autonomia mașinii este de {self.autonomie} km.")

masina_electrica_me = MasinaElectrica("Tesla", "Model S", 500)
masina_electrica_me.afiseaza_informatii()
masina_electrica_me.afiseaza_autonomie()
# Aceasta va afișa:
# Mașina este un Tesla Model S.
# Autonomia mașinii este de 500 km.

# Suprascrierea metodelor (Method Overriding) permite unei subclase să modifice comportamentul unei metode din clasa părinte.

# Suprascrierea metodei afiseaza_informatii în MasinaElectrica:
class MasinaElectrica(Masina):
    def __init__(self, marca, model, autonomie):
        super().__init__(marca, model)
        self.autonomie = autonomie

    def afiseaza_informatii(self):
        super().afiseaza_informatii()  # Apelarea metodei din clasa părinte
        print(f"Și este electrică cu o autonomie de {self.autonomie} km.")

masina_electrica_me = MasinaElectrica("Tesla", "Model S", 500)
masina_electrica_me.afiseaza_informatii()
# Aceasta va afișa:
# Mașina este un Tesla Model S.
# Și este electrică cu o autonomie de 500 km.

# În concluzie, clasele și obiectele sunt fundamentale în Python pentru programarea orientată pe obiecte, 
# permițând structurarea codului într-o manieră modulară și intuitivă. Moștenirea și suprascrierea metodelor 
# oferă flexibilitate în extinderea și adaptarea comportamentelor claselor.
