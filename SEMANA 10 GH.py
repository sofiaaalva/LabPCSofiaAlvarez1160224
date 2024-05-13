    print("Semana No. 10 : Ejericicio 1")
    mesEntrada = int(input("Ingrese un número del 1-12: "))
    mesSalida = ""
    match mesEntrada:
    case 1:
    mesSalida = "Enero"
    case 2:
    mesSalida = "Febrero"
    case 3:
    mesSalida = "Marzo"
    case 4:
    mesSalida = "Abril"
    case 5:
    mesSalida = "Mayo"
    case 6:
    mesSalida = "Junio"
    case 7:
    mesSalida = "Julio"
    case 8:
    mesSalida = "Agosto"
    case 9:
    mesSalida = "Septiembre"
    case 10:
    mesSalida = "Octubre"
    case 11:
    mesSalida = "Noviembre"
    case 12:
    mesSalida = "Diciembre"
    case _:
    print("Error: El número ingresado debe de estar entre 1 y 12")
    print(f"MES: {mesSalida}")
    #Actividad 2
    print("Semana No 10: Ejercicio 2")
    a = int(input("Ingrese un primer número mayor a 0: "))
    b = int(input("Ingrese un segundo número mayor a 0: "))
    c = int(input("Ingrese un tercer número mayor a 0: "))
    if (a <= 0 or b <= 0 or c <= 0):
    print("ERROR, ingrese un numero mayor a 0")
    if a > b:
    if a > c:
    print("A es el mayor")
    else:
    if a == c:
    print("A es mayor a B, A es igual a C")
    else:
    print("A es mayor a B, A es menor a C")
    elif a == b:
    if a > c:
    print("A es igual a B, A mayor que C")
    elif a == c:
    print("A es igual a B y C")
    else:
    print("A es igual a B y menor que C")
    if b > c:
    print("B igual a A y mayor que C")
    elif b == c:
    print("B es igual a A e igual a C")
    else:
    print("B es igual a A y menor que C")
    #Actividad 3

    año = int(input("Ingrese su año de nacimiento: "))
    mes = int(input("Ingrese un número del 1-12: "))
    día = int(input("Ingrese un número del 1-31: "))
    if mes <= 0 or mes >= 12 and día <= 0 or día >= 31:
    print("Ingrese valores númericos correctos")
    else:
    if (mes == 1 and día >= 19) or (mes == 12 >= 22):
    print("Su signo es Capricornio")
    if (mes == 1 and día >= 20) or (mes == 2 <= 22):
    print("Su signo es Acuario")
    else:
    if (mes == 2 and día >= 19) or (mes == 3 <= 20):
    print("Su signo es Piscis")
    if (mes == 3 and día >= 21) or (mes == 4 <= 19):
    print("Su signo es Aries")
    else:
    if (mes == 4 and día >= 20) or (mes == 5 <= 20):
    print("Su signo es Tauro")
    if (mes == 5 and día >= 21) or (mes == 6 <= 20):
    print("Su signo es Géminis")
    else:
    if (mes == 6 and día >= 21) or (mes == 7 <= 22):
    print("Su signo es Cancer")
    if (mes == 7 and día >= 23) or (mes == 8 <= 22):
    print("Su signo es Leo")
    else: 
    if (mes == 8 and día >= 23) or (mes == 9 <= 22):
    print("Su signo es Virgo")
    if (mes == 9 and día >= 23) or (mes == 10 <= 22):
    print("Su signo es Libra")
    else:
    if (mes == 10 and día >= 23) or (mes == 11 <= 21):
    print("Su signo es Escorpio")
    if (mes == 11 and día >= 22) or (mes == 12 <= 21):
    print("Su signo es Sagitario")