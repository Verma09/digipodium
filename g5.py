import random 

WIDTH = 500
HEIGHT = 500
MAX_BULLETS = 3

level = 1
lives = 3
score = 0

background = Actor("background")
player = Actor("player", (100,400))
enemies = []
bullets = []
bombs = []

def draw_text():
    screen.draw.text("Level" + str(level), (0,0), color="red")
    screen.draw.text("Score" + str(score), (100,0), color="red")
    screen.draw.text("Lives" + str(lives) (200,0), color="red")
    background.draw
    player.draw
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bombs.draw()
    draw_text()
    
def update (delta):
    move_player()
    move_bullets()
    move_enemies()

def create_bombs():
    if random.randint(0,100 - level * 6) == 0:
        enemy = random.choice(enemies)
        bomb = Actor ("bomb", enemy.pos)
        bombs.append(bomb)
    check_for_end_of_level()
    
def move_bombs():
    global lives
    for bomb in bombs:
        bomb.y = bomb.y + 10
        if bomb.colliderect(player):
            bombs.remove(bomb)
            lives = lives - 1
            if lives == 0:
                exit()
                

def create_enemies():
    for x in range(0, 600, 60):
        for y in range(0, 200, 60):
            enemy = Actor("enemy", (x, y))
            enemy.vx = level * 2
            enemies.append(enemy)
create_enemies()


def move_player():
    if keyboard.right:
        player.x = player.x + 5
    if keyboard.left:
        player.x = player.x - 5
    if player.x > WIDTH:
        player.x = WIDTH
    if player.x < 0:
        player.x = 0
        
        
def move_enemies():
    global score
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration=0.1, y=enemy.y + 60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score = score + 1
        if enemy.colliderect(player):
            exit()
            
def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
       
        
def move_bullets():
    for bullet in bullets:
        bullet.y = bullet.y -6
        if bullet.y < 0:
            bullets.remove(bullet)
            
            

            
            
        
