# Ejercicio N°1

#Mostrar un mensaje en pantalla

print("Hola Mundo")

#Ejercicio N°2

#Ingresar nombre

nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)

#Ejercicio N°3

#Ingresar nombre, edad y país

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su país: ")
print("Hola " + nombre + ", tienes " + edad + " años y vives en " + pais)

#Ejercicio N°4

#Ingresar el radio de un círculo y calcular su área

import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio**2
print("El área del círculo es: " + str(area))

#Ejercicio N°5

# Ingresar tiempo en segundos y convertir a horas
segundos = int(input("Ingrese el tiempo en segundos: "))
horas = segundos // 3600 #es lo que hay en horas
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#Ejercicio N°6

# Pedimos al usuario que ingrese un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Mostramos la tabla del 1 al 10
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio N°7

# Pedimos al usuario que ingrese dos números distintos de 0
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

# Validamos que no sean cero
if num1 == 0 or num2 == 0:
    print("¡Error! Ambos números deben ser distintos de 0.")
else:
    # Realizamos las operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    # Mostramos los resultados
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division:.2f}")

    #Ejercicio N°8

    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / altura**2
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

    #Ejercicio N°9
    
    grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    grados_fahrenheit = (grados_celsius * 9/5) + 32
    print(f"La temperatura en grados Fahrenheit es: {grados_fahrenheit:.2f}")

     #Ejercicio N°10
     #Ingresar tres números y calcular su promedio
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    #calcular el promedio
    promedio = (num1 + num2 + num3) / 3
    #mostrar el resultado
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
