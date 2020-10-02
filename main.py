#!/usr/bin/env python
# encoding: utf-8

import pygame
from objects.game import Game
pygame.init()

# game window
pygame.display.set_caption("MacGyver Escape")
screen = pygame.display.set_mode((600, 600))

# load the game
game = Game()

running = True

# loop running
while running:

    # background and wall
    screen.blit(game.maze.background, (0, 0))
    game.maze.draw_wall(screen, game.maze.wall)
    screen.blit(game.player.image, game.player.rect)

    # movement
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 560:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < 560:
        game.player.move_down()

    # update screen
    pygame.display.flip()

    for event in pygame.event.get():

        # close window
        if event.type == pygame.K_ESCAPE:
            running = False
            pygame.quit()
            print("game closed")

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game closed")

        # player movement
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
