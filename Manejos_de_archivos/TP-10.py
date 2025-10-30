"TP-10 - Manejo de Archivos"

#Actividades:
#1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.
#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.
#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.
#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

# productos_app.py

#1. Crear archivo inicial con productos:
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Regla,180,45\n")
    archivo.write("Cuaderno,200,25\n")

#2 y 4. Leer, mostrar y cargar productos en lista de diccionarios:
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

#3. Agregar productos desde teclado:
while True:
    print("\nAgregar un nuevo producto:")
    nombre = input("Nombre del nuevo producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo_producto)

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print("Producto agregado correctamente.")

    continuar = input("\n¿Desea agregar otro producto? (s/n): ")
    if continuar != "s":
        break


#5. Buscar producto por nombre:
print("\nBuscar producto por nombre")
buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for p in productos:
    if p["nombre"] == buscar:
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nEl producto no existe en la lista.")

#6. Guardar los productos actualizados (sobrescribir el archivo)
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado correctamente.")