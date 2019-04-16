import pygame



pygame.init()

#crash_sound = pygame.mixer.Sound("???")
display_width = 
display_height = 
car_width = 

#showing the game box and title
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('???')

color1 = (0,0,0)
color2 = (255,255,255)

clock = pygame.time.Clock()
sprite = pygame.image.load('???')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(sprite, (x,y))

def game_loop():

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(???)
        car(x,y)

            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()