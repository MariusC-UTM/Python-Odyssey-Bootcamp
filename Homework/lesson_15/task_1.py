# Aceasta este sarcina pentru lecția despre polimorfism, metode speciale și compoziție a claselor în Python.

from sigmoid_check.python_odyssey.lesson_15.lesson_15 import Lesson15

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.8
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.8

# VERIFICATION PROCESS
session = Lesson15()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE
După toată munca depusă pentru proiectul de la DARWIN și TechSolutions, ai primit o ofertă de la cei de la Microsoft, 
aceștia lucrează la crearea unui algoritm care le va permite procesarea a unor cantități mari de date.
"""

"""
Primul pas în crearea algoritmului este implementarea unor containere de date care va permite stocarea și manipularea datelor într-un mod mai simplu
și eficient. Trebuie să creezi o clasă nouă `DataContainer`. Pentru a manipula datele vom folosi metodele speciale ale clasei.

Clasa va primi ca parametru o listă de numere integer.
- __init__ initializează clasa cu lista de numere.
- __str__ va returna lista de numere sub formă de string.
- __len__ va returna numărul de elemente din listă.
- __getitem__ va permite accesarea elementelor din listă folosind indexul (e.g., container[0]).
- __setitem__ va permite modificarea elementelor din listă folosind indexul (e.g., container[0] = 5).
- __add__ va permite combinarea a două instanțe de `DataContainer` într-o singură instanță.
"""

# CODUL TĂU VINE MAI JOS:
class DataContainer:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return str(self.numbers)

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, index):
        return self.numbers[index]

    def __setitem__(self, index, value):
        self.numbers[index] = value

    def __add__(self, container):
        if isinstance(container, DataContainer):
            return DataContainer(self.numbers + container.numbers)
        else:
            # raise TypeError("Operatia de adunare nu este permisa. Obiectul indicat nu este de tip DataContainer.")
            print("Operatia de adunare nu este permisa. Obiectul indicat nu este de tip DataContainer.")
            return None
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(DataContainer))
# VERIFICATION PROCESS

"""
Acum avem nevoie de o modalitate de a calcula suma și produsul containerului de date. Pentru aceasta creează două clase noi care vor moșteni clasa `DataContainer`.
- `SumaContainer` va calcula suma elementelor din listă.
- `ProdusContainer` va calcula produsul elementelor din listă.
Ambele clase vor avea metoda `calculate` care va returna suma sau produsul elementelor.
"""

# CODUL TĂU VINE MAI JOS:
class SumaContainer(DataContainer):
    def calculate(self):
        return sum(self.numbers)
    
class ProdusContainer(DataContainer):
    def calculate(self):
        result = 1
        for num in self.numbers:
            result *= num
        return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(SumaContainer, ProdusContainer, DataContainer))
# VERIFICATION PROCESS

"""
Pentru ca instrumentul pe care îl folosim să fie complet vom mai avea nevoie de careva adiții.
Creează o clasă `DataAnalysis` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `__call__` va returna o listă cu valorile maxime ale fiecărui container.
"""

# CODUL TĂU VINE MAI JOS:
class DataAnalysis:
    def __init__(self, containers = None):
        if containers is None:
            containers = []
        self.containers = containers

    def add_container(self, container):
        if not isinstance(container, DataContainer):
            # raise TypeError("Parametrul trebuie sa fie un obiect de tip DataContainer")
            print("Operatie esuata. Parametrul trebuie sa fie un obiect de tip DataContainer.")
            return
        self.containers.append(container)

    def __call__(self):
        max_values = []
        for container in self.containers:
            max_values.append(max(container.numbers))
        return max_values
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(DataAnalysis, DataContainer))
# VERIFICATION PROCESS

"""
Pe lângă elementul de analiză a datelor, Microsoft a mai cerut și un element de statistică.
Creează o clasă `DataStatistics` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `mean` va returna media aritmetică a elementelor din toate containerele.
- `median` va returna mediana elementelor din toate containerele.
- `min` va returna valoarea minimă din toate containerele.
- `sum` va returna suma elementelor din toate containerele.
"""

# CODUL TĂU VINE MAI JOS:
class DataStatistics:
    def __init__(self, containers = None):
        if containers is None:
            containers = []
        self.containers = containers

    def add_container(self, container):
        if not isinstance(container, DataContainer):
            # raise TypeError("Parametrul trebuie sa fie un obiect de tip DataContainer")
            print("Operatie esuata. Parametrul trebuie sa fie un obiect de tip DataContainer.")
            return
        self.containers.append(container)

    def mean(self):
        total_sum = 0
        total_count = 0
        for container in self.containers:
            total_sum += sum(container)
            total_count += len(container)
        print('calculated mean =', total_sum / total_count if total_count != 0 else 0)
        return total_sum / total_count if total_count != 0 else 0

    def median(self):
        all_values = []
        for container in self.containers:
            all_values.extend(container)
        all_values.sort()
        n = len(all_values)
        if n % 2 == 0:
            return (all_values[n // 2 - 1] + all_values[n // 2]) / 2
        else:
            return all_values[n // 2]

    def min(self):
        min_value = float('inf')
        for container in self.containers:
            min_value = min(min_value, min(container))
        return min_value

    def sum(self):
        total_sum = 0
        for container in self.containers:
            total_sum += sum(container)
        return total_sum
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(DataStatistics, DataContainer))
# VERIFICATION PROCESS

"""
Iar pe ultima sută de metri, Microsoft a cerut și un element de filtrare a datelor.

