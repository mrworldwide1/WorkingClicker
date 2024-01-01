import pygame
import sys
import random

# basic setup
pygame.init()
screenWidth = 1000
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
icon = pygame.image.load("button.png").convert_alpha()
counterFont = pygame.font.Font('PixelifySans-Bold.ttf', 50)
pygame.display.set_caption('Clicker')
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
        if pygame.mouse.get_pressed()[0]:
            if self.lock == False:
                self.lock = True
                global clicks # variable scope
                clicks += 1
        elif not pygame.mouse.get_pressed()[0]:
            self.lock = False

    def update(self):
        self.clicked()

def counter():
    textSurface = counterFont.render(f"{clicks}", False, 'orangered')
    screen.blit(textSurface, (430, 80))

# button sprite
buttons = pygame.sprite.GroupSingle()
buttons.add(Button(200, 200))

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
    counter()
    buttons.draw(screen)
    buttons.update()

    # update everything
    pygame.display.update()
    clock.tick(60)