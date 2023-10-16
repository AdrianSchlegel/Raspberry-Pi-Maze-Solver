import pygame
from config import (
    CELL_SIZE, CELL_WALL_THICKNESS, CELL_BODY_SIZE,
    CELL_START_SE_WALLS,SCREEN_HEIGHT, SCREEN_WIDTH,
    CELL_ARRAY_ROW_LENGTH, COLOR_WALLS
)

class Cell:
    def draw_body(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0] + CELL_WALL_THICKNESS, self.pos[1] + CELL_WALL_THICKNESS, CELL_BODY_SIZE, CELL_BODY_SIZE))

    def draw_top_wall(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0], self.pos[1], CELL_SIZE, CELL_WALL_THICKNESS))

    def draw_bot_wall(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0], self.pos[1] + CELL_START_SE_WALLS, CELL_SIZE, CELL_WALL_THICKNESS))

    def draw_left_wall(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0], self.pos[1], CELL_WALL_THICKNESS, CELL_SIZE))

    def draw_right_wall(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0] + CELL_START_SE_WALLS, self.pos[1], CELL_WALL_THICKNESS, CELL_SIZE))

    def draw_top_opening(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0] + CELL_WALL_THICKNESS, self.pos[1], CELL_BODY_SIZE, CELL_WALL_THICKNESS))

    def draw_bot_opening(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0] + CELL_WALL_THICKNESS, self.pos[1] + CELL_START_SE_WALLS, CELL_BODY_SIZE, CELL_WALL_THICKNESS))

    def draw_left_opening(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0], self.pos[1] + CELL_WALL_THICKNESS, CELL_WALL_THICKNESS, CELL_BODY_SIZE))

    def draw_right_opening(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0] + CELL_START_SE_WALLS, self.pos[1] + CELL_WALL_THICKNESS, CELL_WALL_THICKNESS, CELL_BODY_SIZE))

    def __init__(self, posx, posy, index_input, screen):
        self.left_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self.top_wall = True
        self.adjacent = []
        self.index = index_input
        self.pos = (posx, posy)
        self.visited = False
        self.searched = False
        self.searchindex = 0
        self.referrer = ""

        if (posy - CELL_SIZE) >= 0:
            self.adjacent.append(self.index - CELL_ARRAY_ROW_LENGTH)

        if (posy + 2*CELL_SIZE) <= SCREEN_HEIGHT:
            self.adjacent.append(self.index + CELL_ARRAY_ROW_LENGTH)

        if (posx - CELL_SIZE) >= 0:
            self. adjacent.append(self.index - 1)

        if (posx + 2*CELL_SIZE) <= SCREEN_WIDTH:
            self.adjacent.append(self.index + 1)

        self.draw_bot_wall(COLOR_WALLS, screen)
        self.draw_left_wall(COLOR_WALLS, screen)
        self.draw_right_wall(COLOR_WALLS, screen)
        self.draw_top_wall(COLOR_WALLS, screen)