Creează o clasă `DataFilter` care va primi ca input o listă de obiecte de tipul `DataContainer`.
- __init__ va inițializa clasa cu lista de obiecte.
- `add_container` va permite adăugarea unui nou container în listă.
- `filter_zeros` va returna o listă cu toate elementele care sunt diferite de 0.
- `filter_negatives` va returna o listă cu toate elementele care sunt mai mari sau egale cu 0.
- `filter_positives` va returna o listă cu toate elementele care sunt mai mici sau egale cu 0.
- `filter_under_mean` va returna o listă cu toate elementele care sunt mai mari decât media aritmetică a tuturor elementelor calculate cu metoda `mean` din clasa `DataStatistics`.
"""

# CODUL TĂU VINE MAI JOS:
class DataFilter:
    def __init__(self, containers = None):
        if containers is None:
            containers = []
        self.containers = containers

    def add_container(self, container):
        if not isinstance(container, DataContainer):
            # raise TypeError("Parametrul trebuie sa fie un obiect de tip DataContainer")
            print("Operatie esuata. Parametrul trebuie sa fie un obiect de tip DataContainer.")
            return
        self.containers.append(container)

    def filter_zeros(self):
        result = []
        for container in self.containers:
            result.extend(filter(lambda x: x != 0, container))
        return result

    def filter_negatives(self):
        result = []
        for container in self.containers:
            result.extend(filter(lambda x: x >= 0, container))
        return result

    def filter_positives(self):
        result = []
        for container in self.containers:
            result.extend(filter(lambda x: x <= 0, container))
        return result

    def filter_under_mean(self):
        data_stats = DataStatistics(self.containers)
        for data in data_stats.containers:
            print(data)
        mean_value = data_stats.mean()
        print('rounded mean =', round(mean_value))
        print('int mean =', int(mean_value))
        result = []
        for container in self.containers:
            result.extend(filter(lambda x: x > mean_value, container))
        return result

# Testing
container1 = DataContainer([1, 2, 3, 0, -1, -2, -3])
container2 = DataContainer([0, 5, -5, 10, -10])
data_filter = DataFilter([container1, container2])
data_filter.add_container(DataContainer([-4, 6, 7]))
all_data = []
for data in data_filter.containers:
    all_data.extend(data)
print('Toate elementele:', all_data)
print('Elemente diferite de zero:', data_filter.filter_zeros())
print('Fara elemente negative:', data_filter.filter_negatives())
print('Fara elemente pozitive:', data_filter.filter_positives())
print('Fara elemente sub media aritmetica:', data_filter.filter_under_mean())
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(DataFilter, DataStatistics, DataContainer))
print(session.get_completion_percentage())
# VERIFICATION PROCESS
