from  User import Student
from  User import Teacher
from  Catalog import Book

import datetime

loan_list = []
book_list = []
student_list = []
teacher_list = []

# Cette fonction fournit notre bibliotheque avec N livres avec les caracteristiques suivantes :
# - title du livre num i : title_i
# - autheur du livre num i : authour_i
# - edition du livre num i : 20_an avec an = i % 25
# - isbn du livre num i : 3000 + i
# - type du livre i =
#  * LIVRES si i % 5 = 0
#  * CD     si i % 5 = 1
#  * CASSETTES  si i % 5 = 2
#  * BD         si i % 5 = 3
#  * AUTRES     si i % 5 = 3


learnPyhon = Book("Learn Python By Practice", "Wilson Ted", "2023", 32432, "Livres", None)
learnSpring = Book("Spring framework", "Anta Djeng", "2022", 32132, "Livres", None)
powerShell = Book("Power Shell", "Paul ", "2020", 32135, "Livres", None)
learnGit = Book("Git", " Simon Shey ", "2000", 31135, "Livres", None)

book_list.append(learnPyhon)
book_list.append(learnSpring)
book_list.append(powerShell)

ashley = Student(2, "Ashley", "Cole", "ashleycole@city.com")
oumar = Student(3, "Oumar", "Zidane", "oumar@city.com")

student_list.append(ashley)
student_list.append(oumar)
jean = Teacher(3, "Jean", "Savoie", "savoiejean@madrid.com")
teacher_list.append(jean)

teacher_list.append(jean)
learnPyhon.borrow(jean,datetime.datetime.now(),0) 
powerShell.borrow(jean,datetime.datetime.now(),0) 
learnGit.borrow(jean,datetime.datetime.now(),0) 

learnSpring.borrow(jean,datetime.datetime.now(),0)

print(jean)





