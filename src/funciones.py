import pygame
from random import randint
from classItem import Coin, Projectile

'''------------------------ COLISIONES --------------------------------'''

def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def detectar_colision(rect_1, rect_2):
    for r1, r2 in [(rect_1,rect_2),(rect_2,rect_1)]:
        if punto_en_rectangulo(r1.topleft,r2) or \
            punto_en_rectangulo(r1.topright,r2) or \
            punto_en_rectangulo(rect_1.bottomleft, r2) or\
            punto_en_rectangulo(rect_1.bottomright, r2):
            return True
        else:
            return False

def distancia_entre_puntos(pto_1:tuple[int, int], pto_2:tuple[int, int]) -> float :
    base = pto_1[0] - pto_2[0]
    altura = pto_1[1] - pto_2[1]
    return (base ** 2 + altura ** 2) ** 0.5

def calcular_radio(rect):
    return rect.width // 2

def detectar_colision_circulo(rect_1, rect_2) -> bool :
    r1 = calcular_radio(rect_1)
    r2 = calcular_radio(rect_2)
    base = rect_1.centerx - rect_2.centerx
    altura = rect_1.centery - rect_2.centery
    distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
    return distancia <= r1 + r2

'''------------------------ CARGAR LISTAS --------------------------------'''

def cargar_coins (cantidad: int, width, height) -> list:
    coin_list = []
    for i in range (cantidad):
        coin = Coin ((20,20), (randint(25,width-25),randint(25,height-25)), r"src\coin.png")
        coin_list.append(coin)
    return coin_list


'''---------------------------- FUENTE --------------------------------------'''

def fuente(tamaño_fuente: int, nombre_fuente : str = None) -> pygame.font.Font:
    """
    Crea y devuelve una fuente de Pygame con el tamaño especificado.

    Args:
        tamaño_fuente (int): El tamaño de la fuente a crear.
        nombre_fuente (str): Nombre de la fuente que se va a utilizar, si no se especifica se establece en None.

    Returns:
        pygame.font.Font: Una instancia de la fuente con el tamaño especificado.
    """
    font = pygame.font.SysFont(nombre_fuente, tamaño_fuente)
    return font

'''---------------------------- BLITEO --------------------------------------'''

def blitear_textos(screen, font, texto: str, posicion: tuple , color = (0, 0 ,0)) -> None:
    """
    Dibuja texto en pantalla en la posición especificada con la fuente y color dados.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujará el texto.
        font (pygame.font.Font): La fuente utilizada para dibujar el texto.
        texto (str): El texto que se desea dibujar.
        posicion (tuple): Coordenadas donde comenzará a dibujar el texto.
    """
    if type (texto) != str:
        texto = str(texto)
    textos = font.render (texto, True, color)
    screen.blit (textos, posicion)

def blitear_imagen(screen, path, dimension: tuple, posicion: tuple) -> None:
    """
    Dibuja una imagen en pantalla en la posición especificada con el tamaño dado.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujará la imagen.
        path (str): La ruta del archivo de imagen que se desea dibujar.
        dimension (tuple): Dimensión de la imagen después de ser escalada.
        posicion (tuple): Coordenadas donde se dibujará la imagen.
    """
    imagen_surface = pygame.image.load (path)
    imagen_surface = pygame.transform.scale (imagen_surface, dimension)
    screen.blit (imagen_surface, posicion)
