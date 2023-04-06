import pygame
import os

class main():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('asset/fond.png').convert()
        self.background = pygame.transform.smoothscale(self.background, self.window.get_size())
        self.play_button = pygame.sprite.Sprite()
        self.play_button.image = pygame.transform.scale(pygame.image.load('asset/play.png'),(180, 104))
        self.play_button.rect = self.play_button.image.get_rect()
        self.play_button.rect.center = self.window.get_rect().center
        


        run = True
        while run:
            self.clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.play_button.rect.collidepoint(event.pos):
                            print('button cliqué')

            self.window.blit(self.background, (0, 0))
            self.window.blit(self.play_button.image, self.play_button.rect)


            pygame.display.flip()

        pygame.quit()
    
    def main_screen():
        return False
