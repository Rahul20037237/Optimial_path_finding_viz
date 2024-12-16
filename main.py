import pygame
import random
from Grid_making import Grid
from DFS import DFS
from BFS import BFS
from A_star import AStar

random.seed(99)
pygame.init()

WIDTH, HEIGHT = 900, 900
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DFS Animation")
    clock = pygame.time.Clock()

    grid = Grid(ROWS, COLS)
    grid.create_grid()
    start = (0, 0)
    goal = (ROWS - 1, COLS - 1)
    dfs = BFS(grid.data, screen)

    running = True
    dfs_running = False

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid.reset_grid()
                    dfs_running = True

        # Run DFS if the space key is pressed
        if dfs_running:
            dfs.BFS_img(0,0,29,29,CELL_SIZE)  # Start DFS from (0, 0)
            dfs_running = False

        # Draw the grid
        screen.fill(GRAY)
        Grid.draw_grid(screen, grid.data,CELL_SIZE)
        pygame.display.flip()
        clock.tick(60)  # Run at 60 FPS

    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()