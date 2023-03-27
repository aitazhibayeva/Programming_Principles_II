import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
background = pygame.transform.scale(pygame.image.load('mixkit-headphones-.png'), (WIDTH, HEIGHT))
sound = [
    pygame.mixer.Sound("NewJeans - OMG.mp3"),
    pygame.mixer.Sound("BTS - Dynamite.mp3"),
    pygame.mixer.Sound("Justin Bieber ft. Ludacris — Baby.mp3")
]
sound_name = [
    "NewJeans - OMG",
    "BTS - Dynamite",
    "Justin Bieber - Baby"
]
sound_cnt = 0

myfont = pygame.font.SysFont("comicsansms", 30)

playmusic = myfont.render("Press Space to play music", True, (0, 0, 0))
nextmusic = myfont.render("Press C to play next music", True, (0, 0, 0))
stopmusic = myfont.render("Press Z to stop music", True, (0, 0, 0))
previousmusic = myfont.render("Press X to play previous music", True, (0, 0, 0))


musis_on = False

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(playmusic, (50, 0))
    screen.blit(nextmusic, (50, 100))
    screen.blit(stopmusic, (50, 200))
    screen.blit(previousmusic, (50, 300))
    screen.blit(myfont.render(f"Music name : {sound_name[sound_cnt]}", True, (0, 0, 0)), (50, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not musis_on:
                musis_on = True
                sound[sound_cnt].play()
            elif event.key == pygame.K_c:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt += 1
                if sound_cnt >= len(sound):
                    sound_cnt = 0
                sound[sound_cnt].play()
            elif event.key == pygame.K_z:
                musis_on = False
                sound[sound_cnt].stop()
            elif event.key == pygame.K_x:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt -= 1
                if sound_cnt < 0:
                    sound_cnt = len(sound) - 1
                sound[sound_cnt].play()

    pygame.display.flip()