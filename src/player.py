import pygame

class Panda(pygame.sprite.Sprite):
    def __init__(self, position):
        self.lives = 3
        self.sheet = pygame.image.load(r'src\panda.png')
        self.sheet = pygame.transform.scale(self.sheet, (141,192))
        self.sheet.set_clip(pygame.Rect(48, 0, 48, 48))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position 
        self.frame = 0

        self.down_states = { 0: (0, 0, 48, 48), 1: (48, 0, 48, 48), 2: (96, 0, 48, 48) }
        self.left_states = { 0: (0, 48, 48, 48), 1: (48, 48, 48, 48), 2: (96, 48, 48, 48)}
        self.right_states = { 0: (0, 96, 48, 48), 1: (48, 96, 48, 48), 2: (96, 96, 48, 48) }
        self.up_states = { 0: (0, 144, 48, 48), 1: (48, 144, 48, 48), 2: (96, 144, 48, 48) }

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def update(self):
        if self.moving_left:
            self.clip(self.left_states)
            self.rect.x -= 5
        if self.moving_right:
            self.clip(self.right_states)
            self.rect.x += 5
        if self.moving_up:
            self.clip(self.up_states)
            self.rect.y -= 5
        if self.moving_down:
            self.clip(self.down_states)
            self.rect.y += 5
    
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def clip(self, clipped_rect):
        if isinstance(clipped_rect, dict):
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.moving_left = True
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            if event.key == pygame.K_UP:
                self.moving_up = True
            if event.key == pygame.K_DOWN:
                self.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.moving_left = False
                self.clip(self.left_states[1])
            if event.key == pygame.K_RIGHT:
                self.moving_right = False
                self.clip(self.right_states[1])
            if event.key == pygame.K_UP:
                self.moving_up = False
                self.clip(self.up_states[1])
            if event.key == pygame.K_DOWN:
                self.moving_down = False
                self.clip(self.down_states[1])
    
        self.image = self.sheet.subsurface(self.sheet.get_clip())