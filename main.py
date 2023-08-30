import random
import time
import pygame
from Cell import Cell
import BFS
import DFS


def check_rel(initial, goto):
    if initial.pos[0] == goto.pos[0] - 20:
        initial.rem_color_right("WHITE", screen)
        initial.right_wall = False
        goto.rem_color_left("WHITE", screen)
        goto.left_wall = False
        return "left"
    if initial.pos[0] == goto.pos[0] + 20:
        initial.rem_color_left("WHITE", screen)
        initial.left_wall = False
        goto.rem_color_right("WHITE", screen)
        goto.right_wall = False
        return "right"
    if initial.pos[1] == goto.pos[1] + 20:
        initial.rem_color_top("WHITE", screen)
        initial.top_wall = False
        goto.rem_color_bot("WHITE", screen)
        goto.bottom_wall = False
        return "top"
    if initial.pos[1] == goto.pos[1] - 20:
        initial.rem_color_bot("WHITE", screen)
        initial.bottom_wall = False
        goto.rem_color_top("WHITE", screen)
        goto.top_wall = False
        return "top"
    else:
        return "error"


pygame.init()
screen = pygame.display.set_mode((480, 320))
clock = pygame.time.Clock()
running = True
loops = 0

while running:
    cell_array = []
    loops += 1
    for y in range(0, 301, 20):
        for x in range(0, 461, 20):
            new_cell = Cell(x, y, len(cell_array), screen)
            cell_array.append(new_cell)

    pygame.display.flip()

    previous_cell = cell_array[0]
    pygame.draw.rect(screen, "BLUE", (2, 2, 16, 16))

    previous_cell.color_top(screen)
    current_cell = cell_array[previous_cell.adjacent[random.randint(0, len(previous_cell.adjacent))-1]]
    current_cell.referrer = previous_cell
    current_cell.adjacent.remove(previous_cell.index)
    if 0 in cell_array[24].adjacent:
        cell_array[24].adjacent.remove(0)
    if 0 in cell_array[1].adjacent:
        cell_array[1].adjacent.remove(0)
    check_rel(current_cell, previous_cell)
    current_cell.visited = True
    previous_cell.visited = True

    counter = 0

    while current_cell.pos != (0, 0):
        current_cell.color("WHITE", screen)
        pygame.display.flip()
        time.sleep(0.05)
        previous_cell = current_cell

        if len(current_cell.adjacent) == 0:
            if (current_cell.pos[1] - 20) >= 0:
                if current_cell.index in cell_array[current_cell.index - 24].adjacent:
                    cell_array[current_cell.index - 24].adjacent.remove(current_cell.index)
            if (current_cell.pos[1] + 40) <= 320:
                if current_cell.index in cell_array[current_cell.index + 24].adjacent:
                    cell_array[current_cell.index + 24].adjacent.remove(current_cell.index)
            if (current_cell.pos[0] - 20) >= 0:
                if current_cell.index in cell_array[current_cell.index - 1].adjacent:
                    cell_array[current_cell.index - 1].adjacent.remove(current_cell.index)
            if (current_cell.pos[0] + 40) <= 480:
                if current_cell.index in cell_array[current_cell.index + 1].adjacent:
                    cell_array[current_cell.index + 1].adjacent.remove(current_cell.index)
            current_cell = current_cell.referrer
            previous_cell = current_cell.referrer
            continue

        if (current_cell.pos[1] - 20) >= 0:
            if current_cell.index in cell_array[current_cell.index - 24].adjacent:
                cell_array[current_cell.index - 24].adjacent.remove(current_cell.index)
        if (current_cell.pos[1] + 40) <= 320:
            if current_cell.index in cell_array[current_cell.index + 24].adjacent:
                cell_array[current_cell.index + 24].adjacent.remove(current_cell.index)
        if (current_cell.pos[0] - 20) >= 0:
            if current_cell.index in cell_array[current_cell.index - 1].adjacent:
                cell_array[current_cell.index - 1].adjacent.remove(current_cell.index)
        if (current_cell.pos[0] + 40) <= 480:
            if current_cell.index in cell_array[current_cell.index + 1].adjacent:
                cell_array[current_cell.index + 1].adjacent.remove(current_cell.index)

        current_cell = cell_array[previous_cell.adjacent[random.randint(0, len(previous_cell.adjacent)) - 1]]
        current_cell.referrer = previous_cell
        check_rel(current_cell, previous_cell)
        pygame.display.flip()


    ## Change
    pygame.draw.rect(screen, "BLUE", (2, 2, 16, 16))
    pygame.draw.rect(screen, "RED", (462, 302, 16, 16))
    pygame.display.flip()
    time.sleep(1)
    if loops%2 == 0:
        BFS.bfs_algo(cell_array, screen)
        loops = 0
    else:
        DFS.dfs_algo(cell_array, screen)
    time.sleep(2)
    screen.fill((0, 0, 0))

    pygame.display.flip()
