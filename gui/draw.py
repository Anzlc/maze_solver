import pygame
from consts import WIDTH, HEIGHT
from gui.window import Window

class Draw:
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    @staticmethod
    def set_cell(x,y, id):
        Draw.grid[y][x] = id

    @staticmethod
    def draw_grid():
        w,h = pygame.display.get_window_size()
        cell_size = w // WIDTH
        for y in range(HEIGHT):
            for x in range(WIDTH):
                clr = pygame.Color(255,255,255) if Draw.grid[y][x] == 0 else pygame.Color(0,0,0)
                
                pygame.draw.rect(Window.instance.screen, clr, (x * cell_size, y*cell_size, cell_size, cell_size))

        