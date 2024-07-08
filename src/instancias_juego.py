import pygame
from enemie import Enemie
from player import Panda
from classItem import *
from funciones import *
from colisiones import *
from settings import *

def game (screen):
    clock = pygame.time.Clock()

    player = Panda(SCREEN_CENTER, 3, 0, 10, r"src\panda.png") 

    enemie = Enemie(((WIDTH // 2), 25))
    enemie_sprites = pygame.sprite.Group()
    enemie_sprites.add(enemie)

    enemie_2 = Enemie(((WIDTH // 2), 25))
    enemie2_sprites = pygame.sprite.Group()
    enemie2_sprites.add(enemie_2)

    fondo = pygame.image.load(r'src\fondo.png')
    player.image = player.sheet.subsurface(player.sheet.get_clip())

    colisionando = False
    colisionando2 = False

    coin_list = cargar_coins (10, WIDTH, HEIGHT)
    projectiles_list = [] 

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            player.handle_event(event, projectiles_list)
            
        for i in range (len(coin_list)):
            if detectar_colision_circulo (coin_list[i].get_rect(), player.rect) == True:
                coin_list[i].set_activo (False)

        for i in range (len(projectiles_list)):
            if detectar_colision_circulo (projectiles_list[i].get_rect(), enemie.rect):
                projectiles_list[i].set_activo (False)
                enemie.activo = False
        
        if enemie.activo == True:
            colisionando = colision_enemie(enemie, colisionando, player)
        # colisionando2 = colision_enemie(enemie_2, colisionando2, player)

        if player.lives == 0:
            screen.fill((255, 255, 255))
            blitear_textos(screen, fuente(70), 'Game Over', (250, 250))
            
            pygame.display.flip()
            pygame.time.delay(2000) 
            
            is_running = False  
                
        player.update()
        enemie_sprites.update()

        screen.blit(fondo, (0,0))
        blitear_textos(screen, fuente(30), f'balas: {player.projectiles}', (250, 30))

        for coin in coin_list:
            if coin.get_activo() == True:
                screen.blit(coin.get_imagen(), coin.get_rect()) ##

        lives_x = 25
        for i in range(player.lives):
            blitear_imagen(screen, r'src\live_heart.png', (35,35), (lives_x,25))
            lives_x += 30
        
        screen.blit(player.image, player.rect)

        if enemie.activo == True:
            enemie_sprites.draw(screen)
            # enemie2_sprites.draw(screen)
        
        if player.rect.right > WIDTH:
            player.rect.right = WIDTH
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.bottom > HEIGHT - 10: #pongo '10' por el limite con el borde de bambus
            player.rect.bottom = HEIGHT - 10
        if player.rect.top < 0:
            player.rect.top = 0

        enemie.movimiento(HEIGHT, WIDTH)
        # enemie_2.movimiento(HEIGHT,WIDTH)

        hay_monedas = False
        for coin in coin_list:
            if coin.get_activo() == True:
                hay_monedas = True
                break
        
        if hay_monedas == False:
            coin_list = cargar_coins (20, WIDTH, HEIGHT)

        if len(projectiles_list) > 0:
            for balas in projectiles_list:
                balas.movimiento(HEIGHT, WIDTH)
                screen.blit(balas.get_imagen(), balas.get_rect())
        
        pygame.display.flip()
        clock.tick(20)
    pygame.quit ()

