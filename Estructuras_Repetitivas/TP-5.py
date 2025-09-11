#Trabajo Practico N°5

#Ejercicio N°1

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

#Ejercicio N°2

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un número: "))
cantidad_digitos = len(str(num))
print("La cantidad de dígitos es:", cantidad_digitos)

#Ejercicio N°3
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

suma = 0
for i in range(valor1 + 1, valor2):
    suma += i

print("La suma de los números entre", valor1, "y", valor2, "es:", suma)

#Ejercicio N°4
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma_total = 0
while True:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    if numero == 0:
        break
    suma_total += numero

print("La suma total es:", suma_total)

#Ejercicio N°5
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intentos += 1
    numero_ingresado = int(input("Ingrese un número entre 0 y 9: "))
    if numero_ingresado == numero_aleatorio:
        print("¡Adivinaste el número en", intentos, "intentos!")
        break
    else:
        print("Número incorrecto, intenta de nuevo.")
        
#Ejercicio N°6
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)
    
#Ejercicio N°7
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un número positivo: "))
suma = 0
for i in range(num + 1):
    suma += i

print("La suma de los números entre 0 y", num, "es:", suma)

#Ejercicio N°8
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad=100
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Hay {pares} números pares, {impares} números impares, {positivos} números positivos y {negativos} números negativos.")

#Ejercicio N°9

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 100
suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / cantidad
print(f"La media de los números ingresados es: {media}")

#Ejercicio N°10
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número: "))
numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10

print("El número invertido es:", numero_invertido)