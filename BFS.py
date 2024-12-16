from collections import deque
import pygame
from Grid_making import Grid

class BFS:
    def __init__(self, grid, screen):
        self.grid = grid  
        self.screen = screen 
        self.visited = set() 

    def BFS_img(self, row, col,g_row,g_col, CELL_SIZE):
        queue = deque([(row, col)])
        self.visited = set() 

        while queue:
            r, c = queue.popleft()
            if (r, c) in self.visited:
                continue
            self.visited.add((r, c))
            self.grid[r][c] = 2 
            Grid.draw_grid(self.screen, self.grid, CELL_SIZE)
            pygame.display.flip() 
            pygame.time.delay(50)
            for nr, nc in self.neighbors(r, c):
                if nr==g_row and nc==g_col:
                    break
                if (nr, nc) not in self.visited:
                    queue.append((nr, nc))

    def neighbors(self, row, col):
        indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        return [
            (r, c)
            for r, c in indices
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == 1
        ]
