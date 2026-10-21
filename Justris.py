import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

GRID_WIDTH = 10
GRID_HEIGHT = 20

# Colors (Retro Palette)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (40, 40, 40)

# Shapes (Tetrominos)
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 1], [1, 1]], # O
    [[0, 1, 0], [1, 1, 1]], # T
    [[1, 0, 0], [1, 1, 1]], # L
    [[0, 0, 1], [1, 1, 1]], # J
    [[0, 1, 1], [1, 1, 0]], # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]

SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[BLACK for _ in range(width)] for _ in range(height)]
        self.score = 0
        self.game_over = False
        self.new_piece()

    def new_piece(self):
        self.shape_idx = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.shape_idx]
        self.color = SHAPE_COLORS[self.shape_idx]
        self.x = self.width // 2 - len(self.shape[0]) // 2
        self.y = 0
        if self.check_collision(self.x, self.y, self.shape):
            self.game_over = True

    def check_collision(self, offset_x, offset_y, shape):
        for r_idx, row in enumerate(shape):
            for c_idx, val in enumerate(row):
                if val:
                    new_x = offset_x + c_idx
                    new_y = offset_y + r_idx
                    if new_x < 0 or new_x >= self.width or new_y >= self.height:
                        return True
                    if new_y >= 0 and self.grid[new_y][new_x] != BLACK:
                        return True
        return False

    def merge_piece(self):
        for r_idx, row in enumerate(self.shape):
            for c_idx, val in enumerate(row):
                if val:
                    self.grid[self.y + r_idx][self.x + c_idx] = self.color
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        lines_to_clear = []
        for r_idx, row in enumerate(self.grid):
            if BLACK not in row:
                lines_to_clear.append(r_idx)
        
        for r in lines_to_clear:
            del self.grid[r]
            self.grid.insert(0, [BLACK for _ in range(self.width)])
        
        if lines_to_clear:
            self.score += len(lines_to_clear) * 100

    def rotate_piece(self):
        rotated = [list(row) for row in zip(*self.shape[::-1])]
        if not self.check_collision(self.x, self.y, rotated):
            self.shape = rotated

    def move(self, dx, dy):
        if not self.check_collision(self.x + dx, self.y + dy, self.shape):
            self.x += dx
            self.y += dy
            return True
        return False

# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Tetris")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier", 20, bold=True)

game = Tetris(GRID_WIDTH, GRID_HEIGHT)
fall_time = 0
fall_speed = 400 # Milliseconds per drop

# Main Loop
running = True
while running:
    dt = clock.tick(60)
    fall_time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game.game_over:
                if event.key == pygame.K_r:
                    game = Tetris(GRID_WIDTH, GRID_HEIGHT)
            else:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate_piece()
                elif event.key == pygame.K_SPACE:
                    while game.move(0, 1):
                        pass

    # Automatic falling
    if not game.game_over and fall_time >= fall_speed:
        if not game.move(0, 1):
            game.merge_piece()
        fall_time = 0

    # Drawing
    screen.fill(BLACK)

    # Draw Grid background lines
    for x in range(GRID_WIDTH):
        pygame.draw.line(screen, GRAY, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(screen, GRAY, (0, y * BLOCK_SIZE), (SCREEN_WIDTH, y * BLOCK_SIZE))

    # Draw placed blocks
    for r_idx, row in enumerate(game.grid):
        for c_idx, color in enumerate(row):
            if color != BLACK:
                pygame.draw.rect(screen, color, (c_idx * BLOCK_SIZE, r_idx * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

    # Draw active piece
    if not game.game_over:
        for r_idx, row in enumerate(game.shape):
            for c_idx, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, game.color, ((game.x + c_idx) * BLOCK_SIZE, (game.y + r_idx) * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

    # Draw Score
    score_surf = font.render(f"SCORE: {game.score}", True, WHITE)
    screen.blit(score_surf, (10, 10))

    # Game Over Message
    if game.game_over:
        over_surf = font.render("GAME OVER", True, RED)
        restart_surf = font.render("PRESS 'R' TO RESET", True, WHITE)
        screen.blit(over_surf, (SCREEN_WIDTH // 2 - over_surf.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(restart_surf, (SCREEN_WIDTH // 2 - restart_surf.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

    pygame.display.flip()

pygame.quit()