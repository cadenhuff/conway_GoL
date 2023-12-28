import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
cell_size = 20
rows, cols = height // cell_size, width // cell_size
border_size = 1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the initial grid with random values
grid = np.random.choice([0], size=(rows, cols))

# Create Pygame screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

def update_grid():
    for row in range(rows):
        for col in range(cols):
            # Count live neighbors
            neighbors = np.sum(grid[max(0, row-1):min(rows, row+2), max(0, col-1):min(cols, col+2)]) - grid[row, col]

            # Apply Conway's rules
            if grid[row, col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[row, col] = 0
            else:
                if neighbors == 3:
                    new_grid[row, col] = 1






# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Copy the grid to make updates simultaneously
    new_grid = grid.copy()

    # Update the grid based on Conway's rules
    update_grid()

    # Update the grid
    grid = new_grid

    # Draw the grid
    screen.fill(BLACK)
    for row in range(rows):
        for col in range(cols):
            x = col * cell_size
            y = row * cell_size

            # Draw cell
            pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size))

            # Draw border
            pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size), border_size)

    # Update the display
    pygame.display.flip()

    # Adjust the frame rate
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
