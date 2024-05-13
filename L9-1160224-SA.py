print('Ejercicio 1: operaciones aritméticas')

num1 = int(input('Ingrese primer número: '))
num2 = int(input('Ingrese segundo número: '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division_real = num1 / num2
division_entera = num1 // num2
division_modular = num1 % num2

print(f"Suma = {suma}")
print(f"Resta = {resta}")
print(f"Multiplicación = {multiplicacion}")
print(f"División real = {division_real}")
print(f"División entera = {division_entera}")
print(f"División modular = {division_modular}")

print("Ejercicio 2: operaciones booleanas")

print(f"{num1} > {num2} es {num1 > num2}")
print(f"{num1} < {num2} es {num1 < num2}")
print(f"{num1} == {num2} es {num1 == num2}")
print(f"{num1} != {num2} es {num1 != num2}")


print("Ejercicio 3: jerarquía de operadores")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

print(f"a * b + c = {a * b + c}")
print(f"a(b + c) = {a * (b + c)}")
print(f"a / b + c = {a / b + c}")
print(f"3a + 2b / c ^ 2 = {3 * a + 2 * b / (c ** 2)}")