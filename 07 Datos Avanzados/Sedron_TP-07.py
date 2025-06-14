# ejercicio 1
# Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# .Naranja = 1200
# .Manzana = 1500
# .Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# ejercicio 2
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el
# códigodesarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# .Banana = 1330
# .Manzana = 1700
# .Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# ejercicio 3
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el
# código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas
# sin los precios.
lista_frutas = precios_frutas.keys()
lista_frutas = list(lista_frutas)
print(lista_frutas)

#ejercicio 4
# Escribí un programa que permita almacenar y consultar números telefónicos.
# •Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# •Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos = {}
print("CARGA DE CONTACTOS")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ").lower()  # se guarda en minúsculas
    numero = input(f"Ingresá el número de teléfono de {nombre}: ")
    contactos[nombre] = numero
print("\nCONSULTA DE NÚMERO TELEFÓNICO")
consulta = input("Ingresá el nombre del contacto que querés buscar: ").lower()
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Ese contacto no existe.")

#ejercicio 5
# Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

#ejercicio 6
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá 3 notas para {nombre}:")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
alumnos[nombre] = (nota1, nota2, nota3)
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#ejercicio 7
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
parcial1 = {30, 31, 32, 33, 34}
parcial2 = {34, 34, 36, 30}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#ejercicio 8
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 
# Diccionario inicial con productos y su stock

def leer_entero(prompt, minimo=None):
    """Pide un entero y asegura que sea >= mínimo (si se pasa)."""
    while True:
        s = input(prompt)
        try:
            v = int(s)
        except ValueError:
            print("Debe ingresar un número entero válido.")
            continue
        if minimo is not None and v < minimo:
            print(f"El valor debe ser al menos {minimo}.")
            continue
        return v

stock_productos = {
    "salame": 7,
    "harina": 15,
    "huevos": 300
}
while True:
    print('\n1- Consultar el stock de un producto')
    print('\n2- Agregar unidades al stock si el producto ya existe')
    print('\n3- Agregar un nuevo producto si no existe')
    print('\n4- Finaliza programa')
    while True:
        entrada = input("\n¿Qué desea realizar? ")
        try:
            realizar = int(entrada)
            break       # salió bien: opcion es un entero
        except ValueError:
            print("Debe ingresar un número entero (1–4). Intente de nuevo.")
    if realizar == 1:
        # ---- Consultar stock ----
        print("\nProductos disponibles:", ", ".join(stock_productos.keys()))
        prod = input("Ingrese el nombre del producto a consultar: ")
        if prod in stock_productos:
            print(f"{prod} tiene {stock_productos[prod]} unidades en stock.")
        else:
            print(f"{prod} no está en el stock.")
        input("\nPresione Enter para volver al menú…")
    
    elif realizar == 2:
        #Agregar unidades a un producto existente
        prod = input("\nIngrese el nombre del producto al que quiere sumar unidades: ")
        if prod in stock_productos:
            qty = leer_entero(f"¿Cuántas unidades desea agregar a {prod}? ", minimo=1)
            stock_productos[prod] += qty
            print(f"Stock de {prod} actualizado: {stock_productos[prod]} unidades.")
        else:
            print(f"{prod} no existe en el stock. Use la opción 3 para crearlo.")
        input("\nPresione Enter para volver al menú…")
        
    elif realizar == 3:
        #Agregar un nuevo producto
        prod = input("\nIngrese el nombre del nuevo producto: ")
        if prod not in stock_productos:
            qty = leer_entero(f"¿Cuántas unidades tendrá {prod}? ", minimo=0)
            stock_productos[prod] = qty
            print(f"Producto {prod} agregado con {qty} unidades.")
        else:
            print(f"{prod} ya existe en el stock con {stock_productos[prod]} unidades.")
        input("\nPresione Enter para volver al menú…")

    elif realizar == 4:
        print('Gracias! vuelva pronto!')
        break
    else:
        print('Opcion incorrecta, vuelta a elegir!')

#ejericio 9
# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo: 
# Permití consultar qué actividad hay en cierto día y hora. 
agenda = {
    ("lunes",  "09:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("lunes",  "14:30"): "Entregar TP programacion",
    ("miércoles", "11:00"): "Estudiar y practicar mas!!"
}
DIAS_SEMANA = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
print("AGENDA ORDENADA:\n")
for dia in DIAS_SEMANA:
    horas = []
    for (d, h), evento in agenda.items():
        if d == dia:
            horas.append(h)
    if horas:
        horas.sort()
        for h in horas:
            print(f"{dia.title()} a las {h} → {agenda[(dia, h)]}")

#ejericio 10
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 
paises = {
    "Argentina": "Buenos Aires",
    "Canada": "Ottawa",
    "Colombia": "Bogota",
    "Peru": "Lima"    
}
paises_invertidos = {}
for pais, capital in paises.items():
    paises_invertidos[capital] = pais
print("Diccionario original:", paises)
print("Diccionario invertido:", paises_invertidos)