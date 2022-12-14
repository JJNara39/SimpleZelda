import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        # Usual setup stuff
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.title = pygame.display.set_caption("Zelda-Clone")
        self.clock = pygame.time.Clock()
        
        self.level = Level()

        # sounds
        main_sound = pygame.mixer.Sound('..\\SimpleZelda\\audio\\main.wav')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()