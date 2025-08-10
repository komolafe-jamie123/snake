import pygame
import time
import random

# Initialize the game
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# Set the width and height of the display
display_width = 800
display_height = 600

# Set the size of each block in the game
block_size = 20

# Set the speed of the snake
snake_speed = 15

# Set the font size
font_size = 30
font_style = pygame.font.SysFont(None, font_size)

# Create the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Define the snake's movement
def snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

# Display a message on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

# The main game loop
def game_loop():
    game_over = False
    game_close = False

    # Set the starting position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Set the initial movement direction of the snake
    x1_change = 0
    y1_change = 0

    # Create an empty list to store the snake's body
    snake_list = []
    snake_length = 1

    # Set the initial position of the food
    foodx = round(random.randrange(0, display_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, display_height - block_size) / 20.0) * 20.0

    # The game loop
    while not game_over:

        # If the game is over, display a message and wait for the player to press a key
        while game_close:
            game_display.fill(white)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Check for key presses
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Fill the display with white color
        game_display.fill(white)

        # Draw the food
        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])

        # Update the snake's body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for snake collision with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        snake(block_size, snake_list)

        # Update the display
        pygame.display.update()

        # Check for snake collision with food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, display_height - block_size) / 20.0) * 20.0
            snake_length += 1

        # Set the frame rate of the game
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

# Start the game loop
game_loop()
