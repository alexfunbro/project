import pygame
import os
import math
import datetime

pygame.init()
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert()
        image.set_colorkey((255, 255, 255))
        _image_library[path] = image
    return image

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock_face = get_image("mikey.png")
mickey_right_hand = get_image("onkool.png")
mickey_left_hand = get_image("photosolkolulken.png")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    
    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)
    
    rotated_minute_hand = pygame.transform.rotate(mickey_right_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(mickey_left_hand, second_angle)
    
    min_hand_rect = rotated_minute_hand.get_rect(center=CENTER)
    sec_hand_rect = rotated_second_hand.get_rect(center=CENTER)
    
    screen.fill((255, 255, 255)) 
    screen.blit(clock_face, (53, 95))
    screen.blit(rotated_minute_hand, min_hand_rect.topleft) 
    screen.blit(rotated_second_hand, sec_hand_rect.topleft) 
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()