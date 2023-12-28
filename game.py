import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
width, height = 1200, 700
#800,600
cell_size = 25
rows, cols = height // cell_size, width // cell_size
border_size = 1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the initial grid with random values
grid = np.zeros((rows, cols), dtype=int)

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


# Function to update the grid based on user input
def toggle_grid(mouse_pos):
    print(mouse_pos)
    col = mouse_pos[0] // cell_size
    row = mouse_pos[1] // cell_size

    # Toggle the state of the clicked cell
    grid[row, col] = 1 - grid[row, col]

def draw_grid():
    screen.fill(WHITE)
    for row in range(rows):
        for col in range(cols):
            x = col * cell_size
            y = row * cell_size

            # Draw cell
            if grid[row,col] == 1:
                pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size))
            

            # Draw border
            pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size), border_size)

    # Update the display
    pygame.display.flip()

    # Adjust the frame rate
    pygame.time.delay(100)


# Game loop
running = True
game_running = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                toggle_grid(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_running = True



    # Copy the grid to make updates simultaneously
    new_grid = grid.copy()
    while game_running:
        new_grid = grid.copy()
        #Update the grid based on Conway's rules
        update_grid()
        if (np.array_equal(grid,new_grid)):
            game_running = False
        grid = new_grid
        draw_grid()
    # Update the grid
    
    grid = new_grid
    

    # Draw the grid
    draw_grid()

# Quit Pygame
pygame.quit()
