import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15  # радиус для рисования
    x, y = 0, 0
    mode = 'blue'  # начальный режим рисования (цвет)
    points = []  # список для хранения точек для рисования линий
    drawing = False  # флаг, показывающий, рисуется ли фигура
    start_pos = None  # начальная позиция для рисования
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]  # проверка нажатия ALT
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]  # проверка нажатия CTRL
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_l:
                    mode = 'rectangle'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_q:
                    mode = 'square'  # рисуем квадрат
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'  # рисуем прямоугольный треугольник
                elif event.key == pygame.K_y:
                    mode = 'equilateral_triangle'  # рисуем равносторонний треугольник
                elif event.key == pygame.K_h:
                    mode = 'rhombus'  # рисуем ромб
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mode in ['circle', 'rectangle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        start_pos = event.pos
                        drawing = True
                    elif mode == 'eraser':
                        points = [p for p in points if not (abs(p[0] - event.pos[0]) < radius and abs(p[1] - event.pos[1]) < radius)]
                elif event.button == 3:
                    radius = max(1, radius - 1)  # уменьшение радиуса

            if event.type == pygame.MOUSEMOTION:
                if drawing and mode in ['circle', 'rectangle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                    end_pos = event.pos
                    screen.fill((0, 0, 0))  # очищаем экран
                    if mode == 'circle':
                        pygame.draw.circle(screen, get_color(mode), start_pos, int(((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2) ** 0.5))
                    elif mode == 'rectangle':
                        pygame.draw.rect(screen, get_color(mode), pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
                    elif mode == 'square':
                        side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        pygame.draw.rect(screen, get_color(mode), pygame.Rect(start_pos[0], start_pos[1], side_length, side_length))
                    elif mode == 'right_triangle':
                        pygame.draw.polygon(screen, get_color(mode), [start_pos, (start_pos[0], end_pos[1]), end_pos])
                    elif mode == 'equilateral_triangle':
                        height = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                        pygame.draw.polygon(screen, get_color(mode), [start_pos, (start_pos[0] + height, end_pos[1]), (start_pos[0] - height, end_pos[1])])
                    elif mode == 'rhombus':
                        width = abs(end_pos[0] - start_pos[0])
                        height = abs(end_pos[1] - start_pos[1])
                        pygame.draw.polygon(screen, get_color(mode), [(start_pos[0], start_pos[1] - height), (start_pos[0] + width, start_pos[1]), (start_pos[0], start_pos[1] + height), (start_pos[0] - width, start_pos[1])])
                
                position = event.pos
                points = points + [position]
                points = points[-256:]
        
        if not drawing:
            screen.fill((0, 0, 0))  # очищаем экран
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        pygame.display.flip()
        clock.tick(60)

def get_color(mode):
    """Возвращает цвет в зависимости от выбранного режима рисования"""
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'circle':
        return (255, 255, 0)  # жёлтый для круга
    elif mode == 'rectangle':
        return (255, 165, 0)  # оранжевый для прямоугольника
    elif mode == 'square':
        return (0, 255, 255)  # голубой для квадрата
    elif mode == 'right_triangle':
        return (255, 105, 180)  # розовый для прямоугольного треугольника
    elif mode == 'equilateral_triangle':
        return (255, 69, 0)  # оранжевый для равностороннего треугольника
    elif mode == 'rhombus':
        return (238, 130, 238)  # фиолетовый для ромба
    elif mode == 'eraser':
        return (0, 0, 0)  # чёрный для ластика

def drawLineBetween(screen, index, start, end, width, color_mode):
    """Рисует линию между двумя точками с цветом в зависимости от режима"""
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
