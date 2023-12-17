import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))

pg.display.set_caption("두더지 게임")
font = pg.font.SysFont('numberuungothic', 30)

score = 0

background_img = pg.image.load('dooduji.webp')
background_img = pg.transform.scale(background_img, (800, 600))
character1_img = pg.image.load('doduji-removebg-preview.png')
character1_img = pg.transform.scale(character1_img, (75, 100))

character1_img_pos = character1_img.get_rect()

running = True
while running:

    time_text = font.render(str(pg.time.get_ticks() // 1000) + ' 초', True, (0, 0, 0), None)
    screen.blit(time_text, (680, 55))
    pg.display.update()
    score_text = font.render(str(score) + '점', True, (0, 0, 0), None)
    screen.blit(score_text, (55, 55))
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                character1_img_pos.x -= 5
            elif event.key == pg.K_RIGHT:
                character1_img_pos.x += 5
            elif event.key == pg.K_UP:
                character1_img_pos.y -= 5
            elif event.key == pg.K_DOWN:
                character1_img_pos.y += 5

                
    
    screen.blit(background_img,background_img.get_rect())
    screen.blit(character1_img, character1_img_pos)
    screen.blit(time_text, (680, 55))
    screen.blit(score_text, (55, 55))

    pg.display.update()

pg.quit()