import pygame
import random

from cell import TILE_SIZE
from grid import Grid
from robot import Robot
import preprogrammed

RESOLUTION = WIDTH, HEIGHT = 702, 802
BACKGROUND = pygame.Color('gray')
random.seed(10)

cols, rows = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE

pygame.init()
surface = pygame.display.set_mode(RESOLUTION)
surface.fill(BACKGROUND)
pygame.display.set_caption('Maze Bot')
clock = pygame.time.Clock()

grid = Grid(rows, cols)

robot = Robot(grid.cells[52])


def main():
    gen_maze(10)
    while True:
        for event in pygame.event.get():
            if robot.current_cell.is_goal:
                gen_maze(10)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                key_down(event.key)

        for cell in grid.cells:
            cell.draw(surface)
        robot.draw(surface)
        pygame.display.update()
        clock.tick(60)


def key_down(key):

    if key == pygame.K_UP:
        neighbors = grid.get_neighbors(robot.current_cell)
        robot.move('up', neighbors)
    elif key == pygame.K_DOWN:
        neighbors = grid.get_neighbors(robot.current_cell)
        robot.move('down', neighbors)
    elif key == pygame.K_LEFT:
        neighbors = grid.get_neighbors(robot.current_cell)
        robot.move('left', neighbors)
    elif key == pygame.K_RIGHT:
        neighbors = grid.get_neighbors(robot.current_cell)
        robot.move('right', neighbors)
    elif key == pygame.K_RETURN:
        if robot.programmed:
            neighbors = grid.get_neighbors(robot.current_cell)
            robot.move(robot.programmed.popleft(), neighbors)
        else:
            preprogrammed.main(robot)


def gen_maze(length):
    clear_maze()
    robot.reset()
    current_index = grid.start_index
    current_cell = grid.cells[current_index]
    prev_direction = None
    for i in range(length):
        neighbor_cells = grid.get_neighbors(current_cell)
        valid_directions = get_valid_directions(neighbor_cells)

        try:
            direction = random.choice(valid_directions)
            next_cell = neighbor_cells[direction]
            next_cell.in_maze = True
        except IndexError:
            break

        current_cell.add_walls(direction, prev_direction)

        current_cell = next_cell
        prev_direction = direction

    current_cell.is_goal = True
    current_cell.add_walls(None, prev_direction)


def clear_maze():
    for cell in grid.cells:
        if not cell.is_start:
            cell.is_goal = False
            cell.in_maze = False

        for wall in cell.walls:
            cell.walls[wall] = False

        surface.fill(BACKGROUND)


def get_valid_directions(neighbor_cells):
    valid_neighbors = []
    for key, cell in neighbor_cells.items():
        if cell and not cell.in_maze:
            valid_neighbors.append(key)
    return valid_neighbors


if __name__ == "__main__":
    main()
