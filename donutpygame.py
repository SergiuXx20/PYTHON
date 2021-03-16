import pygame
import math
import colorsys

pygame.init()

color = (255, 255, 255)
fondo = (0, 0, 0)
rgbcolor = 0

alto = 1270
ancho = 720

x_inicio = 0
y_inicio = 0

x_espacio = 10
y_espacio = 20

filas = alto // y_espacio
columnas = ancho // x_espacio
tamaño = filas * columnas

x_compensacion = columnas / 2
y_compensacion = filas / 2

#ANIMACION DE LA ROTACION
A = 0
B = 0  

#VELOCIDAD DE ROTACION, SI SE AUMENTA COMENTAR LINEAS 86 Y 87
espacio = 10
espacio_pi = 1 

#INDEX LUMINOSIDAD
simbolos = ".,-~:;=!*#$@" 

pantalla = pygame.display.set_mode((ancho, alto))

superficie = pygame.display.set_mode((ancho, alto))
#superficie = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Donut')
icono = pygame.image.load("dona.png")
pygame.display.set_icon(icono)

#FUENTE SIMBOLOS
fuente = pygame.font.SysFont('Arial', 18, bold=True)

#LINEA 48, 49 Y 52, 53, 54; HACEN REFERENCIA A LOS COLORES
def RGB(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def textoformato(letter, x_start, y_start):
    texto = fuente.render(str(letter), True, RGB(rgbcolor, 1, 1))
    superficie.blit(texto, (x_start, y_start))

#COLOR BLANCO
#def textoformato(letter, x_start, y_start):
    #texto = fuente.render(str(letter), True, color)
    #superficie.blit(texto, (x_start, y_start))

#INICIO DEL GAME LOOP
funcionando = True
while funcionando:

    pantalla.fill((fondo))

    z = [0] * tamaño #DONUT , RELLENA ESPACIO DEL DONUT
    b = [' '] * tamaño #FONDO, RELLENA EL ESPACIO VACIO

    for j in range(0, 628, espacio): #DE 0 A 2pi
        for i in range(0, 628, espacio_pi): #DE 0 A 2 PI
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_compensacion + 40 * D * (l * h * m - t * n)) #3D X COORDENADA DESPUES DE ROTACION
            y = int(y_compensacion + 20 * D * (l * h * n + t * m)) #3D Y COORDENADA DESPUES DE ROTACION
            o = int(x + columnas * y) #3D Z COORDENADA DESPUES DE ROTACION
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n)) #INDICE LUMINOSIDAD
            if filas > y and y > 0 and x > 0 and columnas > x and D > z[o]:
                z[o] = D
                b[o] = simbolos[N if N > 0 else 0]

    if y_inicio == filas * y_espacio - y_espacio:
        y_inicio = 0

    for i in range(len(b)):
        A += 0.00002 #PARA QUE ROTE MAS RAPIDO CAMBIAR A 0.0002
        B += 0.00001 #PARA QUE ROTE MAS RAPIDO CAMBIAR A 0.0001
        if i == 0 or i % columnas:
            textoformato(b[i], x_inicio, y_inicio)
            x_inicio += x_espacio
        else:
            y_inicio += y_espacio
            x_inicio = 0
            textoformato(b[i], x_inicio, y_inicio)
            x_inicio += x_espacio


    pygame.display.update()

    rgbcolor += 0.005 #COLORES RGB INCREMENTADOS

#FIN DEL GAME LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            funcionando = False

