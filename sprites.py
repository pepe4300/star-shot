from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.starting_image = pygame.image.load(join('assets','player.png'))
        self.image = pygame.transform.scale(self.starting_image,(50,50))
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.display_rect = display.get_rect()

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500

    def movement(self, dt):
        # gathers kbd input
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction

        # moves player around
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def collisions(self):
        # window border collision - keeps player always within window
        if not self.display_rect.contains(self.rect): self.rect.clamp_ip(self.display_rect)
        # obstacle collisions - wip

    def update(self, dt):
        self.movement(dt)
        self.collisions()


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(join('assets','background-image.png'))
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

