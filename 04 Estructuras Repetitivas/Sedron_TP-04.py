# Ejercicio 1
for i in range(0, 101):
    print(i)

# Ejercicio 2
contador = 0
num = int(input("Introduzca numero entero: "))
if num == 0:
    contador = 1
elif num > 0:
    while num > 0:
        contador += 1
        num = num // 10
else:
    num = abs(num)
    while num > 0:
        contador += 1
        num = num // 10
print(f"cantidad digitos es igual a {contador}")

# Ejercicio 3
sumatoria = 0
num1 = int(input("Introduzca primer numero entero: "))
num2 = int(input("Introduzca segundo numero entero: "))
num_menor = min(num1, num2)
num_mayor = max(num1, num2)
for i in range(num_menor + 1, num_mayor):
    sumatoria += i
print(f"El resultado es {sumatoria}")

# Ejercicio 4
acumulador = 0
num = int(input("Ingrese numero entero: "))
while num != 0:
    acumulador += num
    num = int(input("Ingrese numero entero: "))
print(f"El resultado es {acumulador}")

# Ejercicio 5
import random
aleatorio = random.randint(0, 9)
cuenta = 1
num = int(input("Adivine numero de 0 al 9: "))
while aleatorio != num:
    cuenta += 1
    print("Intente nuevamente!")
    num = int(input("Introduzca numero de 0 al 9: "))
print(f"Adivinaste! y necesitaste {cuenta} intentos!")

# Ejercicio 6
for i in range(100, -1, -2):
    print(i)
    
# Ejercicio 7
sumatoria = 0
num = int(input("Introduzca un numero positivo: "))
if num < 0:
    print("El numero introducido es menor a 0")
else:
    for i in range(0, num+1):
        sumatoria += i
print(sumatoria)

# Ejercicio 8
pares = 0
impares = 0
positivo = 0
negativo = 0
for i in range(0, 4):
    num = int(input("Introduzca 100 numeros enteros: "))
    if num > 0 and num % 2 == 0:
        positivo += 1
        pares += 1
    elif num > 0 and num % 2 != 0: 
        positivo += 1
        impares += 1
    if num < 0 and num % 2 == 0:
        negativo += 1
        pares += 1
    elif num < 0 and num % 2 != 0: 
        negativo += 1
        impares += 1
print(f"Se ingresaron {positivo} números positivos")
print(f"Se ingresaron {negativo} números negativos")
print(f"Se ingresaron {pares} números pares")
print(f"Se ingresaron {impares} números impares")

# Ejercicio 9
acumulador = 0
contador = 0
for i in range(0, 100):
    contador += 1
    num = int(input("Introduzca 100 numeros enteros: "))
    acumulador += num
media = acumulador / contador
print(f"La media de los numeros introducidos es: {media}")

# Ejercicio 10
num = int(input("Introduzca un numero entero: "))
valor_digito = 0
nuevo_num = 0
while num > 0:
    valor_digito = num % 10
    num = num // 10
    nuevo_num =  nuevo_num * 10 + valor_digito
num = nuevo_num
print(num)