import pygame
from random import randint
pygame.init()

SCREEN = pygame.display.set_mode((1000, 500))
BACKGROUND = pygame.transform.scale(pygame.image.load("assets/Sky.png"), (1000, 500))
PLAYER_SPRITES = {
    "idle": pygame.image.load("assets/Ship_Idle.png"),
    "thrust": pygame.image.load("assets/Ship_Thrust.png"),
    "break": pygame.image.load("assets/Ship_Break1.png")
}

CLOUD_SPRITES = {
    "top": pygame.image.load("assets/Cloud_Top.png"),
    "bottom": pygame.image.load("assets/Cloud_Bottom.png")
}

class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y

cloudTop = [pygame.Rect(800, -125, 100, 300)]
cloudBottom = [pygame.Rect(800, 325, 100, 300)]

def main():
    clock = pygame.time.Clock()
    player = pygame.Rect(416, 220, 48, 20)
    playerSpriteSelect = "idle"
    gravity = 0
    score = 0
    canMove = True
    
    startButton = pygame.Rect(420, 190, 150, 75)
    fonts = {
        "big": pygame.font.SysFont('SansSerif', 100),
        "small": pygame.font.SysFont('SansSerif', 25)
    }
    textsurface = fonts["big"].render('Play', False, (150, 150, 150))
    paused = False
    startMenu = True
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if canMove:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.type == pygame.MOUSEBUTTONDOWN:
                        gravity = -3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gravity = -3
                    
        while startMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    startMenu = False
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if startButton.collidepoint(pos):
                        startMenu = False
            SCREEN.blit(BACKGROUND, (0, 0))
            SCREEN.blit(fonts["big"].render('SPACESHIP DODGE', False, (100, 100, 100)), (175, 55))
            SCREEN.blit(fonts["big"].render('SPACESHIP DODGE', False, (150, 150, 150)), (170, 50))
            SCREEN.blit(fonts["small"].render('a flappy bird clone by Jason JR.', False, (150, 150, 150)), (170, 115))
            SCREEN.blit(fonts["big"].render('Play', False, (100, 100, 100)), (425, 195))
            SCREEN.blit(textsurface, startButton)
            pygame.display.flip()
            
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            paused = True
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        paused = False
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if startButton.collidepoint(pos):
                            paused = False
                SCREEN.blit(fonts["big"].render('Resume', False, (100, 100, 100)), (startButton.x+5, startButton.y+5))
                SCREEN.blit(fonts["big"].render('Resume', False, (150, 150, 150)), startButton)
                pygame.display.flip()
        playerSprite = pygame.transform.rotate(pygame.transform.scale(PLAYER_SPRITES[playerSpriteSelect], (64, 64)), -(gravity*5))
        player.y += gravity
        gravity += 0.1
            

        if gravity < -2:
            playerSpriteSelect = "thrust"
        elif gravity < 0:
            playerSpriteSelect = "idle"
            
        if player.y < -10:
            canMove = False
            playerSpriteSelect = "break"
            gravity = 5
            
        if player.y > 510:
            run = False
        
        SCREEN.blit(BACKGROUND, (0, 0))
        for i in cloudTop:
            i.x -= 1
            SCREEN.blit(pygame.transform.scale(CLOUD_SPRITES["top"], (100, 300)), i)
            if i.x == player.x: score += 1
            if player.colliderect(i):
                canMove = False
                playerSpriteSelect = "break"
                gravity = 5
                
        for i in cloudBottom:
            i.x -= 1
            SCREEN.blit(pygame.transform.scale(CLOUD_SPRITES["bottom"], (100, 300)), i)
            if player.colliderect(i):
                canMove = False
                playerSpriteSelect = "break"
                gravity = 5
        
        if cloudTop[(len(cloudTop) - 1)].x < 750:
            cloudTop.append(pygame.Rect(1000, randint(-250, 0), 100, 300))
            cloudBottom.append(pygame.Rect(1000, cloudTop[(len(cloudTop) - 1)].y + 450, 100, 300))
        if cloudTop[0].x < -100:
            cloudTop.pop(0)
            cloudBottom.pop(0)
            
        if cloudBottom[(len(cloudTop) - 1)].x < 750:
            cloudTop.append(pygame.Rect(1000, randint(-300, 0), 100, 300))
        if cloudTop[0].x < -100:
            cloudTop.pop(0)
        
        SCREEN.blit(playerSprite, (player.x - 16, player.y - 20))
        SCREEN.blit(fonts["big"].render(str(score), False, (150, 150, 150)), (10, 10))
        pygame.display.flip()
    
    #highscore saving
        
if __name__ == "__main__":
    main()
pygame.quit()
