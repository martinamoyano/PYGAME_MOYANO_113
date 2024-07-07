from funciones import *

def colision_enemie(enemie, colisionando, player):
    if detectar_colision_circulo(enemie.rect, player.rect):
        if colisionando == False: 
            player.lives -= 1
            colisionando = True  
            print(player.lives)
    else:
        colisionando = False  
    
    return colisionando