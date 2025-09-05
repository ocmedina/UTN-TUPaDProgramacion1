#TP-4 Estructuras_Condicionales

#Alumno: Octavio Medina


#Ejercicio N°1

#Lee el siguiente código y explica qué hace:
contrasena_correcta = "programacion1"
contrasena_usuario = input("Introduce la contraseña: ")
if contrasena_usuario == contrasena_correcta:
 print("Contraseña correcta. Bienvenido.")
else:
 print("Contraseña incorrecta. Intenta de nuevo.")
 
 # El código pide una contraseña al usuario y la compara con una contraseña predefinida.
 #Si las contraseñas coinciden, muestra "Contraseña correcta. Bienvenido.".
 #Si no, muestra "Contraseña incorrecta. Intenta de nuevo."
 
 #¿Cómo mejorarías el programa para dar más intentos?

contrasena_correcta = "programacion1"
contrasena_usuario = input("Introduce la contraseña")
if contrasena_usuario == contrasena_correcta:
 print("Contraseña correcta. Bienvenido.")
else:
    for intento in range(2):  # Permitir 2 intentos adicionales
        contrasena_usuario = input("Contraseña incorrecta. Intenta de nuevo: ")
        if contrasena_usuario == contrasena_correcta:
            print("Contraseña correcta. Bienvenido.")
            break
    else:
        print("Has agotado todos los intentos. Acceso denegado.")
#Ejercicio N°2

#¿Cómo manejarías vocales acentuadas (á, é)?

#Incluiría las vocales acentuadas en la lista de vocales para que sean reconocidas correctamente.

vocal = input("Ingresa una letra: ").lower()
if vocal in "aeiouáéíóú":
    print("Es una vocal")
else:
    print("No es una vocal")

#¿Qué estructura usarías para simplificar las comparaciones?

#La mejor estructura seria usar el operador "in" para verificar si el carácter es una vocal.

vocal = input("Ingresa una letra: ").lower()
if vocal in "aeiouáéíóú":
    print("Es una vocal")
else:
    print("No es una vocal")
    

#Ejercicio N°3

num = int(input("Ingresa un número: "))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#¿Qué ocurre si el usuario ingresa un texto?

#el programa no maneja la entrada de texto y puede fallar al intentar convertirlo a número.

#¿Cómo adaptarías el código para números decimales?

#Usaría float() en lugar de int() para permitir números decimales.
num = float(input("Ingresa un número: "))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#Ejercicio N°4

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El número {num2} es mayor que {num1}")
else:
    print("Ambos números son iguales")
    
#¿Cómo modificarías el programa para comparar más de dos números?
#Usaría una lista para almacenar los números y luego usaría la función max() para encontrar el mayor.

numeros = []
cantidad = int(input("¿Cuántos números quieres comparar? "))
for i in range(cantidad):
    num = float(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)
mayor = max(numeros)
print(f"El número mayor es: {mayor}")

#¿Qué pasa si se ingresan valores no numéricos?
#El programa fallará al intentar convertir la entrada a número. 

#Ejercicio N°5

temperatura = float(input("Ingresa la temperatura en grados Celsius: "))
if temperatura <= 10:
    print("Hace frío")
elif 10 < temperatura <= 25: 
    print("Está templado")
else:
    print("Hace calor")
    
#¿Cómo adaptarías el programa para usar °F?
#Usaría la fórmula de conversión de Celsius a Fahrenheit: (°C * 9/5) + 32 = °F

temperatura_c = float(input("Ingresa la temperatura en grados Celsius: "))
temperatura_f = (temperatura_c * 9/5) + 32
if temperatura_f <= 50:
    print("Hace frío")
elif 50 < temperatura_f <= 75: 
    print("Está templado")
else:
    print("Hace calor")
    
#¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
#Podría agregar rangos adicionales para mayor precisión.
temperatura_c = float(input("Ingresa la temperatura en grados Celsius: "))
temperatura_f = (temperatura_c * 9/5) + 32
if temperatura_f <= 50:
    print("Hace mucho frío")
