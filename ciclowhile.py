#CICLO MIENTRAS

#DECLARAR UNA VARIABLE CENTINELA
#O VARIABLE DE CONTRO PARA EVALUAR 
#LA EJECUCION DE MI CICLO
i=0
suma = 0
resta = 0
multiplicacion = 0
raiz = 0
num1= 0
num2 = 0
import math

'''
#MENU DE OPCIONES
print("1. saludar")
print("2. despedir")
print("3. contar quien gano el clasico")
print("4. contar si esta lloviendo")
print("5. salir")
#PROGRAMAR LA ESTRUCTURA DEL CICLO MIENTRAS
while(i!=5): #la variableObservadora lo cambie todas por i
    i=int(input("Digite una opción del menú"))
    
    if(i==1):
        print("Hola como estas")
    elif(i==2):
        print("chao amor")
    elif(i==3):
        print("Ganador del rojo")
    elif(i==4):
        print("No llueve en medallo")
    elif(i==5):
        break

    else: 
        print ("Digita una opción valida")

print("salimos del while")


'''

#MENU DE OPCIONES
print("1. sumar 2 numeros")
print("2. restar 2 numeros")
print("3. multiplicar 2 numeros")
print("4. encontrar la raiz cuadrada de 1 numeros")
print("5. salir")
#PROGRAMAR LA ESTRUCTURA DEL CICLO MIENTRAS
while(i!=5): #la variableObservadora lo cambie todas por i
    i=int(input("Digite una opción del menú"))
    if(i==1):
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        suma = num1 + num2
        print("El resultado de la suma es:", suma)
    elif(i==2):
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resta = num1 - num2 
        print("El resultado de la resta es: ", resta)
    elif(i==3):
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        multiplicacion = num1 * num2 
        print("El resultado de la multiplicacion: ", multiplicacion)
    elif(i==4):
        num1 = int(input("Ingrese el primer numero: "))
        raiz = math.sqrt(num1)
        print("El resultado de la raiz:  ", raiz)
    elif(i==5):
        break

    else: 
        print ("Digita una opción valida")

print("salimos del while")
