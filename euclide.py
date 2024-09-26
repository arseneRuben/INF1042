
a = int(input("entrer A : "))
while(a < 0):
    a = int(input("DOnner une valeur positive: "))
b = int(input("entrer B : "))
while(b < 0):
    b = int(input("DOnner une valeur positive: "))

if(a < b):
    c = a
    a = b
    b = c
print(a , b)

m = a
n = b
if(a == 0):
    print("PGCD(",a," ",b,") = ", b)
if(b == 0):
    print("PGCD(",a," ",b,") = ", a)

while(b>0):
    c = a%b
    a = b
    b = c
print("PGCD(",m," ",n,") = ", a)
    
