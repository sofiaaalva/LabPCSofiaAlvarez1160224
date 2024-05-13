import turtle
import os
from scene_1 import scene_1
from scene_2 import scene_2
from scene_3 import scene_3
from scene_4 import scene_4
from scene_5 import scene_5

# Estructura de preguntas y respuestas para cada secuencia
preguntas = [
    {
        "pregunta": "¿Cuál es el océano de Mariana?",
        "opciones": ["A) Pacífico", "B) Atlántico", "C) Índico"],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿Los delfines eran juguetones?",
        "opciones": ["A) No", "B) Sí", "C) No sé"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Por qué se maravilló marina?",
        "opciones": ["A) Por los colores", "B) Por sus amigos", "C) Por la belleza del arrecife"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿La ballena es jorobada",
        "opciones": ["A) No sé", "B) Sí", "C) No"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Los delfines estaban tristes?",
        "opciones": ["A) Estaban contentos", "B) No", "C) Sí"],
        "respuesta_correcta": "C"
    },
    # Agrega más preguntas para cada secuencia...
]

# Constantes
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
POSICION_INICIAL_TEXTO = (-400, 300)
POSICION_INICIAL_NARRATIVA = (-420, -280)
ANCHO_RECTANGULO = 800
ALTO_RECTANGULO = 400

#variables generales
respuestas_correctas = 0


#limpiar la pantalla de la consola dependiendo si es GNU Linux o cualquier Unix y windows

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def pedir_datos_niño():
    print("Bienvenido al programa de cuentos infantiles.")
    
    # Validación del nombre del niño
    while True:
        nombre = input("Por favor, ingresa el nombre del niño: ")
        if nombre.isalpha():  # Comprueba si todos los caracteres son letras
            break
        else:
            print("Por favor, ingresa un nombre válido sin números ni caracteres especiales.")

    # Validación de la edad del niño
    while True:
        edad = input("Por favor, ingresa la edad del niño: ")
        if edad.isdigit():  # Comprueba si todos los caracteres son dígitos
            break
        else:
            print("Por favor, ingresa una edad válida (números enteros).")

    # Validación del color favorito del niño
    colores_validos = ["red", "blue", "green", "yellow", "purple"]
    while True:
        color_favorito = input("Por favor, ingresa el color favorito del niño (entre red, blue, green, yellow o purple): ")
        if color_favorito.lower() in colores_validos:
            break
        else:
            print("Por favor, ingresa un color válido de la lista proporcionada.")

    return nombre, edad, color_favorito

def mostrar_secuencia_con_cuestionario(secuencia, pantalla, t, nombre, idx_secuencia):
    clear()

    #hacer global respuestas_correctass

    global respuestas_correctas
    # Limpiar pantalla
    t.clear()

    # Mostrar el título de la secuencia
    t.goto(POSICION_INICIAL_TEXTO)
    t.color("black")
    t.write(secuencia["titulo"], font=("Arial", 18, "bold"))
    t.color("black")

    # Llamar a la escena correspondiente según la secuencia
    if secuencia["titulo"] == "El Viaje de la Tortuga Marina - El Comienzo del Viaje":
        scene_1(t, ANCHO_RECTANGULO, ALTO_RECTANGULO,
                color_favorito_niño)  # Llamar a la función scene_1 para dibujar la primera escena
    elif secuencia["titulo"] == "El Viaje de la Tortuga Marina - El Encuentro con los Delfines Juguetones":
        scene_2(t, ANCHO_RECTANGULO, ALTO_RECTANGULO,
                color_favorito_niño)  # Llamar a la función scene_2 para dibujar la segunda escena
    elif secuencia["titulo"] == "El Viaje de la Tortuga Marina - La Travesía por el Arrecife de Coral":
        scene_3(t, ANCHO_RECTANGULO, ALTO_RECTANGULO,
                color_favorito_niño)  # Llamar a la función scene_3 para dibujar la tercera escena
    elif secuencia["titulo"] == "El Viaje de la Tortuga Marina - El Encuentro con la Ballena Cantante":
        scene_4(t, ANCHO_RECTANGULO, ALTO_RECTANGULO, color_favorito_niño)
    elif secuencia["titulo"] == "El Viaje de la Tortuga Marina - El Regreso a Casa":
        scene_5(t, ANCHO_RECTANGULO, ALTO_RECTANGULO)

    # Mostrar la narrativa de la secuencia
    t.goto(POSICION_INICIAL_NARRATIVA)
    t.color("black")
    t.write(secuencia["narrativa"].format(nombre_niño=nombre), font=("Arial", 12), align="left")

    
    ## mostrar las preguntas y si no el usuario no contesta la opcion correcta entonces NO avanza la siguiente escena 


    respuesta_es_correcta = False

    if(respuesta_es_correcta):
        return
    

    # pregunta = preguntas[idx_secuencia]

    while respuesta_es_correcta == False: 
        print(preguntas[idx_secuencia]["pregunta"])
        for opcion in preguntas[idx_secuencia]["opciones"]:
            print(opcion)
        respuesta = input("Introduce tu respuesta: ").upper()
        if respuesta == preguntas[idx_secuencia]["respuesta_correcta"]:
            print("Correcto!")
            respuestas_correctas += 1
            respuesta_es_correcta = True
            break
        else:
            print("Incorrecto. Inténtalo de nuevo.")
    

def mostrar_cuento(secuencias, nombre):
    # Configurar la ventana de Turtle
    pantalla = turtle.Screen()
    pantalla.setup(width=ANCHO_VENTANA, height=ALTO_VENTANA)
    pantalla.title("Cuento Infantil")
    # Crear un objeto Turtle para dibujar
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.goto(-200, 200)
    t.hideturtle()

    # Función para mostrar la secuencia actual con el cuestionario
    def mostrar_secuencia_con_cuestionario_actual():
        mostrar_secuencia_con_cuestionario(secuencias[idx_secuencia], pantalla, t, nombre, idx_secuencia)
        avanzar_cuento()

    # Función para avanzar al siguiente cuento
    def avanzar_cuento():
        nonlocal idx_secuencia
        idx_secuencia += 1
        if idx_secuencia < len(secuencias):
            mostrar_secuencia_con_cuestionario_actual()
        else:
            mostrar_resultados()

    def mostrar_resultados():
        print("¡Cuento completado!")
        print(f"Puntaje final: {respuestas_correctas}/{len(preguntas)}")
        if respuestas_correctas >= len(preguntas) / 2:
            print("¡Felicidades! Has contestado más de la mitad de las preguntas correctamente. ¡Eres genial!")
        else:
            print("¡Ánimo! Puedes intentarlo de nuevo y mejorar en la próxima vez.")
            turtle.done()
            pantalla.bye()

    idx_secuencia = 0
    mostrar_secuencia_con_cuestionario_actual()

# Pedir datos del niño
nombre_niño, edad_niño, color_favorito_niño = pedir_datos_niño()
print("Nombre del niño:", nombre_niño)
print("Edad del niño:", edad_niño)
print("Color favorito del niño:", color_favorito_niño)

#array con cada narrativa

tortugaMarina = [
    {
        "titulo": "El Viaje de la Tortuga Marina - El Comienzo del Viaje",
        "narrativa": f"""
        En las cálidas aguas del océano Pacífico, vivía una tortuga marina llamada Marina. Marina siempre
        había soñado con explorar el vasto océano y descubrir nuevos lugares. Un día, decidió que era hora
        de emprender su gran aventura con su gran amigo {nombre_niño}.
    """
    },
    {
        "titulo": "El Viaje de la Tortuga Marina - El Encuentro con los Delfines Juguetones",
        "narrativa": f"""
        Marina nadaba felizmente por el océano junto con {nombre_niño} cuando de repente se encontró con un grupo
        de delfines juguetones. Los delfines la saludaron con alegría y le preguntaron a dónde se dirigía. Marina
        les contó sobre su viaje y los delfines se ofrecieron a acompañarla en su travesía.
        """
    },
    {
        "titulo": "El Viaje de la Tortuga Marina - La Travesía por el Arrecife de Coral",
        "narrativa": f"""
        Juntos, Marina, los delfines y {nombre_niño} nadaron hacia el arrecife de coral, un lugar lleno de colores
        y vida marina. Mientras exploraban el arrecife, vieron peces de todos los tamaños y colores, así como hermosas
        plantas marinas. Marina se maravilló ante la belleza del arrecife y se sintió agradecida por tener la oportunidad
        de verlo.
        """
    },
    {
        "titulo": "El Viaje de la Tortuga Marina - El Encuentro con la Ballena Cantante",
        "narrativa": f"""
        Mientras continuaban su viaje, se encontraron con una ballena jorobada que cantaba melodías hermosas. 
        La ballena les contó historias sobre sus viajes por los océanos del mundo y les enseñó canciones que 
        habían pasado de generación en generación. Marina los delfines y {nombre_niño} se unieron a la ballena
        en su canción y juntos crearon una sinfonía submarina.
        """
    },
    {
        "titulo": "El Viaje de la Tortuga Marina - El Regreso a Casa",
        "narrativa": f"""
        Después de muchas aventuras emocionantes, Marina decidió que era hora de regresar a casa. Los delfines y {nombre_niño}
        la acompañaron de vuelta a las cálidas aguas del océano Pacífico, donde se despidieron con tristeza pero con
        la  promesa de volver a encontrarse algún día. Marina regresó a su hogar con el corazón lleno de recuerdos
        felices y la satisfacción de haber cumplido su sueño de explorar el océano.
        """
    }
]

# Mostrar el cuento
mostrar_cuento(tortugaMarina, nombre_niño)