import pygame
from enemie import Enemie
from player import Panda
from funciones import *
from colisiones import *
from settings import *

def game (screen):
    clock = pygame.time.Clock()

    player = Panda(SCREEN_CENTER) 

    enemie = Enemie(((WIDTH // 2), 25))
    enemie_sprites = pygame.sprite.Group()
    enemie_sprites.add(enemie)

    fondo = pygame.image.load(r'src\fondo.png')
    player.image = player.sheet.subsurface(player.sheet.get_clip())

    is_running = True
    coin_list = recargar_lista (10, WIDTH, HEIGHT)
    colisionando = False

    while is_running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                is_running = False
        
            player.handle_event(event)
            
        for i in range (len(coin_list)):
            if detectar_colision_circulo (coin_list[i].get_rect(), player.rect) == True:
                coin_list[i].set_activo (False)
        
        colisionando = colision_enemie(enemie, colisionando, player)
        if player.lives == 0:
            screen.fill((255, 255, 255))
            font = pygame.font.Font(None, 74)
            game_over_text = font.render('Game Over', True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=SCREEN_CENTER)
            screen.blit(game_over_text, text_rect)
            
            pygame.display.flip()
            pygame.time.delay(2000) 
            
            is_running = False  
                
        player.update()
        enemie_sprites.update()

        screen.blit(fondo, (0,0))
        for coin in coin_list:
            if coin.get_activo() == True:
                screen.blit(coin.get_imagen(), coin.get_rect())

        
        screen.blit(player.image, player.rect)
        enemie_sprites.draw(screen)
        
        if player.rect.right > WIDTH:
            player.rect.right = WIDTH
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.bottom > HEIGHT - 10: #pongo '10' por el limite con el borde de bambus
            player.rect.bottom = HEIGHT - 10
        if player.rect.top < 0:
            player.rect.top = 0

        enemie.movimiento(HEIGHT, WIDTH)

        pygame.display.flip()
        clock.tick(20)

        hay_monedas = False
        for coin in coin_list:
            if coin.get_activo() == True:
                hay_monedas = True
                break
        
        if hay_monedas == False:
            coin_list = recargar_lista (20, WIDTH, HEIGHT)

    pygame.quit ()

