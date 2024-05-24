# La această lecție vom învăța despre instrucțiunile condiționale if, else și elif.
# Instrucțiunile condiționale sunt folosite pentru a executa cod diferit în funcție de anumite condiții.
# Instrucțiunea if este cea mai simplă formă de instrucțiune condițională.

# De exemplu, să verificăm dacă un număr este pozitiv:

num = 10
if num > 0:
    print("Numărul este pozitiv")
# Ar trebui să obțineți 'Numărul este pozitiv'
    
# După cuvântul cheie if, se specifică o condiție care trebuie să fie evaluată ca adevărată sau falsă.
# Dacă condiția este adevărată, blocul de cod care urmează după if este executat.
# Dacă condiția este falsă, blocul de cod este ignorat.
# Această condiție poate fi orice expresie care poate fi evaluată ca adevărată sau falsă.
# Inclusiv și o variabilă booleană, o comparație între două valori sau o expresie aritmetică.

# Instrucțiunea else poate fi folosită pentru a executa un bloc de cod dacă condiția inițială if nu este adevărată.

# De exemplu, să verificăm dacă un număr este pozitiv sau negativ:

num = -5
if num > 0:
    print("Numărul este pozitiv")
else:
    print("Numărul este negativ")
# Ar trebui să obțineți 'Numărul este negativ'
    
# Observați că blocul de cod care urmează după else este executat doar dacă condiția inițială if este falsă.
# De asemenea avem nevoie de identare pentru a indica blocurile de cod care sunt executate în cadrul instrucțiunilor condiționale.
# În Python, blocurile de cod sunt identate cu 4 spații sau un tab.
# Blocurile de cod care sunt la același nivel de identare sunt considerate a face parte din același bloc de cod.
# Blocurile de cod care sunt identate diferit sunt considerate a face parte din blocuri de cod diferite.
# De exemplu, blocul de cod care urmează după if este identat cu 4 spații, iar blocul de cod care urmează după else este identat cu aceeași cantitate de spații.
# Acest lucru indică că ambele blocuri de cod sunt parte a instrucțiunii condiționale if-else.

# Instrucțiunea elif (prescurtare pentru else if) permite verificarea mai multor condiții.

# De exemplu, să verificăm dacă un număr este pozitiv, negativ sau zero:

num = 0
if num > 0:
    print("Numărul este pozitiv")
elif num == 0:
    print("Numărul este zero")
else:
    print("Numărul este negativ")
# Ar trebui să obțineți 'Numărul este zero'

# În acest caz avem trei blocuri de cod care sunt verificate în ordine.
# Dacă prima condiție if este adevărată, blocul de cod care urmează după if este executat și restul condițiilor sunt ignorate.
# Dacă prima condiție if este falsă, se trece la următoarea condiție elif.
# Dacă condiția elif este adevărată, blocul de cod care urmează după elif este executat și restul condițiilor sunt ignorate.
# Dacă niciuna dintre condiții nu este adevărată, blocul de cod care urmează după else este executat.
    
# Instrucțiunile condiționale pot fi îmbinate pentru a forma condiții complexe

# De exemplu, să determinăm categoria de vârstă a unei persoane:

age = 20
if age < 13:
    print("Copil")
elif age < 20:
    print("Adolescent")
elif age < 60:
    print("Adult")
else:
    print("Vârstnic")
# Ar trebui să obțineți 'Adult'

# Instrucțiunile condiționale sunt fundamentale în programare și sunt folosite pentru a controla fluxul de execuție al programelor.
# Acestea permit programelor să ia decizii și să execute diferite blocuri de cod în funcție de diferite condiții.

# După cum am menționat anterior condițiile pot fi și variabile booleane.

# De exemplu, să verificăm dacă o variabilă booleană este adevărată sau falsă:

is_true = True

if is_true:
    print("Variabila este adevărată")
else:
    print("Variabila este falsă")
# Ar trebui să obțineți 'Variabila este adevărată'
    
# and, or și not sunt operatori logici care pot fi folosiți pentru a combina condiții.
    
# Operatorul and returnează adevărat dacă ambele condiții sunt adevărate.

# De exemplu, să verificăm dacă un număr este pozitiv și par:

num = 10
if num > 0 and num % 2 == 0:
    print("Numărul este pozitiv și par")
else:
    print("Numărul nu este pozitiv și par")
# Ar trebui să obțineți 'Numărul este pozitiv și par'
    
# Operatorul or returnează adevărat dacă cel puțin una dintre condiții este adevărată.

# De exemplu, să verificăm dacă un număr este pozitiv sau par:

num = -4
if num > 0 or num % 2 == 0:
    print("Numărul este pozitiv sau par")
else:
    print("Numărul nu este pozitiv sau par")
# Ar trebui să obțineți 'Numărul nu este pozitiv sau par'
    
# Orice expreesie care poate fi evaluată ca adevărată sau falsă poate fi folosită într-o instrucțiune condițională.
# Putem folosi și liste, dicționare sau alte structuri de date în condițiile instrucțiunilor condiționale.
    
# De exemplu să realizăm o anumită acțiune numai în cazul în care list este goală:
    
my_list = []
if not my_list:
    print("Listă goală")
else:
    print("Listă nu este goală")
# Ar trebui să obțineți 'Listă goală'
    
# În acest exemplu, am folosit operatorul not pentru a verifica dacă lista my_list este goală.
    
# Asta a fost tot ce ține de conditional statements în Python.