# AS A CLASS ASSIGNMENT, I GAVE CHATGPT THE CONCEPT OF WHAT I WAS DOING WITH YUP AND IT MADE A GAME.
# IT SUCKS.


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the FPS and create a clock
FPS = 60
clock = pygame.time.Clock()

# Create the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))  # Player is smaller
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 30))
        self.bullet_limit = 3  # Maximum number of bullets on screen
        self.bullets = pygame.sprite.Group()
        self.bullets_timer = 0 #a timer to limit how often the player can shoot
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        # Limit the player's movement within the screen
        self.rect.x = max(0, min(self.rect.x, screen_width - 15))
        #shooting
        self.shoot()
    
    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bullets_timer += 1
            if len(self.bullets) < self.bullet_limit and self.bullets_timer%5==0:  # Check if the number of bullets on screen is less than the limit
                bullet = Bullet(self.rect.centerx, self.rect.top, GREEN)
                all_sprites.add(bullet)
                player_bullets.add(bullet)
                self.bullets.add(bullet)

# Create the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Enemies are larger
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.x_speed = 1  # Slower left and right movement
        self.y_speed = 3  # Faster downward movement
        self.shoot_delay = 3000  # Delay before the enemy can shoot (in milliseconds)
        self.last_shot = pygame.time.get_ticks()  # Time of the last shot
        self.next_shoot_time = random.randint(2000, 5000)  # Initial next shoot time

    def update(self):
        self.rect.x += self.x_speed
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.x_speed = -self.x_speed
            self.rect.y += self.y_speed  # Faster downward movement
        self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.next_shoot_time:
            self.last_shot = now
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, RED)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)
            self.next_shoot_time = random.randint(2000, 5000)  # Randomize the next shoot time

# Main game loop
running = True

# Create the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

# Create the EnemyBullet class
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Same size as regular bullets
        self.image.fill(RED)  # Enemy bullets are red
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += 5
        if self.rect.top > screen_height:
            self.kill()

# Create the player, enemies, and bullets groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Create enemies in a formation at the top of the screen
enemy_rows = 5
enemy_cols = 10
enemy_spacing = 50
for row in range(enemy_rows):
    for col in range(enemy_cols):
        enemy = Enemy(100 + col * enemy_spacing, 50 + row * enemy_spacing)
        all_sprites.add(enemy)
        enemies.add(enemy)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top, GREEN)
            all_sprites.add(bullet)
            player_bullets.add(bullet)
    
    all_sprites.update()
    
    # Enemy bullet collision with player
    if pygame.sprite.spritecollide(player, enemy_bullets, True):
        # Player is hit by an enemy bullet
        running = False

    # Collision detection
    for bullet in player_bullets:
        hits = pygame.sprite.spritecollide(bullet, enemies, True)
        for hit in hits:
            bullet.kill()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()