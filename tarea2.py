
'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
'''

def dividir(a: float,b: float)-> float | None: 
    # Intenta dividir dos numeros, si no puede, captura la excepcion si el divisor es cero
    try: 
        resultado= a/b 
    except ZeroDivisionError: 
        print("Error - No se puede dividir por cero ")
    else: 
        return resultado 
 
resultado = dividir(10, 0)
print(f"Resultado de la division: {resultado} \n")


'''
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
'''

def sumar(a:float, b:float) -> float | None: 
    try: 
        resultado= a+b
    except TypeError: 
        print("Error - Solo se pueden ingresar valores numericos") 
    else: 
        return resultado 

resultado = sumar(50,'hola mundo') 
print(f"Resultado de la suma: {resultado} \n ")

'''
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

'''
diccionario = {'Nombre': 'Tomas', 'Edad': '18', 'Ciudad': 'Corrientes'}

def acceder_diccionario(a: dict, clave: str)-> str | None: 
  
    try: 
        var= diccionario[clave] 
    except KeyError: 
        print('Error - Clave ingresada no es valida')
    else: 
        return var 

print(acceder_diccionario(diccionario, 'fallo'), '\n') 

'''Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.'''
        
nombre_archivo = "prueba.txt"

try:
    # Abro el archivo en modo letura ('r')
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Archivo abierto correctamente.")

except FileNotFoundError:
    # Si el archivo no existe, muestro el error y lo creo en modo escritura ('w')
    print("Error: El archivo no existe. Creando uno nuevo...")
    
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Este es un archivo nuevo creado automáticamente.\n")
        
    print("El archivo ha sido creado con éxito.")

'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario
'''

def dividir_numeros(valor1, valor2):
    try:
        # cconvertir los valores a números y dividirlos
        numero1 = float(valor1)
        numero2 = float(valor2)
        
        resultado = numero1 / numero2
        print(f"El resultado es: {resultado}")

    except ValueError:
        print("Error: El valor ingresado no es un número válido.")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Primera pueba: división exitosa
dividir_numeros(10, 2)

# Segunda prueba: provoca un ValueError (pasamos texto en lugar de número)
dividir_numeros("hola", 5)

# Tercera prueba: [rovoca un ZeroDivisionError (intentamos dividir por cero)
dividir_numeros(10, 0)