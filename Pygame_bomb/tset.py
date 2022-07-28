import pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomb")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

run = True

def drop_bomb():
    bomb = pygame.image.load("bomb.png")
    bomb_posx = 300
    bomb_posy = 400
    WIN.blit(bomb, (400, bomb_posx))
    for i in range(bomb_posx - 32):
        bomb_posx += 1
        WIN.fill(BLACK)
        WIN.blit(bomb, (400, bomb_posx))
        pygame.display.update()
        pygame.time.delay(8)



def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(BLACK)
    
    while run:
        clock.tick(FPS)
        global keys
        keys = pygame.key.get_pressed()
        drop_bomb()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()