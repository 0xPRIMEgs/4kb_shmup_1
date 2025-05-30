import pygame
#4kb shmup - William Starkovich

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
player_hitbox_size = 10

wave = 0
enemies = [
    [
        [screen.get_width() / 2, screen.get_height()/2, 0, 2, 0, 1],
        [1500, screen.get_height()/3, 0, 2, 0, 1],
        [1500, 750, 0, 2, 0, 1],
    ],
    [
        [screen.get_width() / 2, 600, 0, 2, 0, 1],
        [500, 300, 0, 2, 0, 1],
        [1200, 900, 0, 2, 0, 1],
    ],
    [
        [screen.get_width() / 2, screen.get_height()/2, 0, 2, 0, 1],
        [1500, screen.get_height()/3, 0, 2, 0, 1],
        [1500, 750, 0, 2, 0, 1],
    ],
]
bullets = []

def fire_bullets(ox, oy, vx, vy, depth):
    for d in range(depth):
        bullets.append([ox, oy, vx + (d * 0.1), vy, 100])

while True:
    for event in pygame.event.get():
        pass

    screen.fill("black")

    pygame.draw.rect(screen, "blue", (player_pos.x + 36, player_pos.y - 16, 2000, 32))
    pygame.draw.rect(screen, "white", (player_pos.x + 48, player_pos.y - 13, 2000, 26))

    pygame.draw.line(screen, "blue", (player_pos.x -8, player_pos.y - 36), (1920, player_pos.y - 36), 3)
    pygame.draw.line(screen, "blue", (player_pos.x -8, player_pos.y + 36), (1920, player_pos.y + 36), 3)

    pygame.draw.circle(screen, "cyan", player_pos, 24)
    pygame.draw.circle(screen, "blue", player_pos, player_hitbox_size * 0.5)

    pygame.draw.circle(screen, "blue", (player_pos.x - 32, player_pos.y - 32), 16)
    pygame.draw.circle(screen, "white", (player_pos.x - 32, player_pos.y - 32), 12)

    pygame.draw.circle(screen, "blue", (player_pos.x - 32, player_pos.y + 32), 16)
    pygame.draw.circle(screen, "white", (player_pos.x - 32, player_pos.y + 32), 12)

    next_wave = True
    for e in enemies[wave]:
        if e[3] > 0:

            if e[2] == 0:
                e[1] -= 0.1
            elif e[2] == 1:
                e[1] += 0.1

            next_wave = False
            if e[0] >= player_pos.x + 32 and e[1] >= player_pos.y - 16 and e[1] <= player_pos.y + 16:
                e[3] -= dt

            pygame.draw.circle(screen, "red", (e[0], e[1]), 32)
            e[5] -= dt
            if e[5] <= 0:
                if e[2] == 0:
                    e[2] == 1
                elif e[2] == 1:
                    e[2] == 0
                fire_bullets(e[0], e[1], -1, -0.1, 4)
                fire_bullets(e[0], e[1], -1, 0, 4)
                fire_bullets(e[0], e[1], -1, 0.1, 4)
                e[5] = 1

    if next_wave:
        next_wave = False
        wave += 1
        if wave > 2:
            a = c #win

    for b in bullets:
        if b[4] > 0:
            b[0] += b[2]
            b[1] += b[3]
            b[4] -= dt

            if b[0] >= player_pos.x - player_hitbox_size and b[0] <= player_pos.x + player_hitbox_size and b[1] >= player_pos.y - player_hitbox_size and b[1] <= player_pos.y + player_hitbox_size:
                a = c #you died

            pygame.draw.circle(screen, "green", (b[0], b[1]), 8)
            pygame.draw.circle(screen, "white", (b[0], b[1]), 5)

    scan_line = True
    for y in range(int(screen.get_height() * 0.5)):
        scan_line = (not scan_line)
        pygame.draw.rect(screen, "black", (0, y * 2, 1920, 1))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        if player_pos.y <= 0:
            player_pos.y = 0
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        if player_pos.y > 1080:
            player_pos.y = 1080
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        if player_pos.x <= 0:
            player_pos.x = 0
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        if player_pos.x > 1920:
            player_pos.x = 1920
    if keys[pygame.K_q]:
        a = c #q = quit

    pygame.display.flip()
    dt = clock.tick(60) / 1000