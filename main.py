import pygame

pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
Car = pygame.image.load('tesla.png')
Car = pygame.transform.scale(Car, (30, 60))
Car_x = 155
Car_y = 300
cam_x_offset = 0
cam_y_offset = 0
focal_dist = 25
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    #  detect road
    cam_x = Car_x + cam_x_offset + 15
    cam_y = Car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dist))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dist))[0]
    right_px = window.get_at((cam_x + focal_dist, cam_y))[0]
    print(up_px, right_px, down_px)
    # take turn or change direction
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        Car = pygame.transform.rotate(Car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        Car_x = Car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        Car = pygame.transform.rotate(Car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        Car_y = Car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        Car = pygame.transform.rotate(Car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:

        direction = 'up'
        Car_x = Car_x + 30
        cam_x_offset = 0
        Car = pygame.transform.rotate(Car, 90)

    # drive
    elif direction == 'up' and up_px == 255:
        Car_y = Car_y - 2
    elif direction == 'right' and right_px == 255:
        Car_x = Car_x + 2
    elif direction == 'down' and down_px == 255:
        Car_y = Car_y + 2
    window.blit(track, (0, 0))
    window.blit(Car, (Car_x, Car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
