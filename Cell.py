import pygame


class Cell:

    def color(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0] + 2, self.pos[1] + 2, 16, 16))

    def color_searched(self, screen):
        pygame.draw.rect(screen, "ORANGE", (self.pos[0] + 2, self.pos[1] + 2, 16, 16))

    def color_top(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0], self.pos[1], 20, 2))

    def color_bot(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0], self.pos[1] + 18, 20, 2))

    def color_left(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0], self.pos[1], 2, 20))

    def color_right(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0] + 18, self.pos[1], 2, 20))

    def rem_color_top(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0]+2, self.pos[1], 16, 2))

    def rem_color_bot(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0]+2, self.pos[1] + 18, 16, 2))

    def rem_color_left(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0], self.pos[1]+2, 2, 16))

    def rem_color_right(self, color, screen):
        pygame.draw.rect(screen, color, (self.pos[0] + 18, self.pos[1]+2, 2, 16))

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

        if (posy - 20) >= 0:
            self.adjacent.append(self.index - 24)

        if (posy + 40) <= 320:
            self.adjacent.append(self.index + 24)

        if (posx - 20) >= 0:
            self. adjacent.append(self.index - 1)

        if (posx + 40) <= 480:
            self.adjacent.append(self.index + 1)

        self.color_bot(screen)
        self.color_left(screen)
        self.color_right(screen)
        self.color_top(screen)
