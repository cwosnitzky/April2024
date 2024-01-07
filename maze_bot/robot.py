import os
from pygame import image, transform
from collections import deque

from cell import TILE_SIZE


class Robot:
    def __init__(self, start_cell):
        self.start_cell = start_cell
        self.current_cell = start_cell
        self.base_image = image.load(os.path.join('images', 'robot.png'))
        self.image = transform.scale(self.base_image, (TILE_SIZE, TILE_SIZE))

        self.programmed = deque()

    def draw(self, surface):
        surface.blit(self.image, self.current_cell.xy)

    def move(self, direction, neighbors):
        next_cell = neighbors[direction]
        if next_cell and next_cell.in_maze and not self.current_cell.walls[direction]:
            self.current_cell = neighbors[direction]

    def reset(self):
        self.current_cell = self.start_cell

    # meant for students to pre-program movement
    def go_up(self, steps=1):
        self.programmed.extend(['up' for i in range(steps)])

    def go_down(self, steps=1):
        self.programmed.extend(['down' for i in range(steps)])

    def go_left(self, steps=1):
        self.programmed.extend(['left' for i in range(steps)])

    def go_right(self, steps=1):
        self.programmed.extend(['right' for i in range(steps)])
