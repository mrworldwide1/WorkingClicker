import pygame
import sys
import random

pygame.init()

# setup game window
screenWidth = 1000
screenHeight = 500
pygame.display.set_caption('Clicker')
screen = pygame.display.set_mode((screenWidth, screenHeight))
maxFPS = 60

# define variables
ostNames = ["xDeviruchi - Title Theme .wav", "xDeviruchi - Minigame .wav"]
bgColour = "linen"
buttonName = "button.png"

# button's surface and rectangle combined, must be placed in a group
class Button(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self) # ensure the class inherits from parent Sprite class
        self.image = pygame.image.load(buttonName).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect(center = (screenWidth/2, screenHeight/2))

# surfaces are like layers in photoshop! you fill each surface with stuff like text/color/images
counterFont = pygame.font.Font('PixelifySans-Bold.ttf', 50)
textSurface = counterFont.render('clicks', False, 'orangered')

# create sprite group for lone button
buttons = pygame.sprite.GroupSingle()
buttons.add(Button(250, 250))


# Core part that actually runs everything
def main():
    ost = pygame.mixer.music
    ost.load(ostNames[random.randint(0,1)])
    ost.play()

    # entire game runs inside this loop, keeps the code running forever
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # place surfaces onto screen surface
        screen.fill(bgColour)
        screen.blit(textSurface, (400, 100))
        # draw buttons sprite group
        buttons.draw(screen)

        # update everything
        pygame.display.update()
        pygame.time.Clock().tick(maxFPS)


main()