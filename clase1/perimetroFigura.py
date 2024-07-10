# Algoritmo PerimetroFigura
# D.E: N,M entero
# D.S: Perimetro real
# Comenzar
#    Ingresar Valores de N y M
#    b= N/3
#    a= b/2
#    c=(M-b)/2
#    Perimetro =2a + 2c  + b
# fin
#-----------------------------------------------------
# Ingresar Datos de entrada
N=int(input("ingrese Perimetro del Rectangulo "))
M=int(input("ingrese Perimetro del Triangulo "))
#Procesar Informacion
b=N/3 
a=b/2
c=(M-b)/2
Perimetro= 2*a + 2*c + b
#Mostrar Resultado
print(Perimetro)