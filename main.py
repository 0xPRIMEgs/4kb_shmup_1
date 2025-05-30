import pygame, math
from tiny_shmup import tiny_shmup
#4kb shmup - William Starkovich

pygame.init()
tiny_shmup = tiny_shmup()

screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
player_hitbox_size = 10
player_foc = False

boss_hp = 10
next_wave = False



wave = 0
enemies = [
    [
        [1500, 250, 1, 2, 0, 1],
        [1500, 500, 0, 2, 0, 1],
        [1500, 750, 1, 2, 0, 1],
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
        bullets.append([ox, oy, v[0] + ((v[0] * 0.1) * d), v[1] + ((v[1] * 0.1) * d), 100,0])

def fire_bullet(ox, oy, v):
    bullets.append([ox, oy, v[0], v[1], 100,1])

while True:
    for event in pygame.event.get():
        pass

    screen.fill("black")

    tiny_shmup.draw_beam(screen, "blue", (player_pos.x + 36, player_pos.y), 32, 6)
    
    line_y = 36
    if player_foc:
        line_y = 16

    tiny_shmup.draw_beam(screen, "blue",  (player_pos.x +40, player_pos.y - line_y), 16, 6)
    tiny_shmup.draw_beam(screen, "blue",  (player_pos.x +40, player_pos.y + line_y), 16, 6)
    

    tiny_shmup.draw_player(screen, "cyan", player_pos, 64)
    
    if not player_foc:
        line_y = 32

    tiny_shmup.draw_bit(screen, "cyan", (player_pos.x + 32, player_pos.y - line_y), 32)
    tiny_shmup.draw_bit(screen, "cyan", (player_pos.x + 32, player_pos.y + line_y), 32)
  
    for e in enemies[wave]:
        tiny_shmup.draw_enemy(screen, "red", (e[0], e[1]), 32)
        e[5] -= dt
        if e[5] <= 0:
            if e[2] == 0: 
                fire_bullets(e[0], e[1], tiny_shmup.towards((e[0],e[1]),(player_pos.x, player_pos.y)), 4)
                e[5] = 3
            elif e[2] == 1:
                fire_bullet(e[0], e[1], tiny_shmup.towards((e[0],e[1]),(player_pos.x, player_pos.y)))
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

            bc = "pink"
            if(b[5] == 0):
                bc = "green"
            tiny_shmup.draw_bullet(screen, bc, (b[0], b[1]), 8)

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