import pygame
import math
import mymath
import mic

# pygame setup
pygame.init()
pygame.font.init()
pygame.display.set_caption("9c")

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
FPS = 30
angle = 0
frame = 0
speed = 1
offset = 35

NORMAL_FONT = pygame.font.SysFont("JetBrainsMonoNerdFont-Regular.ttf", 20)
TALKING_FONT = pygame.font.SysFont("JetBrainsMonoNerdFont-Regular.ttf", 25)

text_surfaces = [NORMAL_FONT.render("C", True, (255, 255, 255)), TALKING_FONT.render("O", True, (255, 255, 255))]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    angle -= 2*math.pi if angle > 2*math.pi else 0
    angle += 2*speed/FPS if mic.talking_frames>0 else speed/FPS
    for point in mymath.points:
        pygame_point = mymath.project(point, WIDTH, HEIGHT, angle)
        screen.blit(text_surfaces[1 if mic.talking_frames>0 else 0], pygame_point)
    if mic.talking_frames>0:
        pygame.draw.circle(screen, (255, 255, 255), (195-offset, 190+4*math.sin(frame*speed/FPS)), 30, 5)
        pygame.draw.circle(screen, (255, 255, 255), (190-offset, 185+4*math.sin(frame*speed/FPS)), 18)
        pygame.draw.circle(screen, (255, 255, 255), (195+offset, 200+4*math.sin(frame*speed/FPS)), 30, 5)
        pygame.draw.circle(screen, (255, 255, 255), (190+offset, 195+4*math.sin(frame*speed/FPS)), 18)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (205-offset, 200+4*math.sin(frame*speed/FPS)), 30, 5)
        pygame.draw.circle(screen, (255, 255, 255), (205-offset, 200+4*math.sin(frame*speed/FPS)), 18)
        pygame.draw.circle(screen, (255, 255, 255), (205+offset, 210+4*math.sin(frame*speed/FPS)), 30, 5)
        pygame.draw.circle(screen, (255, 255, 255), (205+offset, 210+4*math.sin(frame*speed/FPS)), 18)
    # screen.blit(text_surfaces[2], (180, 180))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    mic.talking_frames -= 1 if mic.talking_frames>0 else 0
    frame += 1

    clock.tick(30)

pygame.quit()
