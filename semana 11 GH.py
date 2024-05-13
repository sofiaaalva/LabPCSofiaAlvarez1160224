print("Semana No. 11: Ejercicio 1")
n = int(input("Ingrese un número mayor a 0"))
if (n <= 0):
 print("Error, debe ser mayor a 0")
#Definición de variables
a = 0
b = 1
c = 0
i = 2
resultado = " "
if (n > 0):
 resultado = str(a)
 if (n > 1):
 resultado += ", " + str(b)
 print(resultado)
 while(i < n):
 c = a + b
 resultado += " , " + str(b)
 a = b
 b = c
 i = i + 1
 #print ("Adentro ciclo:" , resultado)
 print(resultado)
else:
 print(resultado)
#Actividad 2
print("Semana No. 11: Ejercicio 2")
n2 = int(input("Ingrese un número mayor a 0: "))
if (n2 <= 0):
 print("Error, debe ser mayor a 0")
#Inciso A
resultadoA = 0
for x in range(1, n2 + 1):
 resultadoA += 1/x
print("Inciso A:", resultadoA)
ResultadoB = 0
for i in range(1, n2 + 1):
 ResultadoB += 1 / (2 ** i)
print("Inciso B:", ResultadoB)
ResultadoC = 0
for k in range(n2 + 1):
 ResultadoC += (x**k) / (a**k)
print("Inciso C:", ResultadoC)