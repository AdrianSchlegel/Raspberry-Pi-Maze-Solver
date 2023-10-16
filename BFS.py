import time
import pygame
from functions import calc_neighbours, color_walls, generate_index, draw_path
from config import COLOR_SEARCHING, COLOR_PATH, COLOR_SEARCHED, SLEEP_SEARCH


def generate_path(cell_array):
    path = [cell_array[-1]]  # Start from the last cell

    visited = set()  # set to keep track of visited cells for quick lookup
    visited.add(cell_array[-1].index)

    while path[-1].index != cell_array[0].index:
        neighbours = calc_neighbours(path[-1], cell_array, False, False)

        # Filter out neighbors that have already been visited
        neighbours = [n for n in neighbours if n.index not in visited and n.searched]

        if not neighbours:
            # No valid neighbors found; break the loop
            break

        # Get the neighbor with the lowest index
        next_cell = min(neighbours, key=lambda obj: obj.searchindex)

        path.append(next_cell)  # Append this cell to the path
        visited.add(next_cell.index)  # Mark the cell as visited

    path.append(cell_array[-1])  # Add the starting cell at the end of the path for completeness

    return path[::-1]  # Reverse the path to go from start to end

def bfs_algo(cell_array, screen):
    target = cell_array[-1]
    current = cell_array[0]
    queue = [current]
    run = 0
    path = []

    while current != target:
        run += 1
        generate_index(current, cell_array, run)
        current = queue.pop(0)
        current.draw_body(COLOR_SEARCHING, screen)
        color_walls(current, cell_array, COLOR_SEARCHING, screen)
        pygame.display.flip()
        time.sleep(SLEEP_SEARCH)
        current.searched = True
        neighbours = calc_neighbours(current, cell_array, True, True)

        for i in neighbours:
            queue.append(i)

        current.draw_body(COLOR_SEARCHED, screen)
        color_walls(current, cell_array, COLOR_SEARCHED, screen)

        pygame.display.flip()

        if len(neighbours) == 0:
            if current == target:
                break
            continue

    generate_index(cell_array[-1], cell_array, run + 1)
    path = generate_path(cell_array)
    draw_path(path, cell_array, COLOR_PATH, screen)
