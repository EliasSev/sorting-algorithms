import pygame
import sys
import numpy as np
import matplotlib.pylab as pl

class Graphics:

    def __init__(self, L, width, height, fps=60, color_range=None):
        self.L = L
        self.width = width
        self.height = height
        self.fps = fps

        if color_range is None:
            self.color_range = (0, 1)
        else:
            self.color_range = color_range

    
    def draw_fps(self):
        fps = "[" + str(int(self.clock.get_fps())) + "]"
        text_obj = self.fps_font.render(fps, True, (255, 0, 0))
        self.window.blit(text_obj, (7, -2))


    def draw_squares(self, A):
        n = len(A)
        c0, c1 = self.color_range
        colors = [(r, g, b) for r, g, b, _ in 
                  pl.cm.jet(np.linspace(c0, c1, self.height))*255]
        widths = np.linspace(0, self.width, n+1)
        avg_width = self.width / n 

        for i in range(n):
            body = pygame.Rect(widths[i], self.height-A[i],  # start from x, -y
                               avg_width, A[i])              # rectangle dim
            pygame.draw.rect(self.window, colors[int(A[i]-1)], body)


    def update(self):
        while True:
            for A in self.L:
                self.window.fill((0, 0, 0))
                self.draw_squares(A)
                self.draw_fps()
                self.clock.tick(self.fps)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


    def start(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.fps_font = pygame.font.SysFont('arialblack', 13)
        pygame.display.set_caption('Sorting Algorithms')
        self.update()
