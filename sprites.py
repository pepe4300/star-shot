import pygame

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.starting_image = pygame.image.load(join('assets','player.png'))
        self.image = pygame.transform.scale(self.starting_image,(50,50))
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.display_rect = display.get_rect()
        self.group = groups

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500

        # dash cooldown
        self.dash_cooldown = 500
        self.can_dash = True
        self.current_time = pygame.time.get_ticks()
        self.dash_time = pygame.time.get_ticks()

        # dash animation frames
        self.dash_frames = []
        self.dash_folder = join('assets', 'dash_animation')
        for filename in sorted(os.listdir(self.dash_folder)):
            if filename.endswith(".png"):
                dash_img = pygame.image.load(join(self.dash_folder, filename)).convert_alpha()
                self.dash_frames.append(dash_img)

    def movement(self, dt):
        # gathers kbd input
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction

        # moves player around
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def dash(self):
        shift = pygame.key.get_just_pressed()
        # dash logic, checks the player direction and calculates dash accordingly
        if self.can_dash:
            if shift[pygame.K_LSHIFT]:
                    Dash_Animation(self.group, self.rect.midtop, self.dash_frames, self.rect.center)
                    self.dash_time = pygame.time.get_ticks()
                    if self.direction.x != 0:
                        if self.direction.x < 0:
                            self.rect.x = self.rect.x - 150
                        else:
                            self.rect.x = self.rect.x + 150
                    if self.direction.y:
                        if self.direction.y < 0:
                            self.rect.y = self.rect.y - 150
                        else:
                            self.rect.y = self.rect.y + 150

        # check if player can dash or is in cooldown
        if (self.current_time - self.dash_time) >= self.dash_cooldown:
            self.can_dash = True
        else:
            self.can_dash = False
            self.current_time = pygame.time.get_ticks()

    def collisions(self):
        # window border collision - keeps player always within window
        if not self.display_rect.contains(self.rect): self.rect.clamp_ip(self.display_rect)
        # obstacle collisions - wip

    def update(self, dt):
        self.movement(dt)
        self.dash()
        self.collisions()

class Background(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('assets','background-image.png'))
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

class Obstakle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.rotation = randint(-25,25)
        self.starting_image = pygame.image.load(join('assets', 'obstakle-glow.png'))
        self.image = pygame.transform.rotozoom(self.starting_image, self.rotation, 1.0)
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, 1400))

        # movement attributes
        self.direction = pygame.Vector2(0,-1)
        self.speed = 250

    def update(self, dt):
        self.rect.y += self.direction.y * self.speed * dt
        if self.rect.centery < -200:
            self.kill()

class Dash_Animation(pygame.sprite.Sprite):
    def __init__(self, groups, pos, frames, player):
        super().__init__(groups)
        self.player = player
        self.frames = frames
        self.frame_index = 0
        self.animation_speed = 30
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames):
            self.kill()
            return
        self.image = self.frames[int(self.frame_index)]

        self.rect.center += self.player

















