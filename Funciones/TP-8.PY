
#TP-8: Funciones - MEDINA OCTAVIO


#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
 print("Hola Mundo!")

imprimir_hola_mundo()


#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
 print(f"Hola {nombre}!")
 
nombre=input("Ingrese su nombre: ")
saludar_usuario(nombre)


#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre,appelido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    

nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su appelido:")
edad=int(input("Ingrese su edad:"))
residencia=input("Ingese su lugar de residencia:")
informacion_personal(nombre,apellido,edad,residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio 
#al usuario y llamar ambas funciones para mostrar los resultados.
import math
def calcular_area_circulo(radio):
    area=(math.pi)*(radio**2)
    print(f"El área del circulo es de: {area}")

def calcular_perimetro_circulo(radio):
  perimetro=2*(math.pi)*radio
  print(f"El perimetro del circulo es de: {perimetro}")


radio=int(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio) 


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
 horas=segundos/3600
 print(f"{segundos} segundos equivale a {horas} horas")    

segundos=int(input("Ingrese una cantidad de segundos:"))
segundos_a_horas

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.


def tabla_multiplicar(numero):
    for i in range(11):
     print(f"{numero} * {i}: ",i*numero)
    

num=int(input("Ingrese un numero para imprimir su tabla de multiplicar:"))
tabla_multiplicar(num)  


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    
    return (suma, resta, multiplicacion, division)


a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")



#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su IMC es: {imc:.2f}")


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
 return (celsius*(9/5)+32)

temp=float(input("Ingrese su temperatura en grados Celsius: "))
fahrenheit=celsius_a_fahrenheit(temp)
print(f"{temp}°C equivale a {fahrenheit}°F")


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
  return (num1+num2+num3)/3

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

promedio=calcular_promedio(num1, num2, num3)

print("El promedio de los numeros ingresados es de: ",promedio)
