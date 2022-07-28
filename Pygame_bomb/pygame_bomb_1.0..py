import pygame
from random import randint
from glob import glob

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomb")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.SysFont("comicsans", 50)


plane_posx = 0
plane_posy = 0
plane = pygame.image.load("airplane.png")

    
    
def draw_plane():
    WIN.blit(plane, (plane_posx, plane_posy))

def handle_movement(keys):

    if keys[pygame.K_d]:
        plane_posx += 4

def draw_explosion():
    explosion = pygame.image.load("explosion.png")
    WIN.blit(explosion, (tank_posx, tank_posy - 50))

def move_bomb():
    bomb = pygame.image.load("bomb.png")
    global bomb_posx
    global bomb_posy
    bomb_posx = plane_posx + 22
    bomb_posy = plane_posy + 70
    WIN.blit(bomb, (bomb_posx, bomb_posy))
    for i in range(439):
        bomb_posy += 1
        WIN.fill(BLACK)
        WIN.blit(bomb, (bomb_posx, bomb_posy))
        WIN.blit(plane, (plane_posx, plane_posy))
        #WIN.blit(tank, (tank_posx, tank_posy))
        pygame.display.update()
        pygame.time.delay(8)
        if bomb_posx == tank_posx and bomb_posy == tank_posy - 25:# and bomb_posx in range(tank_pos_min, tank_pos_max + 1):
            #pygame.time.delay(3920)
            draw_explosion()

def handle_bomb():
    if keys[pygame.K_SPACE]:
        move_bomb()
            

def draw_tank():
    #global tank
    global tank_posx
    global tank_posy
    global tank_pos_min
    global tank_pos_max
    tank_posx = tank_pos_min = 0
    tank_posy = HEIGHT - 40
    tank_pos_max = 70
    #tank = pygame.image.load("tank.png")
    #WIN.blit(tank, (tank_posx, tank_posy))

    

def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(BLACK)
    
   


    while run:
        clock.tick(FPS)
        global keys
        keys = pygame.key.get_pressed()
        draw_plane()
        handle_bomb()
        draw_tank()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()