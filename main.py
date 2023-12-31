import pygame
import sys
import random

pygame.init()

# setup game window
screenWidth = 1000
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Clicker')
icon = pygame.image.load("button.png").convert_alpha()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# define variables
ostNames = ["xDeviruchi - Title Theme .wav", "xDeviruchi - Minigame .wav"]
bgColour = "linen"
clicks = 0

# button's surface and rectangle combined, must be placed in a group
class Button(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self) # ensure the class inherits from parent Sprite class
        buttonName = "button.png"
        self.lock = False
        self.image = pygame.image.load(buttonName).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect(center = (screenWidth/2, screenHeight/2)) # place rectangle in center of screen
    
    def clicked(self):
        # locking mechanism to prevent holding down left click
        if pygame.mouse.get_pressed()[0]:
            if self.lock == False:
                self.lock = True
                print(clicks)
                clicks += 1
        elif not pygame.mouse.get_pressed()[0]:
            self.lock = False

    def update(self):
        self.clicked()

# surfaces are like layers in photoshop! you fill each surface with stuff like text/color/images
counterFont = pygame.font.Font('PixelifySans-Bold.ttf', 50)
textSurface = counterFont.render(f"{clicks}", False, 'orangered')

# sprite group for lone button
buttons = pygame.sprite.GroupSingle()
buttons.add(Button(200, 200))

# Core part that actually runs everything
def main():
    ost = pygame.mixer.music
    ost.load(ostNames[random.randint(0,1)])
    ost.play()

    # entire game runs inside this loop, keeps the code running forever
    while True:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # place surfaces onto screen surface
        screen.fill(bgColour)
        screen.blit(textSurface, (430, 80))
        # draw buttons sprite group
        buttons.draw(screen)
        buttons.update() # calls update method inside Button class, in turn running other methods

        # update everything
        pygame.display.update()
        clock.tick(60)


main()