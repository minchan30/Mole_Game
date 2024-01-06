import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800, 600))

pg.display.set_caption("두더지 게임")

bg_img = pg.image.load("background.png")
bg_img = pg.transform.scale(bg_img, (800, 600))
charic_img = pg.image.load("character.png")
charic_img = pg.transform.scale(charic_img, (130, 150))
hammer_img = pg.image.load("hammer.png")
hammer_img = pg.transform.scale(hammer_img, (80, 80))
success_img = pg.image.load('success.png')
success_img = pg.transform.scale(success_img, (800, 600))
fail_img = pg.image.load('fail.png')
fail_img = pg.transform.scale(fail_img, (800, 600))

font = pg.font.SysFont('malgungothic', 30)

charics_pos = [(70, 100), (335, 100), (595, 100), (200, 240), (465, 240), 
                      (70, 380), (335, 380), (595, 380)]

running = True
check_time = True

limit_time = 30
target_score = 10
score = 0
random_time_list = [1, 2, 3]
charics = []
pg.mouse.set_visible(False)


start_time = pg.time.get_ticks()
random_time = random.choice(random_time_list)
minute = 0
current_time = None


while running:
    
    screen.blit(bg_img, bg_img.get_rect())
    
    time_text = font.render(str(pg.time.get_ticks() // 1000) + "   초", True, (0, 0, 0), None)
    score_text = font.render(str(score) + "   점", True, (0, 0, 0), None)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            for charic in charics:
                if charic.collidepoint(event.pos):
                    charics.remove(charic)
                    score += 1
                    break
    
    current_time = (pg.time.get_ticks() - start_time) // 1000

    if current_time == minute :
        minute += 1
        random_time -= 1
        if random_time <= 0 :
            random_time = random.choice(random_time_list)
            check_time = True

    if check_time:
        add_charic = screen.blit(charic_img, random.choice(charics_pos))
        charics.append(add_charic)
        check_time = False 

        if not charics :
            add_rabbit = screen.blit(charic_img, random.choice(charics_pos))
            charics.append(add_charic)

    for charic in charics:
        screen.blit(charic_img, charic)
    
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))
    screen.blit(hammer_img, pg.mouse.get_pos())
    
    if pg.time.get_ticks() // 1000 >= limit_time:
        if score >= target_score:
            screen.blit(success_img, (0, 0))
        else:
            screen.blit(fail_img, (0, 0))
        
        pg.display.update()
        pg.time.wait(3000)
        break
    
    pg.display.update()


pg.quit()