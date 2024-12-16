import heapq
import pygame
from Grid_making import Grid

class AStar:
    def __init__(self, grid, screen):
        self.grid = grid
        self.screen = screen
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, a, b):
        # Use Manhattan distance as the heuristic function
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(self, row, col):
        # Define neighbors (up, down, left, right)
        indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        return [
            (r, c)
            for r, c in indices
            if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != 0
        ]

    def reconstruct_path(self, came_from, current, start, CELL_SIZE):
        # Reconstruct and display the path
        while current != start:
            r, c = current
            self.grid[r][c] = 3  # Mark path
            Grid.draw_grid(self.screen, self.grid, CELL_SIZE)
            pygame.display.flip()
            pygame.time.delay(50)
            current = came_from[current]

    def AStar_img(self, start, goal, CELL_SIZE):
        open_set = []
        heapq.heappush(open_set, (0, start))  # Min-heap with (priority, node)
        came_from = {}
        g_score = {start: 0}  # Cost from start to each node
        f_score = {start: self.heuristic(start, goal)}  # Estimated total cost

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                self.reconstruct_path(came_from, current, start, CELL_SIZE)
                return True

            for neighbor in self.neighbors(*current):
                tentative_g_score = g_score[current] + 1  # Assuming uniform cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    if neighbor not in [n[1] for n in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

            self.grid[current[0]][current[1]] = 2  # Mark visited
            Grid.draw_grid(self.screen, self.grid, CELL_SIZE)
            pygame.display.flip()
            pygame.time.delay(50)

        return False  # No path found