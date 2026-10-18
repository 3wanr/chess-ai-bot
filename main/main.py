# Importing Modules
import pygame

# Initialising pygame module
pygame.init()

# Setting Width and height of the Chess Game screen
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

font = pygame.font.Font("freesansbold.ttf", 20)
medium_font = pygame.font.Font("freesansbold.ttf", 40)
big_font = pygame.font.Font("freesansbold.ttf", 50)

clock = pygame.time.Clock()
fps = 60

# Chess board settings
board_size = 8
tile_size = 80
board_x = (WIDTH - board_size * tile_size) // 2
board_y = (HEIGHT - board_size * tile_size) // 2

light_square = (240, 217, 181)
dark_square = (181, 136, 99)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgray")

    # Draw chess board
    for row in range(board_size):
        for col in range(board_size):
            x = board_x + col * tile_size
            y = board_y + row * tile_size
            color = light_square if (row + col) % 2 == 0 else dark_square
            pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))

    # Draw border around board
    pygame.draw.rect(screen, (0, 0, 0), (board_x, board_y, board_size * tile_size, board_size * tile_size), 3)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()