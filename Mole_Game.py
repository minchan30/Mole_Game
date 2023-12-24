import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))

pg.display.set_caption("두더지 게임")

bg_img = pg.image.load('dooduji.webp')
bg_img = pg.transform.scale(bg_img, (800, 600))
charic_img = pg.image.load('diduda.png')
charic_img = pg.transform.scale(charic_img, (130, 150))
font = pg.font.SysFont('malgungothic', 30)

charics_pos = [(70, 100), (335, 100), (595, 100), (200, 240), (465, 240), 
                      (70, 380), (335, 380), (595, 380)]
#character1_img_pos = character1_img.get_rect()

running = True
score = 0
check_time = True
charics = []
while running :

    screen.blit(bg_img, bg_img.get_rect())

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
        if event.type == pg.MOUSEBUTTONDOWN :
            for charic in charics :
                if charic in charics :
                    if charic.collidepoint(event.pos) :
                        score += 1
                        charics.remove(charic)
                        break
                
        #     screen.blit(character1_img, random.choice(character1_img_pos))
    if(pg.time.get_ticks() // 1000) % 2 == 0 :
        if check_time :
            add_charic = screen.blit(charic_img, random.choice(charics_pos))
            charics.append(add_charic)

            check_time = False

        # if check_time == True :
    
        #     screen .blit(character1_img, random.choice(character1_img_pos))
        #     pg.display.update()
        #     pg.time.wait(500)
    else:
        check_time = True
            
    for charic in charics :
        screen.blit(charic_img, charic)
        
            # pg.display.update()
            # pg.time.wait(2000)

                
    #screen.blit(character1_img, character1_img_pos)
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()