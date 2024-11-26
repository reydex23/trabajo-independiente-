from random import choice
from turtle import *
from freegames import floor, vector
import json

estado = {'puntaje': 0}
ruta = Turtle(visible=False)
escritor = Turtle(visible=False)
direccion = vector(5, 0)
pacman = vector(-40, -80)
fantasmas = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
tiles_iniciales = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
tiles = tiles_iniciales.copy()

def cuadrado(x, y):
    """Dibuja el mapa en (x,y)."""
    ruta.up()
    ruta.goto(x, y)
    ruta.down()
    ruta.begin_fill()
    for count in range(4):
        ruta.forward(20)
        ruta.left(90)
    ruta.end_fill()

def desplazamiento(punto):
    """Devuelve a un punto específico."""
    x = (floor(punto.x, 20) + 200) / 20
    y = (180 - floor(punto.y, 20)) / 20
    indice = int(x + y * 20)
    return indice

def valido(punto):
    """Devuelve si el punto es verdadero en el mapa."""
    indice = desplazamiento(punto)
    if tiles[indice] == 0:
        return False
    indice = desplazamiento(punto + 19)
    if tiles[indice] == 0:
        return False
    return punto.x % 20 == 0 or punto.y % 20 == 0

def mundo():
    """Ruta dibujada del mundo."""
    bgcolor('black')
    ruta.color('blue')
    for indice in range(len(tiles)):
        tile = tiles[indice]
        if tile > 0:
            x = (indice % 20) * 20 - 200
            y = 180 - (indice // 20) * 20
            cuadrado(x, y)

            if tile == 1:
                ruta.up()
                ruta.goto(x + 10, y + 10)
                ruta.dot(2, 'white')
def mover():
    """Movimiento de pacman y de todos los fantasmas."""
    escritor.undo()
    escritor.write(estado['puntaje'])
    clear()
    if valido(pacman + direccion):
        pacman.move(direccion)
    indice = desplazamiento(pacman)
    if tiles[indice] == 1:
        tiles[indice] = 2
        estado['puntaje'] += 1
        x = (indice % 20) * 20 - 200
        y = 180 - (indice // 20) * 20
        cuadrado(x, y)
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for punto, rumbo in fantasmas:
        opciones = ordenar_direcciones(punto)  # Ordenar opciones
        if valido(punto + rumbo):
            punto.move(rumbo)
        else:
            plan = choice(opciones)
            rumbo.x = plan.x
            rumbo.y = plan.y
        up()
        goto(punto.x + 10, punto.y + 10)
        dot(20, 'red')

    update()
    for punto, rumbo in fantasmas:
        if abs(pacman - punto) < 20:
            reiniciar_juego()
            return
    ontimer(mover, 100)

def ordenar_direcciones(ghost_position):
    direcciones = [
        vector(5, 0), vector(-5, 0),
        vector(0, 5), vector(0, -5)
    ]
    
    direcciones_validas = [d for d in direcciones if valido(ghost_position + d)]
    
    direcciones_validas.sort(key=lambda d: distancia(pacman, ghost_position + d))

    return direcciones_validas

def distancia(a, b):
    """Calcula la distancia de Manhattan entre dos puntos."""
    return abs(a.x - b.x) + abs(a.y - b.y)

def cambiar(x, y):
    """Cambia la dirección de pacman si es válida."""
    if valido(pacman + vector(x, y)):
        direccion.x = x
        direccion.y = y
def reiniciar_juego():
    """Reinicio del juego."""
    global tiles
    pacman.x, pacman.y = -40, -80
    fantasmas[:] = [
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]
    tiles = tiles_iniciales.copy()
    estado['puntaje'] = 0
    mundo()
    mover()

def ciclo_del_juego():
    """Bucle principal del juego."""
    reiniciar_juego()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
escritor.goto(160, 160)
escritor.color('white')
escritor.write(estado['puntaje'])
listen()
onkey(lambda: cambiar(5, 0), 'Right')
onkey(lambda: cambiar(-5, 0), 'Left')
onkey(lambda: cambiar(0, 5), 'Up')
onkey(lambda: cambiar(0, -5), 'Down')
ciclo_del_juego()
done()
