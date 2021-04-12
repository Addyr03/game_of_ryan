import pygame 
import sys
pygame.init ()

width = 1920
height = 1080
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
tank_speed = 5
dps_speed = 10
fps = 15
clock = pygame.time.Clock () 
screen = pygame.display.set_mode ((width, height))
font = pygame.font.SysFont(None, 25)
pygame.display.set_caption ("art of ryan")
background = pygame.image.load ("map.png").convert()
#define everything here


def line1(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [100,100])

def pause(msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [width/3.5,height/2])
def pauseGame():
    gameisPaused = True
    while gameisPaused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameisPaused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def main ():
    playerstartx = 50
    playerstarty = 810
    run = True

    while run :
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause ("paused", white)
                    pauseGame()
                if event.key == pygame.K_q:
                    run = False
            mouse = pygame.mouse.get_pos ()
            print (mouse) 

        screen.blit(background, [0, 0])

        pygame.draw.rect (screen, white, (50, 810, 30,35))

        line1("esc to pause, then Q to quit :)",red)

        #if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos ()
        if  50 <= mouse [0] <= 50+30 and 810 <= mouse [1] <= 810+35: 
            pygame.draw.rect (screen, red, (playerstartx, playerstarty, 20,20))

        playerstartx += 3
        clock.tick(fps)
        pygame.display.update ()
main ()

