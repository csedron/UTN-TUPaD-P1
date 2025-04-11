# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Introduzca su edad: "))
if edad >= 18:
    print(f"Tu edad es {edad} y por ende eres mayor de edad.")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar 
# por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Ingrese nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje 
# "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese número par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

verificoEdad = int(input("Ingrese su edad: "))
if verificoEdad > 0 and verificoEdad < 12:
    print("nino")
elif verificoEdad >= 12 and verificoEdad < 18:
    print("adolescente")
elif verificoEdad >= 18 and verificoEdad < 30:
    print("adulto joven")
else:
    print("adulto")
    
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
# imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos 
# que tiene un iterable tal como una lista o un string.

password = input("Introduzca contraseña: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
import random 
from statistics import mode, median, mean 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string 
# tal cual lo ingresó el usuario e imprimirlo por pantalla. 
frase = input("introduzaca una frase o palabra: ")
# if frase[-1] == "a" or frase[-1] == "A" or frase[-1] == "e" or frase[-1] == "E" or frase[-1] == "i" or frase[-1] == "I" or frase[-1] == "o" or frase[-1] == "O" or frase[-1] == "u" or frase[-1] == "U":
if frase[-1] in "aeiouAEIOU":
    print(f"{frase}!")
else:
    print(frase)

# Ejercicio 8
ingresoNombre = input("Ingrese su nombre: ")
eleccion = int(input("Ingrese: 1 para poner en mayusculas \n         2 para poner en minusculas \n         3 para primer letra en mayusculas \n"))
if eleccion == 1:
    print(f"Se convierte nombre introducido en mayusculas, {ingresoNombre.upper()}")
elif eleccion == 2:
    print(f"Se convierte nombre introducido en minusculas, {ingresoNombre.lower()}")
elif eleccion == 3:
    print(f"Se convierte nombre introducido con la primera letra mayúscula, {ingresoNombre.title()}")
else:
    print("Opcion incorrecta!!")

# Ejercicio 9
print("Este programa clasifica la magnitud de un terremoto \n")
magnitud = float(input("Introduzca magnitud de terremoto:  \n"))
if 0 <= magnitud < 3:
    print('"Muy leve" (imperceptible).')
elif 3 <= magnitud < 4:
    print('"Leve" (ligeramente perceptible).')
elif 4 <= magnitud < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
elif 5 <= magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles).')
elif 6 <= magnitud < 7:
    print('"Muy Fuerte" (puede causar daños significativos).')
elif 7 <= magnitud <= 10:
    print('"Extremo" (puede causar graves daños a gran escala).')
else:
    print("Numero introducido no pertenece a ninguna categoria de la escala de Richter")

# Ejercicio 10
hemisferio = input("indicar hemisferio norte con N, y hermisferio sur con S: ")
mes = int(input("Introduzca mes de año: "))
dia = int(input("Introduzca que dia es: "))
if hemisferio in "nN":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Ud. se encuentra en Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Ud. se encuentra en Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Ud. se encuentra en Verano")
    else:
        print("Ud. se encuentra en Otoño")
elif hemisferio in "sS":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Ud. se encuentra en Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Ud. se encuentra en Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Ud. se encuentra en Invierno")
    else:
        print("Ud. se encuentra en Primavera")
else:
    print("opcion ingresada incorrecta")
