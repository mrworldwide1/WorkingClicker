import pygame
import sys
import random

pygame.init()

# game window
screenWidth = 1000
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
icon = pygame.image.load("button.png").convert_alpha()
pygame.display.set_caption('Clicker')
pygame.display.set_icon(icon)

# fps limiter
clock = pygame.time.Clock()

# game-wide font
font = pygame.font.Font('PixelifySans-Bold.ttf', 50)

# just for organization
ostNames = ["xDeviruchi - Title Theme .wav", "xDeviruchi - Minigame .wav"]
bgColour = "linen"
clicks = 0

# button's surface and rectangle combined, must be placed in a group
class Button(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        buttonName = "button.png"
        self.lock = False
        self.image = pygame.image.load(buttonName).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect(center = (screenWidth/2, screenHeight/2)) # place rectangle in center of screen

def counter():
    textSurface = font.render(f"{clicks}", False, 'orangered')
    textRect = textSurface.get_rect(center = (screenWidth/2, screenHeight/4))
    screen.blit(textSurface, (textRect))
    print(textRect)

# sprite groups
buttons = pygame.sprite.GroupSingle()
button1 = Button(200, 200)
buttons.add(button1)

# music
ost = pygame.mixer.music
ost.load(ostNames[random.randint(0,1)])
ost.play()

# entire game runs inside this loop, keeps the code running forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.Rect.collidepoint(pygame.mouse.get_pos) and event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1


    # place surfaces onto screen surface
    screen.fill(bgColour)
    counter()
    buttons.draw(screen)

    # update everything
    pygame.display.update()
    clock.tick(60)