elif 50 < temperatura_f <= 75: 
    print("Hace frío")
elif 75 < temperatura_f <= 100:
    print("Está templado")
else:
    print("Hace calor")
    
#Ejercicio N°6

#Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se ingresó un año bisiesto".

año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Se ingresó un año bisiesto")
else:
    print("No es un año bisiesto")
    
#¿Por qué el año 1900 no es bisiesto?
#Porque es divisible por 100 pero no por 400.

#¿Cómo validarías que el año sea positivo?
#Agregaría una condición para verificar que el año sea mayor que 0.
año = int(input("Ingresa un año: "))
if año > 0:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("Se ingresó un año bisiesto")
    else:
        print("No es un año bisiesto")
else:
    print("Por favor, ingresa un año positivo.")
    
#Ejercicio N°7

frase = input("Ingresa una frase: ").lower()
if not frase.endswith("."):
    frase += "."
print(frase)

#¿Cómo manejarías frases que ya terminan con espacio?
if frase.endswith(" "):
    frase = frase.strip()
print(frase)

#¿Qué otros caracteres de puntuación podrías considerar?
#Puntos, comas, guiones, etc.

#Ejercicio N°8


password = input("Crea una contraseña: ")

if len(password) < 8 or len(password) > 20:
    print(" La contraseña debe tener entre 8 y 20 caracteres.")
else:
    # Verificar mayúscula
    if not any(c.isupper() for c in password):
        print(" La contraseña debe tener al menos una letra mayúscula.")
    else:
        # Verificar número
        if not any(c.isdigit() for c in password):
            print(" La contraseña debe tener al menos un número.")
        else:
            print(" La contraseña es válida.")
    
#¿Cómo añadirías la regla de usar un carácter especial?
#Usaría una condición para verificar si al menos un carácter especial está presente.

#¿Por qué es importante limitar la longitud máxima?
#Para evitar contraseñas excesivamente largas que puedan ser difíciles de manejar o recordar.

#Ejercicio N°9

# Ejercicio 9: Mejorando mensajes de error

password = input("Crea una contraseña: ")

# Verificar longitud mínima
if len(password) < 8:
    print(" La contraseña no es segura. Debe tener al menos 8 caracteres.")
# Verificar longitud máxima
elif len(password) > 20:
    print(" La contraseña no es segura. Debe tener no más de 20 caracteres.")
# Verificar mayúscula
elif not any(c.isupper() for c in password):
    print(" La contraseña no es segura. Debe tener al menos una mayúscula.")
# Verificar número
elif not any(c.isdigit() for c in password):
    print(" La contraseña no es segura. Debe tener al menos un número.")
else:
    print(" La contraseña es válida.")
    
#¿Cómo mejorarías la experiencia del usuario?
#Proporcionando mensajes de error específicos para cada regla que no se cumple.

#¿Qué otras reglas de seguridad podrías implementar?
#Incluir requisitos para caracteres especiales, evitar palabras comunes, etc.

#Ejercicio N°10

jugador1=input("Jugador 1, ingrese su jugada (piedra, papel o tijera): ").lower()
jugador2=input("Jugador 2, ingrese su jugada (piedra, papel o tijera): ").lower()

if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
    print("Jugador 1 gana")
elif jugador1==jugador2:
    print("Empate")
else:
    print("Jugador 2 gana")
    
#¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?

#Agregaría una condición para verificar si la entrada es una de las opciones permitidas.
opciones = ["piedra", "papel", "tijera"]
if jugador1 not in opciones:
    print("Entrada inválida para Jugador 1.")
if jugador2 not in opciones:
    print("Entrada inválida para Jugador 2.")

#¿Qué estructura usarías para simplificar las comparaciones?

#La mejor estructura seria usar el operador "in" para verificar si el carácter es una vocal.

if jugador1 not in opciones:
    print("Entrada inválida para Jugador 1.")
if jugador2 not in opciones:
    print("Entrada inválida para Jugador 2.")
