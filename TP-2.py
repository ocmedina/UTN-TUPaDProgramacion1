#Ejercicio N°1

#pedir el ancho y alto de un rectangulo
ancho = float(input("Ingrese el ancho del rectángulo: "))
alto = float(input("Ingrese el alto del rectángulo: "))
ancho = ancho * 2
alto = alto * 2
print("El nuevo ancho es:", ancho)
print("El nuevo alto es:", alto)

#Ejercicio N°2
#Convertir grados Celsius a Fahrenheit

grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
grados_fahrenheit = (grados_celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {grados_fahrenheit:.2f}")

#Ejercicio N°3
#Uso de booleanos 

a = True
b = False

print(a and b)
print(a or b)
print(not a)    
print(not b)

#Ejercicio N°4
a = 5
b = 3
c = a + b
a= 2

print(c)

#El resultado de la suma es: 8
#Porque c se calculó cuando a valía 5 y b valía 3, así que c quedó con el valor 8.

#Ejercicio N°5

#Pedir un número al usuario
numero = float(input("Ingrese un número: "))
numero = numero ** 2
print("El cuadrado del número es:", numero)

#Ejercicio N°6

# 1. Declarar variables
x = 10
y = 20

print("Antes del intercambio:")
print("x =", x, "y =", y)

# 2. Intercambiar usando operaciones aritméticas
x = x + y  # ahora x = 30
y = x - y  # ahora y = 10
x = x - y  # ahora x = 20

# 3. Mostrar después del intercambio
print("Después del intercambio:")
print("x =", x, "y =", y)


#Ejercicio N°7

# 1. Solicitar datos al usuario
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# 2. Calcular el IMC
imc = peso / (altura ** 2)

# 3. Mostrar resultado
print("Tu IMC es:", round(imc, 2))

#Ejercicio N°8

# 1. Pedir el nombre completo
nombre = input("Ingrese su nombre completo: ")

# 2.a Cantidad de letras sin contar espacios
cantidad_letras = len(nombre.replace(" ", ""))

# 2.b Primeras 3 letras
primeras_tres = nombre[:3]

# 2.c Nombre alternando mayúsculas y minúsculas (versión simple con .title())
alternado = nombre.title()  # ejemplo: "Juan Perez"

# 3. Mostrar resultados
print("Cantidad total de letras (sin espacios):", cantidad_letras)
print("Primeras 3 letras:", primeras_tres)
print("Nombre alternado:", alternado)

#Ejercicio N°9

# 1. Declarar variables
a = 7.5
b = 3.2

# 2. Operaciones
suma = a + b
division = round(a / b, 2)
potencia = a ** b

# 3. Mostrar resultados
print("Suma:", suma)
print("División redondeada a 2 decimales:", division)
print("Potencia:", potencia)

#Ejercicio N°10

# 1. Pedir el precio original
precio_original = float(input("Ingrese el precio original del producto: "))

# 2. Pedir el porcentaje de descuento
descuento = float(input("Ingrese el porcentaje de descuento: "))

# 3. Calcular el precio final
precio_final = precio_original * (1 - (descuento / 100))

# 4. Mostrar el precio con descuento
print("El precio con descuento es:", round(precio_final, 2))


