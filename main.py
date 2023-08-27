import random
import time
import pygame
from Cell import Cell
import algs4

def check_rel(initial, goto):
    if initial.pos[0] == goto.pos[0] - 40:
        initial.rem_color_right(screen)
        initial.right_wall = False
        goto.rem_color_left(screen)
        goto.left_wall = False
        return "left"
    if initial.pos[0] == goto.pos[0] + 40:
        initial.rem_color_left(screen)
        initial.left_wall = False
        goto.rem_color_right(screen)
        goto.right_wall = False
        return "right"
    if initial.pos[1] == goto.pos[1] + 40:
        initial.rem_color_top(screen)
        initial.top_wall = False
        goto.rem_color_bot(screen)
        goto.bot_wall = False
        return "top"
    if initial.pos[1] == goto.pos[1] - 40:
        initial.rem_color_bot(screen)
        initial.bottom_wall = False
        goto.rem_color_top(screen)
        goto.top_wall = False
        return "top"
    else:
        return "error"


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
cell_array = []

for y in range(0, 281, 40):
    for x in range(0, 441, 40):
        new_cell = Cell(x, y, len(cell_array), screen)
        cell_array.append(new_cell)


pygame.display.flip()


previous_cell = cell_array[0]
pygame.draw.rect(screen, "BLUE", (5, 5, 30, 30))

previous_cell.color_top(screen)
current_cell = cell_array[previous_cell.adjacent[random.randint(0, len(previous_cell.adjacent))-1]]
current_cell.referrer = previous_cell
current_cell.adjacent.remove(previous_cell.index)
if 0 in cell_array[12].adjacent:
    cell_array[12].adjacent.remove(0)
if 0 in cell_array[1].adjacent:
    cell_array[1].adjacent.remove(0)
check_rel(current_cell, previous_cell)
current_cell.visited = True
previous_cell.visited = True


while current_cell.pos != (0, 0):
    current_cell.color(screen)
    pygame.display.flip()
    time.sleep(0.05)
    previous_cell = current_cell

    if len(current_cell.adjacent) == 0:
        if (current_cell.pos[1] - 40) >= 0:
            if current_cell.index in cell_array[current_cell.index - 12].adjacent:
                cell_array[current_cell.index - 12].adjacent.remove(current_cell.index)
        if (current_cell.pos[1] + 80) <= 320:
            if current_cell.index in cell_array[current_cell.index + 12].adjacent:
                cell_array[current_cell.index + 12].adjacent.remove(current_cell.index)
        if (current_cell.pos[0] - 40) >= 0:
            if current_cell.index in cell_array[current_cell.index - 1].adjacent:
                cell_array[current_cell.index - 1].adjacent.remove(current_cell.index)
        if (current_cell.pos[0] + 80) <= 480:
            if current_cell.index in cell_array[current_cell.index + 1].adjacent:
                cell_array[current_cell.index + 1].adjacent.remove(current_cell.index)
        current_cell = current_cell.referrer
        previous_cell = current_cell.referrer
        time.sleep(0.0000005)
        continue

    if (current_cell.pos[1] - 40) >= 0:
        if current_cell.index in cell_array[current_cell.index - 12].adjacent:
            cell_array[current_cell.index - 12].adjacent.remove(current_cell.index)
    if (current_cell.pos[1] + 80) <= 320:
        if current_cell.index in cell_array[current_cell.index + 12].adjacent:
            cell_array[current_cell.index + 12].adjacent.remove(current_cell.index)
    if (current_cell.pos[0] - 40) >= 0:
        if current_cell.index in cell_array[current_cell.index - 1].adjacent:
            cell_array[current_cell.index - 1].adjacent.remove(current_cell.index)
    if (current_cell.pos[0] + 80) <= 480:
        if current_cell.index in cell_array[current_cell.index + 1].adjacent:
            cell_array[current_cell.index + 1].adjacent.remove(current_cell.index)

    current_cell = cell_array[previous_cell.adjacent[random.randint(0, len(previous_cell.adjacent)) - 1]]
    current_cell.referrer = previous_cell
    check_rel(current_cell, previous_cell)
    pygame.display.flip()

pygame.draw.rect(screen, "BLUE", (5, 5, 30, 30))
pygame.draw.rect(screen, "RED", (445, 285, 30, 30))
pygame.display.flip()

# A*


while running:
    pygame.display.flip()

