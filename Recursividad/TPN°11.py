#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario.
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


n = int(input("Ingrese un número entero: "))
print("Factoriales del 1 al",n,"son:")
for i in range(1, n + 1):
    print(f"El factorial de {i} es {factorial(i)}")
    

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {n}:")
for i in range(n):
    print(fibonacci(i))
    
    
#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛
#(𝑚−1).
#. Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print(f"{base} elevado a la {exponente} es igual a {resultado}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num // 2) + str(num % 2)
    
n = int(input("Ingrese un número entero positivo en base decimal: "))
binario = decimal_a_binario(n)
if binario == "":
    binario = "0"
print(f"La representación binaria de {n} es: {binario}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
 #Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    elif palabra[0] != palabra[-1]:#si la primera y ultima letra son diferentes
        return False #no es palindromo
    else:
        
        return es_palindromo(palabra[1:-1])#llama a la funcion sin la primera y ultima letra

texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo")
else:
    print(f"'{texto}' no es un palíndromo")


#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
 #    Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5)

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10) #suma el ultimo digito (n%10) y llama a la funcion con el numero sin el ultimo digito (n//10) 

numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 
#      Ejemplos: 
#contar_bloques(1)   → 1         (1) 
#contar_bloques(2)   → 3         (2 + 1) 
#contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1) 
    
niveles = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
total_bloques = contar_bloques(niveles)
print(f"El total de bloques necesarios para construir la pirámide es: {total_bloques}")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 
 #     Ejemplos: 
#contar_digito(12233421, 2)   → 3   
#contar_digito(5555, 5)       → 4   

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        contador = 1 if numero % 10 == digito else 0
        return contador + contar_digito(numero // 10, digito)#suma 1 si el ultimo digito es igual al digito buscado, y llama a la funcion con el numero sin el ultimo digito

input_numero = int(input("Ingrese un número entero positivo: "))
input_digito = int(input("Ingrese un dígito (entre 0 y 9): "))
resultado = contar_digito(input_numero, input_digito)
print(f"El dígito {input_digito} aparece {resultado} veces en el número {input_numero}.")