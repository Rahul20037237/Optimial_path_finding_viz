import pygame
from Grid_making import Grid

class DFS:
    def __init__(self, grid, screen):
        self.grid = grid
        self.screen = screen
        self.visited = set()

    def neighbors(self, row, col):
        # Define neighbors in 4 directions (up, down, left, right)
        indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        return [
            (r, c)
            for r, c in indices
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == 1
        ]

    def DFS_img(self, row, col,CELL_SIZE):
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            if (r, c) in self.visited:
                continue
            self.visited.add((r, c))
            self.grid[r][c] = 2  # Mark cell as visited (part of path)
            Grid.draw_grid(self.screen, self.grid,CELL_SIZE)  # Draw updated grid
            pygame.display.flip()  # Update the screen
            pygame.time.delay(50)  # Delay to visualize animation

            for nr, nc in self.neighbors(r, c):  # Add neighboring cells to stack
                if (nr, nc) not in self.visited:
                    stack.append((nr, nc))