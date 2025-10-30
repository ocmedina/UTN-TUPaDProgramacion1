"TP-9 - Estructuras de Datos Complejas"


#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800

print(precios_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

frutas = list(precios_frutas.keys())
print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda[nombre] = numero
consulta = input("Ingrese el nombre del contacto a consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"No existe un contacto con el nombre {consulta}")
    
    
#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras: 
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)


print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items(): #
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
    

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Ana", "Juan", "Sofía", "Pedro", "Lucía"}
parcial2 = {"Sofía", "Pedro", "Carla", "Mateo"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock = {
    "pan": 50,
    "leche": 30,
    "queso": 20
}
print("Stock actual:", stock)

producto = input("\nIngrese el nombre del producto que desea consultar: ")


if producto in stock:
    print(f"El stock actual de '{producto}' es: {stock[producto]} unidades.")
    
    agregar = input("¿Desea agregar unidades a este producto? (s/n): ")
    if agregar == "s":
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de '{producto}': {stock[producto]} unidades.")
    else:
        print("No se realizaron cambios.")
else:
   
    print(f"El producto '{producto}' no existe en el stock.")
    agregar_nuevo = input("¿Desea agregarlo? (s/n): ")
    if agregar_nuevo == "s":
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Se agregó '{producto}' con {cantidad} unidades al stock.")
    else:
        print("No se agregó ningún producto nuevo.")

print("\nStock actualizado:", stock)


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",    
    ("Martes", "14:00"): "Cita con el dentista",
    ("Miércoles", "09:00"): "Clase de yoga",
    ("Jueves", "16:00"): "Llamada con cliente",
    ("Viernes", "12:00"): "Almuerzo con amigos"
}
dia = input("Ingrese el día de la semana: ")
hora = input("Ingrese la hora (HH:MM): ")   
clave = (dia, hora)
if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}") 
else:
    print("No hay ninguna actividad programada para ese día y hora.")
    
#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.
original = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Colombia": "Bogotá"
}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario invertido:", invertido)

    
    



    





