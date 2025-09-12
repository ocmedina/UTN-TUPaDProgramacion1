#Trabajo Adicional N°6

#Ejercicio N°1

#1.Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingresa una palabra: ")
for _ in range(10):
    print(palabra)  
    
#Ejercicio N°2

#2.Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Ingresa tu edad: "))
for año in range(1, edad + 1):
    print(año)
    
#Ejercicio N°3

#3.Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
altura = int(input("Ingresa la altura del triángulo: "))
for i in range(1, altura + 1):
    print('*' * i)
    
#Ejercicio N°4

#4.Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    print(f"Tabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
    
#Ejercicio N°5

#5.Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta
contraseña = "contraseña"
while True:
    intento = input("Introduce la contraseña: ")
    if intento == contraseña:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        
#Ejercicio N°6

#6.Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("Programa terminado.")
        break
    print(entrada)
    
#Ejercicio N°7

#7.Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).
for i in range(2, 21, 2):
    print(i)
    
#Ejercicio N°8

#8.
#Imprime números del 1 al 100, pero:
#Para múltiplos de 3 → "Fizz".
#Para múltiplos de 5 → "Buzz".
#Para múltiplos de ambos → "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
#Ejercicio N°9

#9.Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
numeros = []
for i in range(10):
    num = int(input(f"Ingresa el número {i + 1}: "))
    numeros.append(num)
suma_ultimos_5 = sum(numeros[-5:])
print(f"La suma de los últimos 5 números es: {suma_ultimos_5}")

#Ejercicio N°10

#Realizar un programa que lea los lados de n triángulos. Informar después de cada triángulo si es equilátero (tres lados iguales), isósceles (dos lados iguales) o escaleno (ningún lado igual). Informar después del total de triángulos de cada tipo.
n = int(input("¿Cuántos triángulos deseas ingresar? "))
equilateros = 0
isosceles = 0
escaleno = 0

for i in range(n):
    print(f"Triángulo {i + 1}:")
    lado1 = float(input("Ingresa el lado 1: "))
    lado2 = float(input("Ingresa el lado 2: "))
    lado3 = float(input("Ingresa el lado 3: "))
    
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
        equilateros += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
        isosceles += 1
    else:
        print("El triángulo es escaleno.")
        escaleno += 1

print(f"Total de triángulos equiláteros: {equilateros}")
print(f"Total de triángulos isósceles: {isosceles}")
print(f"Total de triángulos escalenos: {escaleno}")