import pygame, sys

from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        
        self.running = True
        
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        
    def main(self):
        while self.running:
            self.update()
            self.events()
            self.draw()
    
    def draw(self):
        self.screen.fill((24, 102, 2))
        
        self.clock.tick(FPS)
        pygame.display.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if pygame.K_ESCAPE:
                    self.running = False
    
    def new(self):
        pass
    
    def update(self):
        pass
    
if __name__ == "__main__":
    game = Game()
    game.new()
    game.main()
    pygame.quit()
    sys.exit()