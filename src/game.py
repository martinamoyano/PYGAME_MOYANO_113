# from classCoin import Coin
# import pygame, player, random
# from enemie import Enemie

# def recargar_lista (cantidad: int) -> list:
#     coin_list = []
#     for i in range (cantidad):
#         coin = Coin ((20,20), (random.randint(25,WIDTH-25),random.randint(25,HEIGHT-25)), r"src\coin.png")
#         coin_list.append(coin)
#     return coin_list

# def distancia_entre_puntos(pto_1:tuple[int, int], pto_2:tuple[int, int]) -> float :
#     base = pto_1[0] - pto_2[0]
#     altura = pto_1[1] - pto_2[1]
#     return (base ** 2 + altura ** 2) ** 0.5

# def calcular_radio(rect):
#     return rect.width // 2

# def detectar_colision_circulo(rect_1, rect_2) -> bool :
#     r1 = calcular_radio(rect_1)
#     r2 = calcular_radio(rect_2)
#     base = rect_1.centerx - rect_2.centerx
#     altura = rect_1.centery - rect_2.centery
#     distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
#     return distancia <= r1 + r2

# def colision_enemie(enemie, colisionando, player):
#     if detectar_colision_circulo(enemie.rect, player.rect):
#         if colisionando == False: 
#             player.lives -= 1
#             colisionando = True  
#             print(player.lives)
#     else:
#         colisionando = False  
    
#     return colisionando

        
# pygame.init()

# WIDTH = 800
# HEIGHT = 600
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# SCREEN_CENTER = (WIDTH//2, HEIGHT//2)

# pygame.display.set_caption("PO GAME")
# clock = pygame.time.Clock()
# player = player.Panda(SCREEN_CENTER) 

# enemie = Enemie((WIDTH//2, 25))
# enemie_sprites = pygame.sprite.Group()
# enemie_sprites.add(enemie)

# fondo = pygame.image.load(r'src\fondo.png')
# player.image = player.sheet.subsurface(player.sheet.get_clip())


# is_running = True
# coin_list = recargar_lista (10)
# colisionando = False

# while is_running:
#     for event in pygame.event.get():
#         # print(event)
#         if event.type == pygame.QUIT:
#             is_running = False
    
#         player.handle_event(event)
        
#     for i in range (len(coin_list)):
#         if detectar_colision_circulo (coin_list[i].get_rect(), player.rect) == True:
#             coin_list[i].set_activo (False)
    
#     colisionando = colision_enemie(enemie, colisionando, player)
#     if player.lives == 0:
#         SCREEN.fill((255, 255, 255))
#         font = pygame.font.Font(None, 74)
#         game_over_text = font.render('Game Over', True, (255, 0, 0))
#         text_rect = game_over_text.get_rect(center=SCREEN_CENTER)
#         SCREEN.blit(game_over_text, text_rect)
        
#         pygame.display.flip()
#         pygame.time.delay(2000) 
        
#         is_running = False  
            
#     player.update()
#     enemie_sprites.update()

#     SCREEN.blit(fondo, (0,0))
#     for coin in coin_list:
#         if coin.get_activo() == True:
#             SCREEN.blit(coin.get_imagen(), coin.get_rect())

    
#     SCREEN.blit(player.image, player.rect)
#     enemie_sprites.draw(SCREEN)
    
#     if player.rect.right > WIDTH:
#         player.rect.right = WIDTH
#     if player.rect.left < 0:
#         player.rect.left = 0
#     if player.rect.bottom > HEIGHT - 10: #pongo '10' por el limite con el borde de bambus
#         player.rect.bottom = HEIGHT - 10
#     if player.rect.top < 0:
#         player.rect.top = 0

#     enemie.movimiento(HEIGHT, WIDTH)

#     pygame.display.flip()
#     clock.tick(20)

#     hay_monedas = False
#     for coin in coin_list:
#         if coin.get_activo() == True:
#             hay_monedas = True
#             break
    
#     if hay_monedas == False:
#         coin_list = recargar_lista (20)

    
# pygame.quit ()


