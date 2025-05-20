import pygame

class Window:
    instance = None
    def __init__(self):
        Window.instance = self
        pygame.init()
        self.screen = None
        self.clock = None
        self.is_running = True

    def open(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock() 

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("white")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
    def tick(self):
        pygame.display.flip()

        self.clock.tick(60)
    
    def close(self):
        pygame.quit()