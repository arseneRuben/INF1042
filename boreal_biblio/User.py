class User : 
    def __init__(self,matricule, firstname, lastname, email):
        self.matricule = matricule
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.borrowed_books=[]
        
    def __repr__(self):
        return "({}, {}, {}, {})".format(self.matricule,  self.firstname, self.lastname ,  self.email )


class Teacher(User):
    
    def borrowedBooks(self):
        return self.borrowed_books
    def __repr__(self):
        return "Teacher : ({}, {}, {}, {})".format(self.matricule,  self.firstname, self.lastname ,  self.email )


class Student(User):
    
    def borrowedBooks(self):
        return self.borrowed_books

    def __repr__(self):
        return "Student : ({}, {}, {}, {}, {})".format(self.matricule,  self.firstname, self.lastname ,  self.email, self.borrowed_books )
      
    
        