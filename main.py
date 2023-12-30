import pygame
import sys
import random

# button class - surface and rectangle combined, must be placed in a group
class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(buttonName).convert_alpha()
        self.rect = self.image.get_rect

pygame.init()

# setup game window
screenWidth = 1000
screenHeight = 500
pygame.display.set_caption('Clicker')
screen = pygame.display.set_mode((screenWidth, screenHeight))
maxFPS = 60

# define variables
buttonWidth = 200
buttonHeight = 200
ostNames = ["xDeviruchi - Title Theme .wav", "xDeviruchi - Minigame .wav"]
bgColour = "linen"
buttonName = "button.png"

# surfaces are like layers in photoshop! you fill each surface with stuff like text/color/images
counterFont = pygame.font.Font('PixelifySans-Bold.ttf', 50)
textSurface = counterFont.render('my game', False, 'orangered')

bgSurface = pygame.Surface((screenWidth, screenHeight))
bgSurface.fill(bgColour)

buttonSurface = pygame.image.load(buttonName).convert_alpha()
buttonSurface = pygame.transform.scale(buttonSurface, (200,200))


# Core part that actually runs everything
def main():
    # random music
    ost = pygame.mixer.music
    ost.load(ostNames[random.randint(0,1)])
    ost.play()

    # entire game runs inside this loop, keeps the code running forever
    while True:
        # check each frame for events that occur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # place surfaces onto screen surface
        screen.blit(bgSurface, (0,0))
        screen.blit(buttonSurface, (400,200))
        screen.blit(textSurface, (400, 100))

        # update everything
        pygame.display.update()
        pygame.time.Clock().tick(maxFPS)


main()