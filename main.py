import pygame
pygame.init()

# game window
pygame.display.set_caption("MacGyver Escape")
screen = pygame.display.set_mode((600, 600))

background = pygame.image.load('assets/background.png')

running = True

# loop running
while running:

    # background
    screen.blit(background, (0, 0))

    # update screen
    pygame.display.flip()

    for event in pygame.event.get():
        # close window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game off")
