tablero = [[' '] * 8 for _ in range(8)]

tablero.insert(0, [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
for i in range(1, 9):
    tablero[i].insert(0, str(9 - i))


def tablero_de_ajedrez_imprimir():
    print("   ╭───────────────────────────────╮")
    for i in range(1, 9):  
        filas = f" {9 - i} ┃"  
        for j in range(1, 9):
            celdas_del_tablero = tablero[i][j]
            filas += f" {celdas_del_tablero} ┃" if celdas_del_tablero != ' ' else "   ┃"
        print(filas)
        if i < 8:
            print("   ├───────────────────────────────┤")
    print("   ╰───────────────────────────────╯")
    print("     A   B   C   D   E   F   G   H")


def meter_pieza(tipo, color, posicion):
    letra, numero = posicion
    x = ord(letra) - ord('a') + 1
    y = 9 - int(numero)  
    if tablero[y][x] != ' ':
        return "Ya hay una pieza en esa posición."
    tablero[y][x] = tipo[0] + color[0]  
    return "Pieza agregada exitosamente."

def validar_movimientos(posicion, color):
    letra, numero = posicion
    x = ord(letra) - ord('a') + 1
    y = 9 - int(numero)  

    movimientos = [[x + 2, y + 1], [x + 2, y - 1], [x - 2, y + 1], [x - 2, y - 1],
                   [x + 1, y + 2], [x + 1, y - 2], [x - 1, y + 2], [x - 1, y - 2]]

    movimientos_validos = []
    for mov in movimientos:
        nx, ny = mov
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            pieza_destino = tablero[ny][nx]
            if pieza_destino == ' ':
                movimientos_validos.append((chr(nx + ord('a') - 1), 9 - ny, "vacía"))
            elif pieza_destino != ' ' and pieza_destino[1] != color[0]:  
                movimientos_validos.append((chr(nx + ord('a') - 1), 9 - ny, f"con {pieza_destino[0]}"))

    return movimientos_validos

def insercion_de_pieza():
    while True:
        n = input("Ingrese el número de piezas a agregar: ")
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        else:
            print("Ingrese un número entero positivo.")

    for _ in range(n):
        tipo = input("Tipo de pieza (alfil, peon, caballo, torre, rey, dama): ").lower()
        while tipo not in ['alfil', 'peon', 'caballo', 'torre', 'rey', 'dama']:
            print("Tipo de pieza no válido. Intente de nuevo.")
            tipo = input("Tipo de pieza: ").lower()

        color = input("Color de la pieza (blanco o negro): ").lower()
        while color not in ['blanco', 'negro']:
            print("Color no válido. Intente de nuevo.")
            color = input("Color de la pieza: ").lower()

        posicion = input("Posición de la pieza (ej. a1, e4, f8): ").lower()
        while not (len(posicion) == 2 and 'a' <= posicion[0] <= 'h' and '1' <= posicion[1] <= '8'):
            print("Formato de posición no válido. Intente de nuevo.")
            posicion = input("Posición de la pieza: ").lower()

        mensaje = meter_pieza(tipo, color, posicion)
        print(mensaje)

def ingresar_caballo():
    posicion = input("Ingrese la posición del caballo a evaluar: ").lower()
    while not (len(posicion) == 2 and 'a' <= posicion[0] <= 'h' and '1' <= posicion[1] <= '8'):
        print("Formato de posición no válido. Intente de nuevo.")
        posicion = input("Posición del caballo: ").lower()

    color = input("Ingrese el color del caballo (blanco o negro): ").lower()
    while color not in ['blanco', 'negro']:
        print("Color no válido. Intente de nuevo.")
        color = input("Color del caballo: ").lower()

    mensaje = meter_pieza("caballo", color, posicion)
    print(mensaje)
    if mensaje == "Pieza agregada exitosamente.":
        movimientos = validar_movimientos(posicion, color)
        print("Los posibles movimientos del caballo son:")
        for i in range(len(movimientos)):
            mov = movimientos[i]
            print(f"{i+1}. {mov[0]}{mov[1]}, {mov[2]}")

if __name__ == "__main__":
    tablero_de_ajedrez_imprimir()
    insercion_de_pieza()
    ingresar_caballo()
    tablero_de_ajedrez_imprimir()