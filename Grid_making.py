import pygame
import random

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def create_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = 1 if random.random() < 0.6 else 0
        self.data[0][0] = 1
        self.data[self.rows - 1][self.cols - 1] = 1
        x, y = 0, 0
        self.data[x][y] = 1
        while x < self.rows - 1 or y < self.cols - 1:
            if x < self.rows - 1 and (y == self.cols - 1 or random.choice([True, False])):
                x += 1
            else:
                y += 1
            self.data[x][y] = 1

    def reset_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != 1:
                    self.data[i][j] = 0

    @staticmethod
    def draw_grid(screen, grid,CELL_SIZE):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    color = (255, 255, 255)
                elif grid[i][j] == 2:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, (200, 200, 200), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)