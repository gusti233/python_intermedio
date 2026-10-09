# 1. Calcular el mayor de dos números ingresados por teclado usando un operador ternario
num1 = float(input("1. Ingresá el primer número: "))
num2 = float(input("   Ingresá el segundo número: "))
mayor = num1 if num1 > num2 else num2
print(f"El mayor es: {mayor}\n")


# 2. Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
def buscar_palabra(palabra_objetivo, *args):
    # retorna un string u otro dependiendo de si la palabra está en los argumentos (args)
    resultado = "Encontrada" if palabra_objetivo in args else "No encontrada"
    return resultado

lista_palabras = input("2. Ingresá varias palabras separadas por espacio: ").split()
buscada = input("Ingresá la palabra que querés buscar: ")

print(f"Resultado: {buscar_palabra(buscada, *lista_palabras)}\n")


# 3. Determinar si un número es par o impar
num3 = int(input("3. Ingresá un número entero para saber si es par o impar: "))
par_impar = "Par" if num3 % 2 == 0 else "Impar"
print(f"El número es {par_impar}\n")


# 4. Calcular el promedio de una lista de números usando args y un operador ternario
def calcular_promedio(*args):
    # El operador ternario acá es ideal para evitar dividir por cero si la lista está vacía
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    return promedio

# Prueba rápida pasando argumentos fijos
print(f"4. El promedio de 10, 8 y 6 es: {calcular_promedio(10, 8, 6)}\n")


# 5. Imprimir un mensaje de error si no se pasan suficientes argumentos
def validar_argumentos(*args):
    # Asumimos que el mínimo de argumentos requeridos son 3
    mensaje = "Datos correctos" if len(args) >= 3 else "Error: No se pasaron suficientes argumentos"
    print(f"5. {mensaje}")

# Llamamos a la función pasándole solo 2 argumentos para forzar el error
validar_argumentos("dato1", "dato2")