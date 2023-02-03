import pygame as pg
import pygame.time
import time

pg.init()
window = pg.display.set_mode((800, 600))

x = 300
y = 250
button = pg.rect.Rect(x, y, 200, 100)


def print_text(text: str, osx, osy, font_large):
    font = pg.font.Font("freesansbold.ttf", font_large)
    text_obj = font.render(text, True, (0, 0, 0))
    window.blit(text_obj, (osx, osy))


def refresh():
    # window.fill((24, 164, 240))
    pg.display.update()


print_flag = False
fake_time = True

run = True
while run:
    pygame.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONUP:
            print_flag = True
    window.fill((24, 164, 240))

    if print_flag:
        if fake_time:
            print_text("5", 370, 290, 30)
            pg.display.update()
            time.sleep(1)
            window.fill((24, 164, 240))
            print_text("4", 370, 290, 30)
            pg.display.update()
            time.sleep(1)
            window.fill((24, 164, 240))
            print_text("3", 370, 290, 30)
            pg.display.update()
            time.sleep(1)
            window.fill((24, 164, 240))
            print_text("2", 370, 290, 30)
            pg.display.update()
            time.sleep(1)
            window.fill((24, 164, 240))
            print_text("1", 370, 290, 30)
            pg.display.update()
            time.sleep(1)

            fake_time = False
        print_text("W losowaniu zwyciężył:", 290, 100, 20)
        print_text("BARTEK", 295, 160, 50)
    else:
        pg.draw.rect(window, (20, 200, 20), button)
        print_text("Losuj", 360, 285, 30)

    pg.display.update()
