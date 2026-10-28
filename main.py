import os
import pygame

player_one = True
player_two = False

pygame.init()

# Setting Width and height of the Chess Game screen
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

clock = pygame.time.Clock()
FPS = 60

# Chess board settings
BOARD_SIZE = 8
TILE_SIZE = 80
BOARD_X = (WIDTH - BOARD_SIZE * TILE_SIZE) // 2
BOARD_Y = (HEIGHT - BOARD_SIZE * TILE_SIZE) // 2

LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)

def load_piece_image(name):
    path = os.path.join("assets", f"{name}.png")
    if os.path.exists(path):
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(image, (TILE_SIZE, TILE_SIZE))

    # Fallback graphic if image is missing
    surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
    color = (255, 255, 255) if "white" in name else (20, 20, 20)
    pygame.draw.circle(surface, color, (TILE_SIZE // 2, TILE_SIZE // 2), TILE_SIZE // 3)
    return surface

piece_images = {
    "white_pawn": load_piece_image("white_pawn"),
    "white_rook": load_piece_image("white_rook"),
    "white_knight": load_piece_image("white_knight"),
    "white_bishop": load_piece_image("white_bishop"),
    "white_queen": load_piece_image("white_queen"),
    "white_king": load_piece_image("white_king"),
    "black_pawn": load_piece_image("black_pawn"),
    "black_rook": load_piece_image("black_rook"),
    "black_knight": load_piece_image("black_knight"),
    "black_bishop": load_piece_image("black_bishop"),
    "black_queen": load_piece_image("black_queen"),
    "black_king": load_piece_image("black_king"),
}

board = [
    ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook"],
    ["black_pawn"] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ["white_pawn"] * 8,
    ["white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook"],
]

# draw main game board
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = BOARD_X + col * TILE_SIZE
            y = BOARD_Y + row * TILE_SIZE
            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(screen, (0, 0, 0), (BOARD_X, BOARD_Y, BOARD_SIZE * TILE_SIZE, BOARD_SIZE * TILE_SIZE), 3)

# draw pieces onto board
def draw_pieces():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if piece is None:
                continue

            image = piece_images[piece]
            x = BOARD_X + col * TILE_SIZE
            y = BOARD_Y + row * TILE_SIZE
            screen.blit(image, (x, y))

# Check valid moves for a piece
def is_valid_move(piece, start_pos, end_pos):
    # Placeholder for move validation logic
    return True

def move_piece(start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]

    if piece is None:
        return False

    if not is_valid_move(piece, start_pos, end_pos):
        return False

    board[end_row][end_col] = piece
    board[start_row][start_col] = None
    return True

running = True

# main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))
    draw_board()
    draw_pieces()

    if (player_one):
        

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()