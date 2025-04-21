import psycopg2
import pygame
import random
import sys
from datetime import datetime

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="iskanderb4",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    last_updated TIMESTAMP DEFAULT NOW()
)
""")
conn.commit()

def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def get_user_progress(user_id):
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    if result:
        return result[0], result[1]
    else:
        cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        return 0, 1

def save_progress(user_id, score, level):
    cur.execute("""
        UPDATE user_score SET score = %s, level = %s, last_updated = %s
        WHERE user_id = %s
    """, (score, level, datetime.now(), user_id))
    conn.commit()

# game as it is
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game with postgreSQL")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# user
username = input("enter username: ")
user_id = get_or_create_user(username)
score, level = get_user_progress(user_id)
print(f"welcome {username}. level: {level}, score: {score}")

# logic
snake = [(5, 5)]
direction = (1, 0)
food = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

def generate_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))
        if pos not in snake and pos not in walls:
            return pos

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def draw_walls(level):
    wall_blocks = set()
    if level >= 2:
        for x in range(5, 15):
            wall_blocks.add((x, 10))
    if level >= 3:
        for y in range(15, 20):
            wall_blocks.add((20, y))
    return wall_blocks

walls = draw_walls(level)

paused = False
running = True
move_timer = 0
move_delay = max(100 - level * 10, 40)  # speed +++++

# game loop
while running:
    dt = clock.tick(60)
    move_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress(user_id, score, level)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("paused. press P to resume.")
                    save_progress(user_id, score, level)
            elif not paused:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

    if not paused and move_timer > move_delay:
        move_timer = 0
        head_x, head_y = snake[-1]
        new_head = (head_x + direction[0], head_y + direction[1])

        # checking
        if (
            new_head in snake or
            new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
            new_head in walls
        ):
            print("game over!!! saving progress...")
            save_progress(user_id, score, level)
            pygame.time.delay(2000)
            running = False
            break

        snake.append(new_head)

        if new_head == food:
            score += 10
            if score >= level * 50:
                level += 1
                print(f"level Up! now level {level}")
                walls = draw_walls(level)
                move_delay = max(100 - level * 10, 40)
            food = generate_food()
        else:
            snake.pop(0)

    # renderring
    screen.fill((0, 0, 0))
    draw_grid()

    # snake ex
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # food
    pygame.draw.rect(screen, (255, 0, 0), (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # walls
    for wall in walls:
        pygame.draw.rect(screen, (128, 128, 128), (wall[0]*CELL_SIZE, wall[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # ui
    score_text = font.render(f"score: {score}", True, (255, 255, 255))
    level_text = font.render(f"level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    if paused:
        pause_text = font.render("PAUSED", True, (255, 255, 0))
        screen.blit(pause_text, (WIDTH//2 - 60, HEIGHT//2 - 20))

    pygame.display.flip()

pygame.quit()
cur.close()
conn.close()
