

class Book:
  
    def __init__(self, title, author, edition_year, isbn, type, borrower):
        self.title = title
        self.author = author
        self.edition_year = edition_year
        self.isbn = isbn
        self.available = True
        self.borrower = borrower
        self.loan_list = []

        if(type  in ["Livres", "CD", "Cassettes", "BD", "Autres"]):
            self.type = type
        else:
            type = ""
       
            
    def borrow(self, student,  begin, renewal_number):
        if(self.available and len(student.borrowedBooks())<1 ):
            self.borrower = student.matricule
            loan = Loan(begin, student.matricule, self.isbn,   "Etudiant",1)
            self.available=False
            self.loan_list.append(loan)
            student.borrowed_books.append(self.isbn)
        elif(self.available):
            print("livre indisponible ou l'etudiant detient deja un livre")
        else:
            print("L'etudiant a deja un livre emprunte")
        
        
        
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