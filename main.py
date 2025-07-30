from settings import *
from sprites import Player, Background

# setup
pygame.init()
pygame.display.set_caption("Pygame Star Shooter")

clock = pygame.time.Clock()
running = True

# instantiate sprites
background = Background()
player = Player()

# define group, place sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(background, player)

while running:

    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)
    all_sprites.draw(display)
    pygame.display.update()

pygame.quit()

