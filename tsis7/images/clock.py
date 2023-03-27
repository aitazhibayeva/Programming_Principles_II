import pygame
import datetime

pygame.init() 
HEIGHT, WIDTH = 600, 800

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Clock')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background = pygame.transform.scale(pygame.image.load('Main.jpeg'), (WIDTH, HEIGHT))

pygame.mixer.music.load('W9_clock_music_sound.mp3')
pygame.mixer.music.play(-1)  
font = pygame.font.SysFont("Times New Roman", 30)

right = pygame.image.load('HourHand.png')
left = pygame.image.load('MinHand.png')

rhand = pygame.transform.scale(pygame.image.load('HourHand.png'), (right.get_width()//1.75, right.get_height()//1.75))
lhand = pygame.transform.scale(pygame.image.load('MinHand.png'), (left.get_width()//1.75, left.get_height()//1.75))


def blit_rotate_center(image, x0, y0, angel):
    rotated_image = pygame.transform.rotate(image, angel)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=(x0, y0)).center)
    screen.blit(rotated_image, new_rect)

running = True
while running:
    clock.tick(60)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second
    
    screen.blit(background, (0, 0))
    text = font.render(f'The time is now: {hour}:{minute}:{second}', True, BLUE)
    blit_rotate_center(rhand, WIDTH // 2 - rhand.get_width()//2, HEIGHT // 2 - rhand.get_height()//2, (-6*minute) - 11)  
    blit_rotate_center(lhand, WIDTH // 2 - lhand.get_width() // 2, HEIGHT // 2 - lhand.get_height() // 2, (-6*second) - 3)  
    screen.blit(text, (250, 550))

    pygame.display.flip()
