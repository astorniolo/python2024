#Ingresar n
n=int(input("Ingresar n "))
#inicializar el acumulador en 0 
acumulador=0
#iterar en cada termino
for i in range(0,n+1):
    termino_i=  ((-1)**i)/(1+i)
    acumulador= acumulador + termino_i
    print(f'i={i} termino_i = {termino_i} acumulador={acumulador}')
#muestro resultados3
print(f'El valor de la serie para el termino n {n} es {acumulador}') 
