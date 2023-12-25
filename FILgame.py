import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fire Flight")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

rect_width, rect_height = 50, 30
rect_x, rect_y = width // 2 - rect_width // 2, height // 2 - rect_height // 2

speed = 5

# Set up game loop
clock = pygame.time.Clock()
fps = 60

# Main game loop
running = True
while running:

    pygame.display.flip()
    clock.tick(fps)

    # closes window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # allows object to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # Drawing
    screen.fill(white)
    pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height))


# Quit Pygame
pygame.quit()
sys.exit()
