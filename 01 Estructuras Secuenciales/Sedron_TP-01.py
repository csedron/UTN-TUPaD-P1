#Ejericio 1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.\
print("“Hola Mundo!”")

#Ejericio 2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
#realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#Ejericio 3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar
#la impresión por pantalla.
nombre = input("Cual es tu nombre: ")
apellido = input("Como es tu apellido: ")
edad = int(input("Decime tu edad: "))
residencia = input("Cual es tu lugar de residencia: ")
print (f"Soy {nombre}, tengo {edad} y vivo en {residencia}")

#Ejericio 4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("ingrese radio de circulo: "))
pi = float(3.141)
area = pi * radio ** 2
perimetro = pi * radio * 2
print(f"el area es {area}")
print(f"El perimetro es {perimetro}")

#Ejericio 5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos =  int(input("Ingrese cantidad de segundos: "))
conversion = float(segundos/3600)
print(f"Los segundos ingresados: {segundos}, son {conversion} horas")

#Ejercicio6
numero = int(input("Ingrese numero "))
print(f"{numero} x 1 = ", (numero*1))
print(f"{numero} x 2 = ", (numero*2))
print(f"{numero} x 3 = ", (numero*3))
print(f"{numero} x 4 = ", (numero*4))
print(f"{numero} x 5 = ", (numero*5))
print(f"{numero} x 6 = ", (numero*6))
print(f"{numero} x 7 = ", (numero*7))
print(f"{numero} x 8 = ", (numero*8))
print(f"{numero} x 9 = ", (numero*9))
print(f"{numero} x 10 = ", (numero*10))

#Ejercicio 7
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = float(input("Introduzca 1er numero diferente de cero: "))
numero2 = float(input("Introduzca 2do numero diferente de cero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"la suma de ambos numeros ingresado es {suma}")
print(f"la resta de ambos numeros ingresado es {resta}")
print(f"la multiplicacion de ambos numeros ingresado es {multiplicacion}")
print(f"la division de ambos numeros ingresado es {division}")

#Ejercicio 8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))
calculoImc = peso / (altura ** 2)
print(f"El IMC corresponde a: {calculoImc}")

#Ejercicio 9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.
gradosCelsius = float(input("Introduzca la temperatura en Celsius: "))
convesrionFarenheit = (9/5 * gradosCelsius) + 32
print(f"Los grados Celsius introducidos equivalen a {convesrionFarenheit} Farenheit")

#Ejercicio 10
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
ingresoNum1 = float(input("Ingrese N 1: "))
ingresoNum2 = float(input("Ingrese N 2: "))
ingresoNum3 = float(input("Ingrese N 3: "))
promedio = (ingresoNum1 + ingresoNum2 + ingresoNum3) / 3
print(f"El promedio de los tres numeros ingresados es: {promedio}")