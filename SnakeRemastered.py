# 'Snake Remastered'
# By: Isaac Castaneda
# Taking the classic game "Snake" and throwing in new
# features for experimental purposes.
import pygame
import random
import sys

# GAME CONSTANTS
WINWIDTH = 720
WINHEIGHT = 480
BOXSIZE = 10
FONTSIZE = 18
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)

# Ensures there are no errors while initializing game
precond = pygame.init()
if precond[1] > 0:
    print('Error while initializing game.')
    sys.exit(-1)
else:
    print('Game initialized.')

# Builds the display window + other necessary tools
window = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Snake Remastered')
font = pygame.font.SysFont('timesnewroman', FONTSIZE)
fps = pygame.time.Clock()


# Termination call to close window
# TODO: Add delay or timer when ending ?
def game_end():
    print('Thank you for playing!')
    pygame.quit()
    sys.exit()

# Pushes score to display
def display_score(score):
    curr_score = font.render('Score: ' + str(score), True, WHITE)
    window.blit(curr_score, [0, 0])


# Handles the game's mechanics and graphics
# TODO: Split into smaller functions
def game_logic():
    list = pygame.font.get_fonts()
    print(list)
    # The variables for the snake head, current pos and moving pos
    x_axis = WINWIDTH / 2
    x_move = 0
    y_axis = WINHEIGHT / 2
    y_move = 0

    # Holds the snake's body (including head)
    body = []
    # TODO: Broadcast this variable to display
    score = 0

    # Stands for point x/y_axis, spawns initial point
    px_axis = random.randrange(1, (WINWIDTH / BOXSIZE)) * BOXSIZE
    py_axis = random.randrange(1, (WINHEIGHT / BOXSIZE)) * BOXSIZE

    # Main loop for game, controls hitboxes, graphics, and keypresses
    while True:
        # Hit the exit button and force ends game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end()

        # Checks currently pressed keys to move in requested direction
        # W = UP, A = LEFT, S = DOWN, D = RIGHT
        # TODO: Insert 2nd set (arrow keys) for potential 2-player mode
        keys = pygame.key.get_pressed()
        # Northwest (Up + Left)
        if keys[pygame.K_a] and keys[pygame.K_w]:
            x_move = -BOXSIZE
            y_move = -BOXSIZE
        # Southwest (Down + Left)
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            x_move = -BOXSIZE
            y_move = BOXSIZE
        # Northeast (Up + Right)
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            x_move = BOXSIZE
            y_move = -BOXSIZE
        # Southeast (Down + Right)
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            x_move = BOXSIZE
            y_move = BOXSIZE
        # West (Left)
        elif keys[pygame.K_a]:
            x_move = -BOXSIZE
            y_move = 0
        # East (Right)
        elif keys[pygame.K_d]:
            x_move = BOXSIZE
            y_move = 0
        # North (Up)
        elif keys[pygame.K_w]:
            x_move = 0
            y_move = -BOXSIZE
        # South (Down)
        elif keys[pygame.K_s]:
            x_move = 0
            y_move = BOXSIZE

        # Hitbox checks, go out-of-bounds and the game ends
        if x_axis < 0 or x_axis >= WINWIDTH:
            game_end()
        if y_axis < 0 or y_axis >= WINHEIGHT:
            game_end()

        # Sets new head coordinates
        x_axis += x_move
        y_axis += y_move

        # Updates head coordinates and inserts into body
        head = [x_axis, y_axis]
        body.append(head)

        # Removes end of snake to prevent infinite length (mimics movement)
        if len(body) > (score + 1):
            del body[0]

        # Hitbox check, ensures head does not hit the body or ends game
        for part in body[:-1]:
            if part == head:
                game_end()

        # Resets the canvas to replicate movement of the pieces
        window.fill(BLACK)
        # Draws the point at its current location
        pygame.draw.rect(window, RED, [px_axis, py_axis, BOXSIZE, BOXSIZE])
        # Draws the snake's body
        for part in body:
            pygame.draw.rect(window, GRAY, [part[0], part[1], BOXSIZE, BOXSIZE])

        # Score display
        display_score(score)

        # Refreshes the display with new changes
        pygame.display.update()

        # Point updater + storage, finds new location for next point
        if x_axis == px_axis and y_axis == py_axis:
            px_axis = random.randrange(1, (WINWIDTH // BOXSIZE)) * BOXSIZE
            py_axis = random.randrange(1, (WINHEIGHT // BOXSIZE)) * BOXSIZE
            score += 1
            print('Score: ' + str(score))

        # Handles game speed
        # TODO: Increment FPS based on points/settings to mimic difficulty increase ?
        fps.tick(10)


# TODO: Better way to start the game
game_logic()