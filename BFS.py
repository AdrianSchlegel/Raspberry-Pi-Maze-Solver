import time
import pygame
import random

def color_walls(cell, cell_array, color, screen):
    if not cell.left_wall:
        if cell_array[cell.index-1].searched:
            cell.rem_color_left(color, screen)
            cell_array[cell.index-1].rem_color_right(color, screen)
    if not cell.right_wall:
        if cell_array[cell.index+1].searched:
            cell.rem_color_right(color, screen)
            cell_array[cell.index+1].rem_color_left(color, screen)
    if not cell.top_wall:
        if cell_array[cell.index-24].searched:
            cell.rem_color_top(color, screen)
            cell_array[cell.index-24].rem_color_bot(color, screen)
    if not cell.bottom_wall:
        if cell_array[cell.index+24].searched:
            cell.rem_color_bot(color, screen)
            cell_array[cell.index+24].rem_color_top(color, screen)



def calc_neighbours(v, cell_array, filter):
    neighbours = []
    if not v.left_wall:
        neighbours.append(cell_array[v.index-1])
    if not v.right_wall:
        neighbours.append(cell_array[v.index+1])
    if not v.top_wall:
        neighbours.append(cell_array[v.index-24])
    if not v.bottom_wall:
        neighbours.append(cell_array[v.index+24])

    if filter:
        neighbours = [i for i in neighbours if not i.searched]

    if filter:
        random.shuffle(neighbours) #this to not optimize to current start and goal layout
    return neighbours


def generate_index(cell, cell_array, index):
    cell_array[cell.index].searchindex = index


def generate_path(cell_array):
    path = [cell_array[-1]]  # Start from the last cell

    visited = set()  # Use a set to keep track of visited cells for quick lookup
    visited.add(cell_array[-1].index)

    while path[-1].index != cell_array[0].index:
        neighbours = calc_neighbours(path[-1], cell_array, False)

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



def draw_path(path, cell_array, color, screen):
    for i in range(len(path) - 1):
        current_cell = path[i].index
        next_cell = path[i + 1].index

        difference = next_cell - current_cell

        cell_array[current_cell].color(color, screen)

        if difference == 1:
            cell_array[current_cell].rem_color_right(color, screen)
            cell_array[next_cell].rem_color_left(color, screen)
            pass
        elif difference == -1:
            cell_array[current_cell].rem_color_left(color, screen)
            cell_array[next_cell].rem_color_right(color, screen)
            pass
        elif difference == 24:
            cell_array[current_cell].rem_color_bot(color, screen)
            cell_array[next_cell].rem_color_top(color, screen)
            pass
        elif difference == -24:
            cell_array[current_cell].rem_color_top(color, screen)
            cell_array[next_cell].rem_color_bot(color, screen)
            pass
        pygame.display.flip()
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
        current.color("YELLOW", screen)
        color_walls(current, cell_array, "YELLOW", screen)
        pygame.display.flip()
        time.sleep(0.1)
        current.searched = True
        neighbours = calc_neighbours(current, cell_array, True)

        for i in neighbours:
            queue.append(i)

        current.color_searched(screen)
        color_walls(current, cell_array, "ORANGE", screen)
        current.color("ORANGE", screen)
        pygame.display.flip()

        if len(neighbours) == 0:
            if current == target:
                break
            continue

    generate_index(cell_array[-1], cell_array, run + 1)
    path = generate_path(cell_array)
    draw_path(path, cell_array, "BLUE", screen)
