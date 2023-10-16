import random
import time
import pygame
from Cell import Cell
from config import (
    CELL_SIZE, CELL_WALL_THICKNESS, CELL_BODY_SIZE,
    SCREEN_HEIGHT, SCREEN_WIDTH, CELL_ARRAY_ROW_LENGTH,
    COLOR_CELL, COLOR_GOAL, COLOR_START,
    SLEEP_MAZE_GEN, SLEEP_START_SEARCH, SCREEN_BORDERLESS
)
from functions import check_rel
import BFS
import DFS


pygame.init()

# Create window with optional borderless mode
if SCREEN_BORDERLESS:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



clock = pygame.time.Clock()
running = True
loops = 0

while running:
    cell_array = []
    loops += 1

    # Create cells based on screen dimensions
    for y in range(0, SCREEN_HEIGHT-1, CELL_SIZE):
        for x in range(0, SCREEN_WIDTH-1, CELL_SIZE):
            new_cell = Cell(x, y, len(cell_array), screen)
            cell_array.append(new_cell)

    pygame.display.flip()
    #time.sleep(1)
    previous_cell = cell_array[0]
    pygame.draw.rect(screen, COLOR_START, (CELL_WALL_THICKNESS, CELL_WALL_THICKNESS, CELL_BODY_SIZE, CELL_BODY_SIZE))
    #time.sleep(1)


    current_cell = cell_array[previous_cell.adjacent[random.randint(0, len(previous_cell.adjacent))-1]]
    current_cell.referrer = previous_cell
    current_cell.adjacent.remove(previous_cell.index)
    if 0 in cell_array[CELL_ARRAY_ROW_LENGTH].adjacent:
        cell_array[CELL_ARRAY_ROW_LENGTH].adjacent.remove(0)
    if 0 in cell_array[1].adjacent:
        cell_array[1].adjacent.remove(0)
    check_rel(current_cell, previous_cell, screen)
    current_cell.visited = True
    previous_cell.visited = True

    counter = 0

    while current_cell.pos != (0, 0):
        current_cell.draw_body(COLOR_CELL, screen)
        pygame.display.flip()
        time.sleep(SLEEP_MAZE_GEN)
        previous_cell = current_cell

        if len(current_cell.adjacent) == 0:
            if (current_cell.pos[1] - CELL_SIZE) >= 0:
                if current_cell.index in cell_array[current_cell.index - CELL_ARRAY_ROW_LENGTH].adjacent:
                    cell_array[current_cell.index - CELL_ARRAY_ROW_LENGTH].adjacent.remove(current_cell.index)
            if (current_cell.pos[1] + 2*CELL_SIZE) <= SCREEN_HEIGHT:
                if current_cell.index in cell_array[current_cell.index + CELL_ARRAY_ROW_LENGTH].adjacent:
                    cell_array[current_cell.index + CELL_ARRAY_ROW_LENGTH].adjacent.remove(current_cell.index)
            if (current_cell.pos[0] - CELL_SIZE) >= 0:
                if current_cell.index in cell_array[current_cell.index - 1].adjacent:
                    cell_array[current_cell.index - 1].adjacent.remove(current_cell.index)
            if (current_cell.pos[0] + 2*CELL_SIZE) <= SCREEN_WIDTH:
                if current_cell.index in cell_array[current_cell.index + 1].adjacent:
                    cell_array[current_cell.index + 1].adjacent.remove(current_cell.index)
            current_cell = current_cell.referrer
            previous_cell = current_cell.referrer
            continue

        if (current_cell.pos[1] - CELL_SIZE) >= 0:
            if current_cell.index in cell_array[current_cell.index - CELL_ARRAY_ROW_LENGTH].adjacent:
                cell_array[current_cell.index - CELL_ARRAY_ROW_LENGTH].adjacent.remove(current_cell.index)
        if (current_cell.pos[1] + 2*CELL_SIZE) <= SCREEN_HEIGHT:
            if current_cell.index in cell_array[current_cell.index + CELL_ARRAY_ROW_LENGTH].adjacent:
                cell_array[current_cell.index + CELL_ARRAY_ROW_LENGTH].adjacent.remove(current_cell.index)
        if (current_cell.pos[0] - CELL_SIZE) >= 0:
            if current_cell.index in cell_array[current_cell.index - 1].adjacent:
                cell_array[current_cell.index - 1].adjacent.remove(current_cell.index)
        if (current_cell.pos[0] + 2*CELL_SIZE) <= SCREEN_WIDTH:
            if current_cell.index in cell_array[current_cell.index + 1].adjacent:
                cell_array[current_cell.index + 1].adjacent.remove(current_cell.index)

        current_cell = cell_array[previous_cell.adjacent[random.randint(0, len(previous_cell.adjacent)) - 1]]
        current_cell.referrer = previous_cell
        check_rel(current_cell, previous_cell, screen)
        pygame.display.flip()


    ## Change
    pygame.draw.rect(screen, COLOR_START, (CELL_WALL_THICKNESS, CELL_WALL_THICKNESS, CELL_BODY_SIZE, CELL_BODY_SIZE))
    pygame.draw.rect(screen, COLOR_GOAL, (SCREEN_WIDTH - CELL_SIZE + CELL_WALL_THICKNESS, SCREEN_HEIGHT - CELL_SIZE + CELL_WALL_THICKNESS, CELL_BODY_SIZE, CELL_BODY_SIZE))
    pygame.display.flip()
    time.sleep(SLEEP_START_SEARCH)


    # Switch between search algorithms
    if loops % 2 == 0:
        DFS.dfs_algo(cell_array, screen)
        loops = 0
    else:
        BFS.bfs_algo(cell_array, screen)
    time.sleep(SLEEP_START_SEARCH)
    screen.fill((0, 0, 0))

    pygame.display.flip()
