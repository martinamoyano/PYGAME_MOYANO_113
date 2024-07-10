import pygame
from instancias_juego import *
from settings import *

def main():
    pygame.init()
	
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PO GAME")    
    menu (SCREEN)
    game(SCREEN)

if __name__ == "__main__":
    main() 
        
