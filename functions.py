import random
import pygame
from Cell import Cell
from config import CELL_SIZE, CELL_ARRAY_ROW_LENGTH, COLOR_CELL

# Check relations between cells
def check_rel(initial, goto, screen):
    if initial.pos[0] == goto.pos[0] - CELL_SIZE:
        initial.draw_right_opening(COLOR_CELL, screen)
        initial.right_wall = False
        goto.draw_left_opening(COLOR_CELL, screen)
        goto.left_wall = False
        return
    if initial.pos[0] == goto.pos[0] + CELL_SIZE:
        initial.draw_left_opening(COLOR_CELL, screen)
        initial.left_wall = False
        goto.draw_right_opening(COLOR_CELL, screen)
        goto.right_wall = False
        return
    if initial.pos[1] == goto.pos[1] + CELL_SIZE:
        initial.draw_top_opening(COLOR_CELL, screen)
        initial.top_wall = False
        goto.draw_bot_opening(COLOR_CELL, screen)
        goto.bottom_wall = False
        return
    if initial.pos[1] == goto.pos[1] - CELL_SIZE:
        initial.draw_bot_opening(COLOR_CELL, screen)
        initial.bottom_wall = False
        goto.draw_top_opening(COLOR_CELL, screen)
        goto.top_wall = False
        return

# Color walls in a cell
def color_walls(cell, cell_array, color, screen):
    if not cell.left_wall:
        if cell_array[cell.index - 1].searched:
            cell.draw_left_opening(color, screen)
            cell_array[cell.index - 1].draw_right_opening(color, screen)
    if not cell.right_wall:
        if cell_array[cell.index + 1].searched:
            cell.draw_right_opening(color, screen)
            cell_array[cell.index + 1].draw_left_opening(color, screen)
    if not cell.top_wall:
        if cell_array[cell.index - CELL_ARRAY_ROW_LENGTH].searched:
            cell.draw_top_opening(color, screen)
            cell_array[cell.index - CELL_ARRAY_ROW_LENGTH].draw_bot_opening(color, screen)
    if not cell.bottom_wall:
        if cell_array[cell.index + CELL_ARRAY_ROW_LENGTH].searched:
            cell.draw_bot_opening(color, screen)
            cell_array[cell.index + CELL_ARRAY_ROW_LENGTH].draw_top_opening(color, screen)

# Calculate neighboring cells
def calc_neighbours(v, cell_array, filter, shuffle):
    neighbours = []
    if not v.left_wall:
        neighbours.append(cell_array[v.index - 1])
    if not v.right_wall:
        neighbours.append(cell_array[v.index + 1])
    if not v.top_wall:
        neighbours.append(cell_array[v.index - CELL_ARRAY_ROW_LENGTH])
    if not v.bottom_wall:
        neighbours.append(cell_array[v.index + CELL_ARRAY_ROW_LENGTH])

    if filter:
        neighbours = [i for i in neighbours if not i.searched]

    if shuffle:
        random.shuffle(neighbours)  # This is to not optimize the current start and goal layout
    return neighbours

# Generate index for searched cells
def generate_index(cell, cell_array, index):
    cell_array[cell.index].searchindex = index

# Draw path to goal
def draw_path(path, cell_array, color, screen):
    for i in range(len(path) - 1):
        current_cell = path[i].index
        next_cell = path[i + 1].index

        difference = next_cell - current_cell

        cell_array[current_cell].draw_body(color, screen)

        if difference == 1:
            cell_array[current_cell].draw_right_opening(color, screen)
            cell_array[next_cell].draw_left_opening(color, screen)
        elif difference == -1:
            cell_array[current_cell].draw_left_opening(color, screen)
            cell_array[next_cell].draw_right_opening(color, screen)
        elif difference == CELL_ARRAY_ROW_LENGTH:
            cell_array[current_cell].draw_bot_opening(color, screen)
            cell_array[next_cell].draw_top_opening(color, screen)
        elif difference == -CELL_ARRAY_ROW_LENGTH:
            cell_array[current_cell].draw_top_opening(color, screen)
            cell_array[next_cell].draw_bot_opening(color, screen)
        pygame.display.flip()
