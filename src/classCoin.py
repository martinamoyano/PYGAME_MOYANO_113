import pygame

class Coin:
    def __init__(self, dimension: tuple, centro: tuple, imagen: str) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, dimension)
        self.dimension = dimension
        self.rect = self.imagen.get_rect()
        self.rect.center = centro
        self.activo = True
    
    # Getter para imagen
    def get_imagen(self):
        return self.imagen

    # Setter para imagen
    def set_imagen(self, value: str):
        self.imagen = pygame.image.load(value)
        self.imagen = pygame.transform.scale(self.imagen, self.dimension)
        self.rect = self.imagen.get_rect()  # Actualizamos el rectángulo al cambiar la imagen

    # Getter para rect
    def get_rect(self):
        return self.rect

    # Setter para rect
    def set_rect(self, value: pygame.Rect):
        self.rect = value

    # Getter para activo
    def get_activo(self):
        return self.activo

    # Setter para activo
    def set_activo(self, value: bool):
        self.activo = value

    # Getter para la dimensión de la imagen
    def get_dimension(self):
        return self.imagen.get_size()

    # Setter para la dimensión de la imagen
    def set_dimension(self, value: tuple):
        self.imagen = pygame.transform.scale(self.imagen, value)
        self.rect = self.imagen.get_rect()  # Actualizamos el rectángulo al cambiar la dimensión

    # Getter para el centro del rectángulo
    def get_centro(self):
        return self.rect.center

    # Setter para el centro del rectángulo
    def set_centro(self, value: tuple):
        self.rect.center = value

