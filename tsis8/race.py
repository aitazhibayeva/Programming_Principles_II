import random
import pygame as pg
# Initializing 
pg.init()
# Screen 
WIDTH = 400
HEIGHT = 600
SURF = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Street Racer")
# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pg.time.Clock()
# Background 
bg = pg.image.load("tsis8\image\AnimatedStreet.png")
# Font 
score_font = pg.font.SysFont("Roboto-Bold .ttf", 50, True, True)
big_font = pg.font.SysFont("Roboto-Bold .ttf", 70, True, False)
rest_font = pg.font.SysFont("Roboto-Bold .ttf", 50, False, False)
restart = rest_font.render("Press R to restart", True, BLACK)
game_over = big_font.render("GAME OVER", True, BLACK)
# Variables 
paused = False
STEP = 5
# Classes 

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("tsis8\image\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pg.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < WIDTH:
            if pressed_keys[pg.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("tsis8\image\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def update(self):
        self.rect.move_ip(0, STEP)
        if self.rect.top > HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("tsis8\image\coin.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), -200)

    def update(self):
        self.rect.move_ip(0, STEP)
        if self.rect.top > HEIGHT:
            self.bottom = -200
            self.rect.center = (random.randint(40, WIDTH - 40), -200)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def fgame_over():
    global paused
    while paused:
        clock.tick(5)
        SURF.fill(RED)
        SURF.blit(game_over, (30, 250))
        SURF.blit(restart, (55, 300))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    global STEP
                    global SCORE
                    STEP = 5
                    SCORE = 0
                    paused = False
                    main()
                elif event.key == pg.K_q:
                    pg.quit()
                    quit()


def main():
    # # Variables 
    global STEP
    STEP = 5
    SCORE = 0
    # Sprites 
    P1 = Player()
    E1 = Enemy()
    C1 = Coin()
    # Groups 
    enemies = pg.sprite.Group()
    coins = pg.sprite.Group()
    enemies.add(E1)
    coins.add(C1)

    # Music 
    pg.mixer.music.load("tsis8\sound\W10_street racer_sound_background.wav")
    pg.mixer.music.play(-1)
    running = True
    # Adding a new User event 
    INC_SPEED = pg.USEREVENT + 1
    pg.time.set_timer(INC_SPEED, 1000)
    # Game Loop
    while running:
        clock.tick(60)
        # Quit and increasing speed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == INC_SPEED:
                STEP += 0.3
        # Updating 
        P1.update()
        for enemy in enemies:
            enemy.update()
        C1.update()
        # Collision 
        if pg.sprite.spritecollideany(P1, enemies):
            pg.mixer.music.pause()
            pg.mixer.Sound("tsis8\sound\W10_street racer_sound_crash.wav").play()
            global paused
            paused = True
            fgame_over()
            for enemy in enemies:
                enemy.kill()
        if pg.sprite.spritecollideany(P1, coins):
            SCORE += 1
            pg.mixer.Sound("tsis8\sound\W10_street racer_sound_coin.wav").play()
            # Deleting and adding New Coin 
            for c in coins:
                c.kill()
            C1 = Coin()
            coins.add(C1)
        SURF.blit(bg, (0, 0))
        # Drawing 
        for enemy in enemies:
            enemy.draw(SURF)
        P1.draw(SURF)
        C1.draw(SURF)
        score_img = score_font.render(str(SCORE), True, BLACK)
        SURF.blit(score_img, (10, 10))

        # New Car, New Level 
        if SCORE == 10 and len(enemies) < 2:
            E = Enemy()
            enemies.add(E)
        pg.display.update()
    pg.quit()
    exit()


main()