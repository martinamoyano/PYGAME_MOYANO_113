import pygame, sys
from random import randint
from enemy import Enemy
from player import Panda
from classItem import *
from funciones import *
from pantallas import *
from settings import *
from classBoton import *

def colision_botones_scores (event, boton_return: Boton) -> None: 
    """
    Maneja el evento de movimiento del mouse en la pantalla de puntajes.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        boton_return (Boton): Objeto Boton para el botón de retorno a menú en la pantalla de puntajes.
    """
    if (boton_return.get_rect().collidepoint(event.pos)):
        boton_return.colisionar()
    else:
        boton_return.quitar_colision()
        pygame.mouse.set_system_cursor (pygame.SYSTEM_CURSOR_ARROW)

def click_botones_scores (event, run, boton_return: Boton) -> bool: #renombrar como click_botones_scores o algo asi
    """
    Maneja el evento de clic de mouse en la pantalla de puntajes.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        run (bool): Estado de ejecución del juego.
        boton_return (Boton): Objeto Boton para el botón de retorno a menú en la pantalla de puntajes.

    Returns:
        bool: Nuevo estado de ejecución del juego.
    """
    if (boton_return.get_rect().collidepoint(event.pos)): #inicia juego
        run = False
        boton_return.quitar_colision()
    
    return run
def menu_screen(screen, boton_play: Boton, boton_score: Boton) -> None:
    """
    Muestra la pantalla del menú principal del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        boton_play (Boton): Objeto Boton para el botón de jugar en el menú.
        boton_score (Boton): Objeto Boton para el botón de puntajes en el menú.
    """
    #Fondo
    blitear_imagen(screen, r"src\fondo.png", (WIDTH, HEIGHT),(0, 0))
    
    #Botones
    screen.blit(boton_play.get_imagen_surface(), boton_play.get_rect())
    screen.blit(boton_score.get_imagen_surface(), boton_score.get_rect())

    #Actualizamos pantalla
    pygame.display.update()

def scores_screen(screen, boton_return: Boton) -> None:
    """
    Muestra la pantalla de puntajes del juego.

    Args:
        screen (pygame.Surface): La superficie de la pantalla de Pygame.
        boton_return (Boton): Objeto Boton para el botón de retorno a menú en la pantalla de puntajes.
    """
    #Fondo
    blitear_imagen(screen, r"src\fondo.png", (WIDTH, HEIGHT),(0, 0))

    #Botones
    screen.blit(boton_return.get_imagen_surface(), boton_return.get_rect())
    

    #Lista de puntajes
    # blitear_scores(screen, r"json/jugadores.json")

    #Actualizamos pantalla
    pygame.display.update()

def colisionar_boton (boton: Boton, boton_a: Boton) -> None:
    if boton_a.get_colision() == True:
        boton_a.quitar_colision()

    boton.colisionar()

def colisiones_botones_menu (event, boton_play: Boton, boton_score: Boton) -> None:
    """
    Maneja el evento de movimiento del mouse en el menú principal del juego.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        boton_play (Boton): Objeto Boton para el botón de jugar en el menú.
        boton_score (Boton): Objeto Boton para el botón de puntajes en el menú.
    """
    if (boton_play.get_rect().collidepoint(event.pos)):
        colisionar_boton (boton_play, boton_score)
    elif (boton_score.get_rect().collidepoint(event.pos)):
        colisionar_boton (boton_score, boton_play)
    else:
        boton_play.quitar_colision()
        boton_score.quitar_colision()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

def click_botones_menu (event, run: bool, scores: bool, boton_play: Boton, boton_play_score: Boton) -> bool:
    """
    Maneja el evento de clic de mouse en el menú principal del juego.

    Args:
        event (pygame.event.Event): Objeto de evento de Pygame.
        run (bool): Estado de ejecución del juego.
        scores (bool): Estado de la pantalla de puntajes.
        boton_play (Boton): Objeto Boton para el botón de jugar en el menú.
        boton_play_score (Boton): Objeto Boton para el botón de puntajes en el menú.

    Returns:
        tuple: Nuevo estado de ejecución del juego y estado de la pantalla de puntajes.
    """
    if (boton_play.get_rect().collidepoint(event.pos)):
        run = False

    elif (boton_play_score.get_rect().collidepoint(event.pos)):
        scores = True
    
    return run, scores
