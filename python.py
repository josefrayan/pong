import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("0-0")

player1goals = 0
player2goals = 0

ballpos_x = 1280/2
ballpos_y = 720/2

playerpos1_x = 40
playerpos1_y = 720/2
playerpos2_x = 1240
playerpos2_y = 720/2

a = random.choice([-1,1])
b = random.choice([-1,1])

bewegung_x = 6 * b
bewegung_y = 6  * a
 
spielaktiv = True
while spielaktiv:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spiel beendet")
    
    ballpos_x += bewegung_x
    ballpos_y += bewegung_y
    if ballpos_y-20 <= 0:
        bewegung_y *= -1
    if ballpos_y+20 >= 720:
        bewegung_y *= -1
    


    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerpos1_y -=4
    if keys[pygame.K_s]:
        playerpos1_y +=4
    if keys[pygame.K_UP]:
        playerpos2_y -=4
    if keys[pygame.K_DOWN]:
        playerpos2_y +=4
      

    screen.fill((100,100,100))
    ball = pygame.draw.circle(screen,(255,140,0),[ballpos_x,ballpos_y],20)
    player1 = pygame.draw.line(screen,(255,0,0),[playerpos1_x,playerpos1_y+50],[playerpos1_x,playerpos1_y-50],10)
    player2 =pygame.draw.line(screen,(255,0,0),[playerpos2_x,playerpos2_y+50],[playerpos2_x,playerpos2_y-50],10)
    tor1 = pygame.draw.line(screen,(0,0,0),[10,0],[10,720],2)
    tor2 = pygame.draw.line(screen,(0,0,0),[1270,0],[1270,720],2)


    if ball.colliderect(tor1):
        ballpos_x = 1280/2
        ballpos_y = 720/2
        player2goals += 1
    if ball.colliderect(tor2):
        ballpos_x = 1280/2
        ballpos_y = 720/2
        player1goals += 1
    if ball.colliderect(player1):
        bewegung_x *= -1
    if ball.colliderect(player2):
        bewegung_x *= -1
    pygame.display.set_caption(str(player1goals) + " : " + str(player2goals))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()