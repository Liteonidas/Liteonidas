import pygame as pg
import pygame.time
import time

pg.init()
window = pg.display.set_mode((800, 600))
pygame.display.set_caption('Maszyna losująca')
img = pg.image.load("bartek.jpg")

x = 300
y = 250
button = pg.rect.Rect(x, y, 200, 100)
# IMG_SIZE = (1536, 1536)
IMG_SIZE = (400, 400)

image = pg.transform.scale(img, IMG_SIZE)


def print_text(text: str, osx, osy, font_large):
    font = pg.font.Font("freesansbold.ttf", font_large)
    text_obj = font.render(text, True, (0, 0, 0))
    window.blit(text_obj, (osx, osy))


def counting_down(counter=5):
    while counter > 0:
        window.fill((24, 164, 240))
        print_text(str(counter), 400, 290, 30)
        pg.display.update()
        time.sleep(1)
        counter -= 1


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
            counting_down()
            fake_time = False
        print_text("W losowaniu zwyciężył:", 290, 30, 20)
        print_text("BARTEK", 295, 60, 50)
        window.blit(image, (200, 120))
    else:
        pg.draw.rect(window, (20, 200, 20), button)
        print_text("Losuj", 360, 285, 30)

    pg.display.update()
