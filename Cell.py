import pygame


class Cell:

    def color(self, screen):
        pygame.draw.rect(screen, "WHITE", (self.pos[0] + 5, self.pos[1] + 5, 30, 30))

    def color_top(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0], self.pos[1], 40, 5))

    def color_bot(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0], self.pos[1] + 35, 40, 5))

    def color_left(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0], self.pos[1], 5, 40))

    def color_right(self, screen):
        pygame.draw.rect(screen, "BLACK", (self.pos[0] + 35, self.pos[1], 5, 40))

    def color(self, screen):
        pygame.draw.rect(screen, "WHITE", (self.pos[0] + 5, self.pos[1] + 5, 30, 30))

    def rem_color_top(self, screen):
        pygame.draw.rect(screen, "WHITE", (self.pos[0]+5, self.pos[1], 30, 5))

    def rem_color_bot(self, screen):
        pygame.draw.rect(screen, "WHITE", (self.pos[0]+5, self.pos[1] + 35, 30, 5))

    def rem_color_left(self, screen):
        pygame.draw.rect(screen, "WHITE", (self.pos[0], self.pos[1]+5, 5, 30))

    def rem_color_right(self, screen):
        pygame.draw.rect(screen, "WHITE", (self.pos[0] + 35, self.pos[1]+5, 5, 30))

    def __init__(self, posx, posy, index_input, screen):
        self.left_wall = True
        self.right_wall = True
        self.bottom_wall = True
        self.top_wall = True
        self.adjacent = []
        self.index = index_input
        self.pos = (posx, posy)
        self.visited = False
        self.referrer = ""

        if (posy - 40) >= 0:
            self.adjacent.append(self.index - 12)

        if (posy + 80) <= 320:
            self.adjacent.append(self.index + 12)

        if (posx - 40) >= 0:
            self. adjacent.append(self.index - 1)

        if (posx + 80) <= 480:
            self.adjacent.append(self.index + 1)

        self.color_bot(screen)
        self.color_left(screen)
        self.color_right(screen)
        self.color_top(screen)





