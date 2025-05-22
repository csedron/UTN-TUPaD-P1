# Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números 
# enteros entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0:
        print(f"El factorial de 0 es igual a 1")
        return 1
    else:
        resultado = factorial(n - 1) * n
        print(f"El factorial de {n} es igual a {resultado}")
        return resultado   
num = int(input("Ingresar numero: "))
factorial(num)

# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
# F(n) = F(n-1) + F(n-2), donde F(0) = 0 y F(1) = 1. 
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
ingreso_numero = int(input("Ingrese posicion para calcular serie Fibonacci: "))
print(f"El valor de la serie para el valor ingresado {ingreso_numero} es igual a {fibonacci(ingreso_numero)}")
for i in range (ingreso_numero + 1):
    print(f"F{i} = {fibonacci(i)}")

# Crea una función recursiva que calcule la potencia de un número base
# elevado a un exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1). Prueba
# esta función en un algoritmo general.
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)
base1 = int(input("Introducir base: "))
potencia1 = int(input("Introducir potencia: "))
print(potencia(base1, potencia1))

# Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto. 
def conversor(n):
    if n == 0:
        return " "
    return conversor(n // 2) + str(n % 2)
ingreso_decimal = int(input("Ingrese numero entero a convertir: "))
print(conversor(ingreso_decimal))

# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios 
# ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    # comparo primer y ultimo caracter de cadena
    elif palabra[0] != palabra[-1]:
        return False
    # slicing recursivo que elimina primer y ultimo elemento de cadena
    return es_palindromo(palabra[1:-1])
palabra = input("Ingrese una frase para ver si es o no palindromo: ")
print(es_palindromo(palabra))

# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo 
# y devuelva la suma de todos sus dígitos.      
# Restricciones: No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión. 
def suma_digitos(n):
    if n < 10:
        return n
    # recursividad para sumar los restos de n
    return suma_digitos(n // 10) + (n % 10)
ingreso = int(input("Ingrese numero para sumar sus digitos: "))
print(f"La suma de los digitos del numero ingresado es: {suma_digitos(ingreso)}")

# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el 
# siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.  
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide. 
def contar_bloques(n):
    if n == 1:
        return 1
    # recursividad para descontar 1 al ingreso de n y luego sumar el valor de n por cada recursion
    return contar_bloques(n - 1) + n
ingreso_bloques = int(input("Ingrese la cantidad de bloques para la base de la piramide: "))
print(f"La cantidad de bloques necesarios para realizar la piramide son {contar_bloques(ingreso_bloques)}")

# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero 
# positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 
def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        # saco el resto del numero  y pongo un contador para sumar las veces que aparece
        modulo = numero % 10
        contador = 0
        if modulo == digito:
            contador += 1
        # hago recursion del numero ingresado con // 10 para ir sacando 1 digito por vez
        return contador + contar_digito(numero // 10, digito)
ingreso_numero = int(input("Ingrese numero: "))
ingreso_digito = int(input("Ingrese digito: "))
print(f"El digito que introdujo {ingreso_digito}, aparece {contar_digito(ingreso_numero, ingreso_digito)} veces en el numero {ingreso_numero}")
