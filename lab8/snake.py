import pygame, sys, random
from pygame.locals import *

pygame.init()

# частота кадров
FPS = 10
FramePerSec = pygame.time.Clock()

# определяем цвета
WHITE = (255, 255, 255)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (34, 139, 34)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# устанавливаем размеры экрана
SCREEN_WIDTH = 600  # изменённая ширина
SCREEN_HEIGHT = 500  # изменённая высота
SPEED = 10
SEGMENT_SIZE = 10

# создание окна
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game - New Look")

# направления движения змейки
UP = (0, -SPEED)
DOWN = (0, SPEED)
LEFT = (-SPEED, 0)
RIGHT = (SPEED, 0)

# начальные значения счёта и уровня
score = 0
level = 1

# используем новый шрифт
font = pygame.font.Font(pygame.font.get_default_font(), 30)

# класс для змейки
class Snake:
    def __init__(self):
        # начальная позиция змейки 
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = RIGHT  # Начальное направление

    # метод для движения змейки
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # проверка на столкновение с границами
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            game_over()

        self.body.insert(0, new_head)  # добавляем новый сегмент в начало
        self.body.pop()  # удаляем последний сегмент (тело змейки)

    # метод для роста змейки
    def grow(self):
        self.body.append(self.body[-1])  # добавляем новый сегмент в конец

    # метод для изменения направления
    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    # метод для рисования змейки
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, DARK_GREEN, (segment[0], segment[1], SEGMENT_SIZE, SEGMENT_SIZE))

# класс для яблока
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SEGMENT_SIZE, SEGMENT_SIZE))
        self.image.fill(RED)  # Цвет яблока
        self.rect = self.image.get_rect()
        self.spawn()

    # метод для генерации случайной позиции яблока
    def spawn(self):
        self.rect.topleft = (
            random.randint(0, (SCREEN_WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
            random.randint(0, (SCREEN_HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
        )

    # метод для рисования яблока
    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, self.rect)  # цвет яблока

# функция для завершения игры
def game_over():
    print("Game Over!")
    pygame.quit()
    sys.exit()

# создание объектов змейки и яблока
snake = Snake()
apple = Apple()

while True:
    # обрабатываем все события
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    # двигаем змейку
    snake.move()

    # проверка, если змейка съела яблоко
    if snake.body[0] == apple.rect.topleft:
        snake.grow()
        apple.spawn()
        score += 1

        # повышаем уровень каждые 5 яблок
        if score % 5 == 0:
            level += 1
            FPS += 2

    # заполнение фона
    DISPLAYSURF.fill(LIGHT_GREEN)

    # отображение счёта 
    score_text = font.render(f"Score: {score}", True, DARK_GREEN)
    DISPLAYSURF.blit(score_text, (10, 10))

    # отображение уровня 
    level_text = font.render(f"Level: {level}", True, DARK_GREEN)
    DISPLAYSURF.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, SCREEN_HEIGHT - level_text.get_height() - 10))

    # рисуем змейку и яблоко
    snake.draw(DISPLAYSURF)
    apple.draw(DISPLAYSURF)

    # обновляем экран
    pygame.display.update()

    # управляем фпсом
    FramePerSec.tick(FPS)
