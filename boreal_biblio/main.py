from  User import Student
from  User import Teacher
from  Catalog import Book

import datetime

loan_list = []
book_list = []
student_list = []
teacher_list = []

learnPyhon = Book("Learn Python By Practice", "Wilson Ted", "2023", 32432, "Livres", None)
learnSpring = Book("Spring framework", "Anta Djeng", "2022", 32132, "Livres", None)
powerShell = Book("Power Shell", "Paul ", "2020", 32135, "Livres", None)

book_list.append(learnPyhon)
book_list.append(learnSpring)
book_list.append(powerShell)

ashley = Student(2, "Ashley", "Cole", "ashleycole@city.com")
oumar = Student(3, "Oumar", "Zidane", "oumar@city.com")

student_list.append(ashley)
student_list.append(oumar)

teacher_list.append(Teacher(3, "Jean", "Savoie", "savoiejean@madrid.com"))
learnPyhon.borrow(ashley,datetime.datetime.now(),0) 
powerShell.borrow(ashley,datetime.datetime.now(),0) 

learnSpring.borrow(oumar,datetime.datetime.now(),0) 





