import pygame, math
#4kb shmup - William Starkovich

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
player_hitbox_size = 10
player_foc = False

boss_hp = 10
next_wave = False

def target(ox,oy,tv):
    v = pygame.Vector2(tv.x - ox, tv.y - oy).normalize()
    return [v.x, v.y]

wave = 0
enemies = [
    [
        [1500, 250, 0, 2, 0, 1],
        [1500, 750, 0, 2, 0, 1],
    ],
    [
        [1500, 300, 0, 2, 0, 1],
        [1500, 600, 0, 2, 0, 1],
        [1500, 900, 0, 2, 0, 1],
    ],
    [
        [1600, 450, 0, 2, 0, 1],
        [1600, 650, 0, 2, 0, 1],
        [1500, 900, 0, 2, 0, 1],
    ],
]
bullets = []

def fire_bullets(ox, oy, v, depth):
    for d in range(depth):
        bullets.append([ox, oy, v[0] + ((v[0] * 0.1) * d), v[1] + ((v[1] * 0.1) * d), 100])

while True:
    for event in pygame.event.get():
        pass

    screen.fill("black")

    pygame.draw.rect(screen, "blue", (player_pos.x + 36, player_pos.y - 16, 2000, 32))
    pygame.draw.rect(screen, "white", (player_pos.x + 48, player_pos.y - 13, 2000, 26))

    line_y = 36
    if player_foc:
        line_y = 16
        
    pygame.draw.line(screen, "blue", (player_pos.x +40, player_pos.y - line_y), (1920, player_pos.y - line_y), 3)
    pygame.draw.line(screen, "blue", (player_pos.x +40, player_pos.y + line_y), (1920, player_pos.y + line_y), 3)

    pygame.draw.circle(screen, "cyan", player_pos, 24)
    pygame.draw.circle(screen, "blue", player_pos, player_hitbox_size * 0.5)

    if not player_foc:
        line_y = 32

    pygame.draw.circle(screen, "blue", (player_pos.x + 32, player_pos.y - line_y), 16)
    pygame.draw.circle(screen, "white", (player_pos.x + 32, player_pos.y - line_y), 12)

    pygame.draw.circle(screen, "blue", (player_pos.x + 32, player_pos.y + line_y), 16)
    pygame.draw.circle(screen, "white", (player_pos.x + 32, player_pos.y + line_y), 12)

  
    for e in enemies[wave]:
        pygame.draw.circle(screen, "red", (e[0], e[1]), 32)
        e[5] -= dt
        if e[5] <= 0:
            fire_bullets(e[0], e[1], target(e[0],e[1],player_pos), 4)
            e[5] = 1

    if next_wave:
        boss_hp = 10
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

    boss_a = 300
    boss_b = 700
    if player_foc:
        boss_a = 400
        boss_b = 600

    if player_pos.y > boss_a and player_pos.y < boss_b:
        if player_foc:
            boss_hp -= (dt * 1.5)
        else:
            boss_hp -= (dt * 0.5)
        if boss_hp <= 0:
            next_wave = True

    pygame.draw.rect(screen, "red", ((screen.get_width() / 2) - 500, 180,  boss_hp * 100, 32))

    scan_line = True
    for y in range(int(screen.get_height() * 0.5)):
        scan_line = (not scan_line)
        pygame.draw.rect(screen, "black", (0, y * 2, 1920, 1))

    keys = pygame.key.get_pressed()


    spd = 300 * dt
    player_foc = keys[pygame.K_e]

    if player_foc:
        spd = 100 * dt

    if keys[pygame.K_w] and player_pos.y > 0:
        player_pos.y -= spd
    if keys[pygame.K_s] and player_pos.y < 1080:
        player_pos.y += spd
    if keys[pygame.K_a] and player_pos.x > 0:
        player_pos.x -= spd
    if keys[pygame.K_d] and player_pos.x < 1920:
        player_pos.x += spd
    if keys[pygame.K_q]:
        a = c #q = quit

    pygame.display.flip()
    dt = clock.tick(60) / 1000