import pygame

from settings import *
from sprites import Player, Background, Obstakle

# setup
pygame.init()
pygame.display.set_caption("Pygame Star Shooter")

clock = pygame.time.Clock()
running = True


# define group to place sprites to update
all_sprites = pygame.sprite.Group()

# instantiate sprites
background = Background(all_sprites)
player = Player(all_sprites)


# user event to spawn obstakles
obstakle_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstakle_spawn_timer, 1500)


while running:
    # delta
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT + 1:
            obstakle = Obstakle(all_sprites)

    all_sprites.update(dt)
    all_sprites.draw(display)
    pygame.display.update()

pygame.quit()

