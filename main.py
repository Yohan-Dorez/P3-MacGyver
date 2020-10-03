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

    # background, wall and player
    screen.blit(game.maze.background, (0, 0))
    game.wall.draw_wall(screen, game.wall.image)
    screen.blit(game.player.image, game.player.rect)

    # update screen
    pygame.display.flip()

    for event in pygame.event.get():

        # close window by cross
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game closed by cross")

        # player movement

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT and game.player.rect.x < 560:
                game.player.move_right()
            elif event.key == pygame.K_LEFT and game.player.rect.x > 0:
                game.player.move_left()
            elif event.key == pygame.K_UP and game.player.rect.y > 0:
                game.player.move_up()
            elif event.key == pygame.K_DOWN and game.player.rect.y < 560:
                game.player.move_down()

            # close window by escape
            elif event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                print("game closed by escape")
