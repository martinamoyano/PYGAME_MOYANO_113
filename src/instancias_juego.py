import pygame
from random import randint
from enemy import Enemy
from player import Panda
from classItem import *
from funciones import *
from colisiones import *
from settings import *

def game (screen):
    clock = pygame.time.Clock()

    panda_projectiles = 10
    player = Panda(SCREEN_CENTER, 3, panda_projectiles, r"src\panda.png") 

    enemy = Enemy(((WIDTH // 2), 25))
    enemy_sprites = pygame.sprite.Group()
    enemy_sprites.add(enemy)

    enemy_2 = Enemy(((WIDTH // 2), 25))
    enemy2_sprites = pygame.sprite.Group()
    enemy2_sprites.add(enemy_2)

    fondo = pygame.image.load(r'src\fondo.png')
    player.image = player.sheet.subsurface(player.sheet.get_clip())

    colisionando = False
    colisionando2 = False

    coin_list = cargar_coins (10, WIDTH, HEIGHT)
    projectiles_list = []
    extra_lives_list = []
    extra_projectiles_list = []

    next_projectile_spawn_time = pygame.time.get_ticks() + randint(10000, 30000)
    next_life_spawn_time = pygame.time.get_ticks() + randint(10000, 30000)  

    is_running = True
    while is_running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                
            player.handle_event(event, projectiles_list)

        colisionando = colisiones (player, enemy, colisionando, panda_projectiles, projectiles_list, extra_projectiles_list, coin_list, extra_lives_list)

        if player.lives == 0:
            gameover_screen(screen)
            is_running = False  
                
        player.update()
        enemy_sprites.update()
        
        limites(player, WIDTH, HEIGHT)

        enemy.movimiento(HEIGHT, WIDTH)
        # enemy_2.movimiento(HEIGHT,WIDTH)

        hay_monedas = False
        for coin in coin_list:
            if coin.get_activo() == True:
                hay_monedas = True
                break
        
        if hay_monedas == False: #### MODIFICAR
            coin_list = cargar_coins (20, WIDTH, HEIGHT)

        if player.lives < 3 and current_time >= next_life_spawn_time: #### MODULO
            vida = Live((30, 30), (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)), r"src\live_heart.png")
            extra_lives_list.append(vida)
            next_life_spawn_time = current_time + randint(10000, 30000)  
        
        if player.projectiles == 0 and current_time >= next_projectile_spawn_time:
            proyectil = Projectile((15, 15), (randint(15, WIDTH - 15), randint(15, HEIGHT - 15)), r"src\panda_projectile.png", 1)
            extra_projectiles_list.append(proyectil)
            next_projectile_spawn_time = current_time + randint(10000, 30000)

        game_screen(screen, player, fondo, enemy, coin_list, enemy_sprites, projectiles_list, extra_projectiles_list, extra_lives_list, WIDTH, HEIGHT)
        clock.tick(30)
        
    pygame.quit ()
