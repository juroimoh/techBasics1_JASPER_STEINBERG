# Code Review

I will be covering [this repo](https://github.com/codertheashish/Space-Shooter-Game/blob/main/space_shooter_game.py) by **Ashish Kumar Prajapati**.  

The project is a simple space shooter game. You move left and right across the bottom while shooting enemy ships that slowly descend from the top of the screen (see Fig 1), while stars fly by in the background.  

Although the game is fully functional, while playing I encountered some glaring issues:  
- You only lose lives when enemy ships crash into yours, not when they reach the bottom of the screen (like space invaders). After analysing the code it seems this was intentional.  
- You gain score for every shot you take, not every shot you hit, which is completely backwards, especially with infinite ammo. This gives no incentive to attack or do anything. 

![showcase](https://github.com/juroimoh/techBasics1_JASPER_STEINBERG/blob/main/assignments/week11/space_shooter.PNG)  
`Fig 1`

The within the code written by Ashish have been kept. All comments from me are outside the code blocks. Ashish does provide surface level comments, explaining the general application of different functions. 

---

The code begins as follows:  
```
import pygame
import sys
import random

pygame.init()

  # Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Final Version")
```
All necessary libraries are installed, and the screen size is setup with a application title.  

---

```
    # Colors
WHITE = (255, 255, 255)
BLACK = (5, 5, 15)
RED = (255, 60, 60)
GREEN = (0, 220, 120)
BLUE = (80, 160, 255)
YELLOW = (255, 230, 80)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28, bold=True)
big_font = pygame.font.SysFont("Arial", 42, bold=True)

    # Player ship
player_width = 60
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 6

    # Bullets (bigger size)
bullet_width = 8
bullet_height = 20
bullet_speed = 9
bullets = []

    # Enemies
enemy_width = 50
enemy_height = 30
enemy_speed = 1.2    # slow start
enemy_count = 6
enemies = []

    # Score and lives
score = 0    # increases per bullet fired
lives = 5    # game over after 5 touches
```
Here all variables are defined. It seems this game uses almost entirely global variables, which is to be expected.  
Since the colors don't change, they are constants, and therefore uppercase.
Interesting to see is the `player_x` variable, which initially positions the ship in the center of the screen, but since images are displayed from the corner, half of `player_width` is taken away to perfectly center the player ship.

---

```
def create_enemies():
    global enemies
    enemies = []
    for _ in range(enemy_count):
        x = random.randint(0, WIDTH - enemy_width)
        y = random.randint(-400, -40)
        enemies.append([x, y])
```
This creates a list for the enemies to be stored in.  
Random `x` and `y` values are chosen, and appended to the enemies list.  
The `x` value is chosen cleverly to be between `0` and the `WIDTH - enemy_width` to ensure the entire enemy is on screen.  
Then, the `y` value is to seperate the heights of the enemies, so they don't come down in waves, but more randomly.  
The `y` being negative means the enemies are spawned off screen.

---

```
def reset_game():
    global player_x, bullets, score, lives, enemy_speed
    player_x = WIDTH // 2 - player_width // 2
    bullets = []
    score = 0
    lives = 5
    enemy_speed = 1.2
    create_enemies()
```
This function simply resets the game to be replayed.

```
def draw_player():
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, YELLOW, (player_x + player_width//2 - 5, player_y - 8, 10, 8))

def draw_bullets():
    for b in bullets:
        pygame.draw.rect(screen, GREEN, (b[0], b[1], bullet_width, bullet_height))

def draw_enemies():
    for e in enemies:
        pygame.draw.rect(screen, RED, (e[0], e[1], enemy_width, enemy_height))
        pygame.draw.rect(screen, YELLOW, (e[0] + 10, e[1] + 8, 10, 5))
```
These functions draw the different elements, which are later called every frame.  
Where elements are summoned is very efficient.  
`draw_enemies()`, for example, iterates through the list to draw each enemy, and uses each enemies current coordinates for the box that gets drawn.

---

```
def game_over_screen():
    while True:
        screen.fill(BLACK)

        over = big_font.render("GAME OVER!", True, RED)
        score_text = font.render(f"Score: {score}", True, WHITE)
        restart_text = font.render("Press R to Restart", True, BLUE)
        exit_text = font.render("Press ESC to Exit", True, YELLOW)

        screen.blit(over, (WIDTH//2 - over.get_width()//2, 190))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 240))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 300))
        screen.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, 340))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
```
This function runs as a gameloop, where it only runs when the player runs out of lives.  
This renders the text and ability to quit, and stops all other game functions from running since they are not being called.

---

```
    # Start enemies
create_enemies()

# =========================
#        MAIN LOOP
# =========================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Shooting adds score
            if event.key == pygame.K_SPACE:
                score += 1
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y - bullet_height
                bullets.append([bullet_x, bullet_y])
```
This is the main game loop.  
Before anything runs, enemies are already summoned, since the game starts automatically.  
To begin the `while True:` loop, the ability to quit is added, and everytime the `spacebar` is hit, the player score increases, and a bullet is spawned, using a similar mechanic to how enemies spawn.

---

```
            # Movement
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
            player_x -= player_speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < WIDTH - player_width:
            player_x += player_speed
    
            # Move bullets
        for b in bullets:
            b[1] -= bullet_speed
        bullets = [b for b in bullets if b[1] + bullet_height > 0]
    
            # Slowly increase enemy speed
        enemy_speed += 0.0006
```
This section lets the player move, with the `left arrow` or `a` working to move left, vice versa.  
Interesting to note is that `player_speed` is set to `6`, and is never changed.  
When testing the game I also noticed the enemies move very very slightly faster over time (barely noticable), which is confirmed here.  
Turning up `enemy_speed` a tiny bit instantly made the game feel more engaging.

---

```
        # Move enemies and respawn if bottom reached (NO life loss)
    for e in enemies[:]:
        e[1] += enemy_speed
        if e[1] > HEIGHT:
            enemies.remove(e)
            enemies.append([random.randint(0, WIDTH - enemy_width), random.randint(-400, -40)])
```
I had to research what `for e in enemies[:]:` does, but apparently it loops through a copied list.  
Otherwise if `enemies[2]` dies and is removed, then `enemies[3]` turns into `enemies[2]`, and the cycle wouldn't check it (I'm not sure if this is entirely correct).  
Every frame the position of each enemy is updated according to its speed.
When an enemy ship passes below the height of the screen (`e[1]` being the x coordinate) it is removed and another enemy is spawned.  

---

```
        # Bullet hits enemy → enemy disappears
    for b in bullets[:]:
        bx, by = b
        for e in enemies[:]:
            ex, ey = e
            if (bx < ex + enemy_width and
                bx + bullet_width > ex and
                by < ey + enemy_height and
                by + bullet_height > ey):
                bullets.remove(b)
                enemies.remove(e)
                enemies.append([random.randint(0, WIDTH - enemy_width), random.randint(-400, -40)])
                break
```
Here, all bullets are checking if they hit an enemy every frame, again using `[:]`.
When an enemy ship is killed, by checking if the bullet coordinates are within the enemy coordinates, it is removed and another enemy is spawned.  
I'm not sure if this is the most efficient way, but its probably fine for such a small game (see `colliderect()` below).
A huge improvement that I added when testing was the chance of spawning another extra enemy, slowly increasing the amount of enemies over time.  

---

```
        # Player collision → lose life
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for e in enemies[:]:
        enemy_rect = pygame.Rect(e[0], e[1], enemy_width, enemy_height)
        if player_rect.colliderect(enemy_rect):
            lives -= 1
            enemies.remove(e)
            enemies.append([random.randint(0, WIDTH - enemy_width), random.randint(-400, -40)])
```
Here, a built in pygame feature `colliderect()` is used, which checks if the player collides with any incoming enemies.  
I was also planning on using this feature in my game.  
If the player collides, a life is removed and another enemy is spawned once again.

---

```
        # Game over after 5 touches
    if lives <= 0:
        game_over_screen()

        # Draw
    screen.fill(BLACK)

        # Stars background
    for _ in range(20):
        pygame.draw.circle(screen, WHITE, (random.randint(0, WIDTH), random.randint(0, HEIGHT)), 1)
```
A check is run here, seeing if the player has run out of lives.  
If not, then the entire screen is rendered, starting with the background and the stars.  
I might be wrong but I think it would be better to only check if the player has run out of lives everytime one is removed (e.g. adding it to `if player_rect.colliderect(enemy_rect):` from the previous code segment).

---

```
    draw_player()
    draw_bullets()
    draw_enemies()

    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, GREEN)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    pygame.display.update()
    clock.tick(60)
```
Here, the rest of the screen is updated, with the functions to draw the player, bullets and enemies being called.  
The score is also updated live, something I am also planning to do in a similar manner.  
`screen.blit` updates the font in the game window, pasting it in.  
Finally, the screen updates and the fps is limited/set to 60 to ensure smooth gameplay.

---

That is the end of the code
ദ്ദി◝ ⩊ ◜.ᐟ
