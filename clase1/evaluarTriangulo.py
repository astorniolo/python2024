
# Ingresar L1,L2,L3
L1=int(input("ingrese el lado L1: "))
L2=int(input("ingrese el lado L2: "))
L3=int(input("ingrese el lado L3: "))

# Evaluar desigualdad de Minkowski:
if  (L1 + L2 > L3  and  L2 + L3>L1 and  L3 + L1 > L2) :
    print("Es posible formar un triangulo")
else:
    print("NO es posible formar un triangulo")

#Evaluar tipo de TRIANGULO
if(L1 == L2  and  L2 == L3): 
    print("Es un triangulo equilatero") 
else:
    if (L1 == L2  or  L2 == L3  or  L1==L3):
        print("Es un triangulo isosceles")                                                   
    else:
        print("Es un triangulo escaleno")     