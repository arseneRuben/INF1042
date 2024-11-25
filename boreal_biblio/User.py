class User : 
    def __init__(self,matricule, firstname, lastname, email):
        self.matricule = matricule
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.borrowed_books=[]
        
    def __repr__(self):
        return "({}, {}, {}, {})".format(self.matricule,  self.firstname, self.lastname ,  self.email )

    def borrowedBooks(self):
        return self.borrowed_books

class Teacher(User):
    
    
    def __repr__(self):
        return "Teacher : ({}, {}, {}, {}, {})".format(self.matricule,  self.firstname, self.lastname ,  self.email ,  self.borrowed_books  )


class Student(User):
    
   

    def __repr__(self):
        return "Student : ({}, {}, {}, {}, {})".format(self.matricule,  self.firstname, self.lastname ,  self.email, self.borrowed_books )
      
    
        