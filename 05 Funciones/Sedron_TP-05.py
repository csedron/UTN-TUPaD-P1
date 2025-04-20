# ejercicio 1
# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!!")
imprimir_hola_mundo()

# ejercicio 2
# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
saludar_usuario("Claudio")

# ejercicio 3
# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")
edad = int(input("Cual es tu edad: "))
residencia = input("Cual es tu residencia: ")
informacion_personal(nombre,apellido, edad, residencia)

# Ejercicio 4
import math
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    perimetro = math.pi * (radio * 2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro = math.pi * (radio * 2)
    return perimetro
ingreso = float(input("Ingrese radio: "))
area = calcular_area_circulo(ingreso)
perimetro = calcular_perimetro_circulo(ingreso)
print(f"El area del circulo es igual a {area}")
print(f"El perimetro del circulo es igual a {perimetro}")

# Ejercicio 5
# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
ingreso = segundos_a_horas(float(input("Ingrese cantidad segundos: ")))
print(f"La cantidad de segundos ingresados corresponden a {ingreso} horas.")

# Ejercicio 6
# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(1,11):
        mul = numero * i
        print(f"{numero} * {i} = {mul}")
ingreso = tabla_multiplicar(int(input("Ingrese num: ")))

# Ejercicio 7
# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.
def operaciones_basicas(a, b):
    if b != 0:
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b
        return suma, resta, multiplicacion, division
    else:
        print("Divisor no debe ser 0!!")
ingreso = operaciones_basicas(int(input("Ingrese 1er numero: ")), int(input("Ingrese 2do numero: ")))
print(f"El valor de la suma es {ingreso[0]}")
print(f"El valor de la resta es {ingreso[1]}")
print(f"El valor de la multiplicacion es {ingreso[2]}")
print(f"El valor de la division es {ingreso[3]}")

# Ejercicio 8
# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return round(imc, 2)
imc = calcular_imc(float(input("Ingrese peso: ")), float(input("Ingrese altura: ")))
print(f"Tu IMC es {imc}")

# Ejercicio 9
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    farenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} grados Celsius corresponden a {farenheit} grados Farenheit.")
celsius = celsius_a_fahrenheit(float(input("Ingrese grados Celsius para convertir a Farenheit: ")))

# Ejercicio 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.
import statistics
def calcular_promedio(a, b, c):
    promedio = statistics.mean([a, b, c])
    print(f"El promedio de los numeros ingresados es {promedio}")
ingreso = calcular_promedio(float(input("Ingrese numero 1: ")), 
                            float(input("Ingrese numero 2: ")), 
                            float(input("Ingrese numero 3: ")))