import pygame as pg

pg.init()

screen = pg.display.set_mode((600,600))
pg.display.set_caption("나만의 캐릭터 움직이기 게임")

running = True


background_img = pg.image.load('dooduji.webp')
background_img = pg.transform.scale(background_img, (600, 600))
character1_img = pg.image.load('doduji.png')
character1_img = pg.transform.scale(character1_img, (75, 100))
character2_img = pg.image.load('hamor.webp')
character2_img = pg.transform.scale(character2_img, (75, 100))

character1_img_pos = character1_img.get_rect()
character2_img_pos = character2_img.get_rect()

while running:
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
    screen.blit(character2_img, character2_img_pos)

    pg.display.update()

pg.quit()