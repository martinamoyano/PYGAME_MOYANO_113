import pygame
from funciones import *

fondo = pygame.image.load(r'src\fondo.png')
marco = pygame.image.load(r'src\marco_bambu.png')

#BLITEO PANTALLA GAME OVER
def gameover_screen(screen, player) -> None:
    screen.fill((255, 255, 255))
    blitear_textos(screen, fuente(70), 'Game Over', (250, 250))
    blitear_textos(screen, fuente(35), f"Score: {player.score}", (250, 350))
    
    pygame.display.flip()
    pygame.time.delay(2000)

#BLITEO PANTALLA GAME
def game_screen(screen, player, fondo, enemies_list, coin_list, projectiles_list, extra_projectiles_list, extra_lives_list, width, height, booster) -> None:
    """
    Muestra la pantalla de juego principal.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        nivel (Game): Objeto Game que representa el estado del juego.
        caja_texto (Text_box): Objeto Text_box para la caja de texto donde se ingresa la letra.
        comodin_tiempo_extra (Comodin): Objeto Comodin para el comodín de tiempo extra.
        comodin_revelar_letra (Comodin): Objeto Comodin para el comodín de revelar letra.
        comodin_multiplicar_puntos (Comodin): Objeto Comodin para el comodín de multiplicar puntos.
        matriz_letras (list): Lista de objetos Boton representando el teclado de letras.
    """
    screen.blit(fondo, (0,0))

    for enemy in enemies_list:
        if enemy.activo == True:
            enemy.enemy_sprites.draw(screen)
            # enemy2_sprites.draw(screen)  

    screen.blit(marco, (0,0))
    
    blitear_lives(screen, player)
    
    blitear_cant_projectiles(screen, player)


    blitear_textos(screen, fuente(35), f"Score: {player.score}", (600, 25))
    blitear_coins(screen, coin_list)

    
    if player.get_activo():
        screen.blit(player.image, player.rect)
    
    for vidas in extra_lives_list:
        if vidas.get_activo() == True:
            screen.blit(vidas.get_imagen(), vidas.get_rect()) #####

    if booster.get_activo():
        screen.blit(booster.get_imagen(), booster.get_rect())

    for proyectil in extra_projectiles_list:
        if proyectil.get_activo() == True:
            screen.blit(proyectil.get_imagen(), proyectil.get_rect())


    if len(projectiles_list) > 0:
        blitear_disparos(screen, projectiles_list, height, width)

    pygame.display.update()