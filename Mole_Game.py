import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((800, 600))

pg.display.set_caption("두더지 게임")  
font = pg.font.SysFont('malgungothic', 14)

score = 0
rabbits_pos = [(25, 45), (200, 45), (370, 45), (545, 45), (25, 175), (200, 175), (370, 175), (545, 175), (25, 305),
               (200, 305), (370, 305), (545, 305)]

background_img = pg.image.load('dooduji.webp')
background_img = pg.transform.scale(background_img, (800, 600))
character1_img = pg.image.load('diduda.png')
character1_img = pg.transform.scale(character1_img, (100, 150))

character1_img_pos = character1_img.get_rect()

running = True
while running :

    time_text = font.render(str(pg.time.get_ticks() // 1000) + ' 초', True, (0, 0, 0), None)
    screen.blit(time_text, (680, 55))
    #pg.display.update()
    score_text = font.render(str(score) + '점', True, (0, 0, 0), None)
    screen.blit(score_text, (55, 55))
    #pg.display.update()

    for event in pg.event.get() :
        if event.type == pg.QUIT :
            running = False
        elif event.type == pg.KEYDOWN :
            if event.key == pg.K_LEFT :
                character1_img_pos.x -= 5
            elif event.key == pg.K_RIGHT :
                character1_img_pos.x += 5
            elif event.key == pg.K_UP :
                character1_img_pos.y -= 5
            elif event.key == pg.K_DOWN :
                character1_img_pos.y += 5
        if event.type == pg.MOUSEBUTTONDOWN :
            screen.blit(character1_img, random.choice(character1_img_pos))
        
            pg.display.update()
            pg.time.wait(2000)

                
    
    screen.blit(background_img,background_img.get_rect())
    screen.blit(character1_img, character1_img_pos)
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()