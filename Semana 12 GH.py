# Menú principal
print("Semana No. 12: Ejercicio 1")
print("-" * 30)
print("Menú de opciones:")
print("a) Sumatoria")
print("b) Factorial")
print("c) Tablas de Multiplicar")
print("d) Número perfecto")
print("-" * 30)
opcion = input("Seleccione una opción (a, b, c o d): ")
# Funciones para cada opción del menú
def sumatoria():
 """
 Calcula la suma de los números desde 1 hasta un número N ingresado por el
usuario.
 """
 numero = int(input("Ingrese un número entero positivo: "))
 suma = 0
 for i in range(1, numero + 1):
 suma += i
 print(f"La suma de los números hasta {numero} es: {suma}")
def factorial():
 """
 Calcula la factorial de un número N ingresado por el usuario.
 """
 numero = int(input("Ingrese un número entero positivo: "))
 if numero == 0:
 factorial = 1
 else:
 factorial = 1
 for i in range(1, numero + 1):
 factorial *= i
 print(f"El factorial de {numero} es: {factorial}")
def tablas_multiplicar():
 """
 Muestra en pantalla las tablas de multiplicar del 1 al 10.
 """
 for tabla in range(1, 11):
 print(f"Tabla del {tabla}:")
 for multiplicando in range(1, 11):
 resultado = tabla * multiplicando
 print(f"{tabla} x {multiplicando} = {resultado}")
def numero_perfecto():
 """
 Comprueba si un número N ingresado por el usuario es un número perfecto.
 """
 numero = int(input("Ingrese un número entero positivo: "))
 suma_factores = 0
 for divisor in range(1, numero):
 if numero % divisor == 0:
 suma_factores += divisor
 if suma_factores == numero:
 print(f"{numero} es un número perfecto.")
 else:
 print(f"{numero} no es un número perfecto.")
# Ejecutar la opción seleccionada
if opcion == "a":
 sumatoria()
elif opcion == "b":
 factorial()
elif opcion == "c":
 tablas_multiplicar()
elif opcion == "d":
 numero_perfecto()
else:
 print("Opción no válida.")