import pygame.draw

TILE_SIZE = 100


class Cell:

    def __init__(self, col, row):
        self.col, self.row = col, row
        self.x, self.y = self.col * TILE_SIZE, self.row * TILE_SIZE
        self.walls = {'up': False, 'right': False, 'left': False, 'down': False}
        self.in_maze = False
        self.visited = False
        self.is_start = False
        self.is_goal = False

    def draw(self, surface):
        x, y = self.col * TILE_SIZE, self.row * TILE_SIZE
        if self.in_maze:
            if self.is_start:
                color = pygame.Color('white')
            elif self.is_goal:
                color = pygame.Color('red')
            else:
                color = pygame.Color('aqua')
            pygame.draw.rect(surface, color, (x, y, TILE_SIZE, TILE_SIZE))

            # draws edges
            self.draw_edge(surface, self.walls['up'], (x, y), (x + TILE_SIZE, y))
            self.draw_edge(surface, self.walls['down'], (x, y + TILE_SIZE), (x + TILE_SIZE, y + TILE_SIZE))
            self.draw_edge(surface, self.walls['left'], (x, y), (x, y + TILE_SIZE))
            self.draw_edge(surface, self.walls['right'], (x + TILE_SIZE, y), (x + TILE_SIZE, y + TILE_SIZE))

    @staticmethod
    def draw_edge(view, is_wall: bool, start: tuple, end: tuple):
        if is_wall:
            pygame.draw.line(view, pygame.Color('black'), start, end, 2)
        else:
            pygame.draw.line(view, pygame.Color('gray'), start, end, 1)

    def get_neighbors(self, rows, cols):
        left = (self.col - 1, self.row) if self.col > 0 else None
        right = (self.col + 1, self.row) if self.col < cols - 1 else None
        up = (self.col, self.row - 1) if self.row > 0 else None
        down = (self.col, self.row + 1) if self.row < rows - 1 else None
        return {'left': left, 'right': right, 'up': up, 'down': down}

    def add_walls(self, next_direction, prev_direction):
        skip_walls = list()
        skip_walls.append(next_direction)

        if prev_direction == 'right':
            skip_walls.append('left')
        elif prev_direction == 'left':
            skip_walls.append('right')
        elif prev_direction == 'up':
            skip_walls.append('down')
        elif prev_direction == 'down':
            skip_walls.append('up')

        for wall in self.walls:
            if wall not in skip_walls:
                self.walls[wall] = True

    @property
    def xy(self):
        return self.x, self.y
