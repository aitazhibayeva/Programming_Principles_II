import pygame as pg
import random
# Initializing 
pg.init()
# Display 
screen = pg.display.set_mode((1000, 800))
clock = pg.time.Clock()
menue = pg.Surface((200, 800))
menue.fill('skyblue')
# Variables ------------------------------------------------------------------------------------------------------------
p_f = 1
f = 1
c = 'black' # Instead of (x, x, x) we can use named color
d = 2
running = True

class Button(pg.sprite.Sprite):
  # Buttons ------------------------------------------------------------------------------------------------------------
  def __init__(self, flag, img, x, y):
    pg.sprite.Sprite.__init__(self)
    self.flag = flag
    if flag == 0:
      self.img = pg.Surface((70, 70)) 
      self.c = img
      self.img.fill(self.c)
    elif self.flag == 2:
      self.img = pg.Surface((70, 70))
      self.img.fill((255, 255, 255))
      pg.draw.rect(self.img, (0, 0, 0), (15, 15, 40, 40), 2)
    elif self.flag == 3:
      self.img = pg.Surface((70, 70))
      self.img.fill((255, 255, 255))
      pg.draw.circle(self.img, (0, 0, 0), (35, 35), 20, 2)
    else:
      self.img = pg.image.load('tsis8\img')
    self.rect = self.img.get_rect()
    self.rect.x = x
    self.rect.y = y

  def draw(self):
      screen.blit(self.img, self.rect)

  def check(self, p):
    if self.rect.left < p[0] < self.rect.right and self.rect.top < p[1] < self.rect.bottom:
      return True
    else:
       return False

  def change(self):
    if self.flag == 0:
      self.c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      self.img.fill(self.c) 
# Loading images of buttons --------------------------------------------------------------------------------------------
pencil = Button(1, "tsis8\img\pencil.png", 820, 50)
eraser = Button(1, "tsis8\img\eraser.png", 910, 50)
randomizer = Button(4, 'tsis8\img\rand.png', 820, 160)
rec = Button(2, None, 820, 280)
cir = Button(3, None, 910, 280)

buttons = pg.sprite.Group()
# Adding random colors -------------------------------------------------------------------------------------------------
for i in range(0, 10, 2):
  buttons.add(Button(0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 820, 390 + i/2*110))
  buttons.add(Button(0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 910, 390 + i/2*110))

buttons.add(cir)
buttons.add(rec)
buttons.add(pencil)
buttons.add(eraser)
buttons.add(randomizer)

prev, cur = None, None
screen.fill('white')

while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
    if event.type == pg.MOUSEBUTTONDOWN:
      prev = pg.mouse.get_pos()
      if 799 < prev[0] < 1001:
        for o in buttons:
          if o.check(prev):
            f = o.flag
            if f == 0:
              f = p_f
              c = o.c
            elif f == 1:
              p_f = 1
              d = 2
              if o == eraser:
                d = 30
                c = 'white'
            elif f == 2:
              p_f = f      
            elif f == 3:
              p_f = f
            elif f == 4:
              for i in buttons:
                i.change()
            break
    # Drawing figures with coordinates ---------------------------------------------------------------------------------
    if f == 1:
      if event.type == pg.MOUSEMOTION:
        cur = pg.mouse.get_pos()
        if prev:     
          pg.draw.line(screen, c, prev, cur, d)
          prev = cur
      if event.type == pg.MOUSEBUTTONUP:
        prev = None
    elif f == 2:
      if event.type == pg.MOUSEBUTTONUP:
        cur = pg.mouse.get_pos()
        if prev:     
          pg.draw.rect(screen, c, (min(prev[0], cur[0]), min(prev[1], cur[1]), abs(prev[0] - cur[0]), abs(prev[1] - cur[1])), 2)
          prev = cur
    elif f == 3:
      if event.type == pg.MOUSEBUTTONUP:
        cur = pg.mouse.get_pos()
        if prev:     
          pg.draw.circle(screen, c, (min(prev[0], cur[0]) + abs(prev[0] - cur[0])//2, min(prev[1], cur[1]) + abs(prev[1] - cur[1])//2), abs(prev[0] - cur[0])//2, 2)
          prev = cur

  screen.blit(menue, (800, 0))
  for o in buttons:
    o.draw()
  pg.display.flip()

  clock.tick(300)


pg.quit()