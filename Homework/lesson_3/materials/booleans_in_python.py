# Booleans în Python
# Booleans este cel mai simplu tip de date în Python
# Un boolean poate avea doar două valori: True sau False
# Puteți utiliza booleans pentru a lua decizii în codul dvs.
# De exemplu, puteți utiliza un boolean pentru a verifica dacă o condiție este True sau False
# Puteți utiliza, de asemenea, booleans pentru a compara valori
# De exemplu, puteți utiliza operatorul de egalitate (==) pentru a compara două valori
# Dacă cele două valori sunt egale, rezultatul este True
# Dacă cele două valori nu sunt egale, rezultatul este False
# Puteți utiliza, de asemenea, și alți operatori de comparație pentru a compara valori
# Iată o listă cu toți aceștia:
# - Egal: ==
# - Diferit: !=
# - Mai mare decât: >
# - Mai mic decât: <
# - Mai mare decât sau egal cu: >=
# - Mai mic decât sau egal cu: <=
# Dar destulă vorbărie, să creăm niște booleans:
# Să creăm o variabilă booleană numită is_student și să-i atribuim valoarea True
is_student = True
# Acum să afișăm valoarea lui is_student
print(is_student)
# Puteți utiliza, de asemenea, operatorul de egalitate pentru a compara valori
# Să creăm o variabilă booleană numită is_teacher și să-i atribuim valoarea False
is_teacher = False
# Acum să comparăm valorile lui is_student și is_teacher
# Dacă cele două valori sunt egale, rezultatul este True
# Dacă cele două valori nu sunt egale, rezultatul este False
print(is_student == is_teacher)
# Puteți utiliza, de asemenea, și alți operatori de comparație pentru a compara valori
# Să comparăm valorile lui is_student și is_teacher folosind operatorul de diferență
# Dacă cele două valori nu sunt egale, rezultatul este True
# Dacă cele două valori sunt egale, rezultatul este False
print(is_student != is_teacher)
# Cred că ai înțeles ideea

# O altă modalitate de a utiliza booleans este cu ajutorul operatorilor and, or și not
# Puteți utiliza and pentru a verifica dacă două sau mai multe condiții sunt True
# Puteți utiliza or pentru a verifica dacă cel puțin o condiție este True
# Puteți utiliza not pentru a verifica dacă o condiție este False
# Să creăm două variabile booleans
is_student = True
is_teacher = False
# Acum să utilizăm and pentru a verifica dacă is_student și is_teacher sunt True
# Dacă ambele condiții sunt True, rezultatul este True
# Dacă cel puțin o condiție este False, rezultatul este False
print(is_student and is_teacher)
# Acum să utilizăm or pentru a verifica dacă is_student sau is_teacher sunt True
# Dacă cel puțin o condiție este True, rezultatul este True
# Dacă ambele condiții sunt False, rezultatul este False
print(is_student or is_teacher)
# Acum să utilizăm not pentru a verifica dacă is_student este False
# Dacă condiția este False, rezultatul este True
# Dacă condiția este True, rezultatul este False
print(not is_student)
# Aceasta este tot pentru booleans
