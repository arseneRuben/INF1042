LIMIT = 2
from User import Student
class Book:
  
    def __init__(self, title, author, edition_year, isbn, type, borrower):
        self.title = title
        self.author = author
        self.edition_year = edition_year
        self.isbn = isbn
        self.available = True
        self.borrower = borrower
        self.loan_list = []

        if(type  in ["LIVRES", "CD", "CASSETTES", "BD", "AUTRES"]):
            self.type = type
        else:
            type = ""
       
            
    def borrow(self, usr,  begin, renewal_number):

        if(isinstance(usr, Student)):

            if(self.available and len(usr.borrowedBooks())<1 ):
                self.borrower = usr.matricule
                loan = Loan(begin, usr.matricule, self.isbn,   "Etudiant",1)
                self.available=False
                self.loan_list.append(loan)
                usr.borrowed_books.append(self.isbn)

            elif(not(self.available)):
                print("`Le livre {} est indisponible".format(self.title))
            else:
                print("L'etudiant a deja un livre emprunte")
        else:
            if(self.available and len(usr.borrowedBooks())<LIMIT ):
                self.borrower = usr.matricule
                loan = Loan(begin, usr.matricule, self.isbn,   "Etudiant",1)
                self.available=False
                self.loan_list.append(loan)
                usr.borrowed_books.append(self.isbn)

            elif(not(self.available)):
                print("`Le livre {} est indisponible".format(self.title))
            else:
                print("L'enseignant a deja {} livre emprunte".format(LIMIT))


        
        
        
    def __repr__(self):
        return "({}, {}, {}, {}, {},{}, {})".format(self.title,  self.author, self.edition_year ,  self.isbn,  self.type , self.borrower, self.available)


class Loan:
    def __init__(self, begin, matricule, isbn, type, renewal_number):
        self.begin = begin
        self.matricule = matricule
        self.isbn = isbn
        if(type  in ["Professeur", "Etudiant"]):
            self.type = type
        else:
            type = ""
        self.renewal_number = 0
    def __repr__(self):
        return "({}, {}, {}, {}, {})".format(self.isbn,  self.matricule, self.begin ,  self.isbn,  self.renewal_number )