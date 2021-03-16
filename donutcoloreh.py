import pygame
import math
import colorsys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0  #ANIMACION DE LA ROTACION

theta_spacing = 10
phi_spacing = 1 #VELOCIDAD DE ROTACION, SI SE AUMENTA COMENTAR LINEAS 86 Y 87

chars = ".,-~:;=!*#$@" #INDEX LUMINOSIDAD

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
#display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)

# LINEA 41, 42 Y 45, 46, 47 HACEN REFERENCIA A LOS COLORES
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

#COLOR BLANCO
#def text_display(letter, x_start, y_start):
    #text = font.render(str(letter), True, white)
    #display_surface.blit(text, (x_start, y_start))


run = True
while run:

    screen.fill((black))

    z = [0] * screen_size #DONUT , RELLENA ESPACIO DEL DONUT
    b = [' '] * screen_size #FONDO, RELLENA EL ESPACIO VACIO

    for j in range(0, 628, theta_spacing): #DE 0 A 2pi
        for i in range(0, 628, phi_spacing): #DE 0 A 2 PI
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
            x = int(x_offset + 40 * D * (l * h * m - t * n)) #3D X COORDENADA DESPUES DE ROTACION
            y = int(y_offset + 20 * D * (l * h * n + t * m)) #3D Y COORDENADA DESPUES DE ROTACION
            o = int(x + columns * y) #3D Z COORDENADA DESPUES DE ROTACION
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n)) #INDEX LUMINOSIDAD
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.000002 #PARA QUE ROTE MAS RAPIDO CAMBIAR A 0.0002
        B += 0.000001 #PARA QUE ROTE MAS RAPIDO CAMBIAR A 0.0001
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator


    pygame.display.update()

    hue += 0.005 #COLOREH

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

