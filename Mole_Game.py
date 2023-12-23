import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))

pg.display.set_caption("두더지 게임")

background_img = pg.image.load('dooduji.webp')
background_img = pg.transform.scale(background_img, (800, 600))
character1_img = pg.image.load('diduda.png')
character1_img = pg.transform.scale(character1_img, (130, 150))
font = pg.font.SysFont('malgungothic', 30)

#character1_img_pos = character1_img.get_rect()

running = True
score = 0
character1_img_pos = [(70, 100), (335, 100), (595, 100), (200, 240), (465, 240), 
                      (70, 380), (335, 380), (595, 380)]

check_time = True

while running :

    screen.blit(background_img,background_img.get_rect())

    time_text = font.render(str(pg.time.get_ticks() // 1000) + ' 초', True, (0, 0, 0), None)
    #screen.blit(time_text, (680, 55))
    #pg.display.update()
    score_text = font.render(str(score) + '점', True, (0, 0, 0), None)
    #screen.blit(score_text, (55, 55))
    #pg.display.update()

    for event in pg.event.get() :
        if event.type == pg.QUIT :
            running = False
        # elif event.type == pg.KEYDOWN :
        #     if event.key == pg.K_LEFT :
        #         character1_img_pos.x -= 5
        #     elif event.key == pg.K_RIGHT :
        #         character1_img_pos.x += 5
        #     elif event.key == pg.K_UP :
        #         character1_img_pos.y -= 5
        #     elif event.key == pg.K_DOWN :
        #         character1_img_pos.y += 5
        # if event.type == pg.MOUSEBUTTONDOWN :
        #     screen.blit(character1_img, random.choice(character1_img_pos))
    if(pg.time.get_ticks() // 1000) % 2 == 0 :
        
        if check_time == True :
            check_time = False
            screen .blit(character1_img, random.choice(character1_img_pos))
            pg.display.update()
            pg.time.wait(500)
    else:
        check_time = True
            
        
            # pg.display.update()
            # pg.time.wait(2000)

                
    #screen.blit(character1_img, character1_img_pos)
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()