def menu (screen):
    boton_play =  Boton ((400,300), (80,80), r"src\bfecbaa063a84b2e9bbd9f8b9b41d410-boton-de-reproduccion-redondo-azul.webp", r"src\check-markimage-search-results-picture-icon-boton-check-115533860879whjy7sk3g.png")
    boton_score =  Boton ((400,400), (50,50), r"src\check-markimage-search-results-picture-icon-boton-check-115533860879whjy7sk3g.png", r"src\bfecbaa063a84b2e9bbd9f8b9b41d410-boton-de-reproduccion-redondo-azul.webp")
    
    run = True
    scores = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                colisiones_botones_menu (event, boton_play, boton_score)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                run, scores = click_botones_menu (event, run, scores, boton_play, boton_score)

        if scores == True:
            run_scores (screen)
            scores = False

        menu_screen (screen, boton_play, boton_score)
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

def run_scores (screen):
    """
    Ejecuta el bucle para mostrar los puntajes de los 10 mejores jugadores.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se muestran los puntajes.
    """
    boton_return = Boton ((50,50), (75,60), r"src\back-158491_640.webp", r"src\check-markimage-search-results-picture-icon-boton-check-115533860879whjy7sk3g.png")
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                colision_botones_scores (event, boton_return)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                run = click_botones_scores (event, run, boton_return)

        scores_screen (screen, boton_return)
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
def game (screen):
    clock = pygame.time.Clock()
    player = Panda(SCREEN_CENTER, 3,0, 5, 10, r"src\panda.png") 
    initial_speed = player.speed

    enemies_list = []
    enemy = Enemy(((WIDTH // 2), 25))
    enemies_list.append(enemy)

    booster = Booster((40, 30), (randint(25,WIDTH-25),randint(68,HEIGHT-25)), r'src\energy_booster.png')
    booster.set_activo(False)

    player.image = player.sheet.subsurface(player.sheet.get_clip())

    coin_list = cargar_coins (10, WIDTH, HEIGHT)
    projectiles_list = []
    extra_lives_list = []
    extra_projectiles_list = []

    next_projectile_spawn_time = pygame.time.get_ticks() + randint(10000, 30000)
    next_life_spawn_time = pygame.time.get_ticks() + randint(10000, 30000)  
    next_booster_spawn_time = pygame.time.get_ticks() + 4000
    booster_end_time = 0

    is_running = True

    next_enemie_spawn_time = pygame.time.get_ticks() + 5000
    inmune = False
    while is_running:

        if player.get_activo() == False and inmune == False:
            pygame.time.set_timer(pygame.USEREVENT, 400)
            inmune = True
            
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                inmune = False
                player.set_activo(True)
            player.handle_event(event, projectiles_list)

        coin_colision(coin_list, player)

        for enemy in enemies_list:
            if enemy.activo == True:
                colision_enemy(enemy, player)
                projectil_colision_enemy(projectiles_list, enemy, player)
            else:
                enemies_list.remove(enemy)

        projectil_extra_colision(extra_projectiles_list, player)

        next_booster_spawn_time, booster_end_time = booster_colision(booster, player, current_time, next_booster_spawn_time, booster_end_time)

        if booster_end_time <= current_time and initial_speed < player.speed:
            player.speed -= 10

            booster_end_time = current_time + 5000
            booster.set_centro((randint(25,WIDTH-25),randint(25,HEIGHT-25)))
        
        live_colision(extra_lives_list, player)

        if player.lives == 0:
            gameover_screen(screen, player)
            is_running = False  
                
        player.update()
        for enemy in enemies_list:
            enemy.enemy_sprites.update()
            enemy.movimiento(HEIGHT, WIDTH)
        
        limites(player, WIDTH, HEIGHT)

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
            proyectil = Projectile((15, 15), (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)), r"src\panda_projectile.png", 0)
            extra_projectiles_list.append(proyectil)
            next_projectile_spawn_time = current_time + randint(10000, 30000)

        if current_time >= next_enemie_spawn_time:
            enemy = Enemy((randint(10, WIDTH - 10), -10))
            enemies_list.append(enemy)
            
            next_enemie_spawn_time = pygame.time.get_ticks() + 5000

        if booster.get_activo() == False and current_time >= next_booster_spawn_time:
            booster.set_activo(True)

        game_screen(screen, player, fondo, enemies_list, coin_list, projectiles_list, extra_projectiles_list, extra_lives_list, WIDTH, HEIGHT, booster)
        clock.tick(30)
        
    pygame.quit ()
