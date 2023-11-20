import pygame
from pygame.locals import *

pygame.init()


screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")

line_width = 6
marker = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

green = (0, 255, 200)
red = (255, 0, 0)
blue = (0, 0, 255)

font = pygame.font.SysFont(None, 40)

ag_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)


def draw_grid():
    bg = (135, 206, 235)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(
            screen, grid, (0, x * 100), (screen_width, x * 100), line_width
        )
        pygame.draw.line(
            screen, grid, (x * 100, 0), (x * 100, screen_height), line_width
        )


for x in range(3):
    row = [0] * 3
    marker.append(row)
print(marker)


def draw_marker():
    x_pos = 0
    for x in marker:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(
                    screen,
                    red,
                    (x_pos * 100 + 15, y_pos * 100 + 15),
                    (x_pos * 100 + 85, y_pos * 100 + 85),
                    line_width,
                )
                pygame.draw.line(
                    screen,
                    red,
                    (x_pos * 100 + 85, y_pos * 100 + 15),
                    (x_pos * 100 + 15, y_pos * 100 + 85),
                    line_width,
                )
            if y == -1:
                pygame.draw.circle(
                    screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width
                )
            y_pos += 1
        x_pos += 1


def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in marker:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if marker[0][y_pos] + marker[1][y_pos] + marker[2][y_pos] == 3:
            winner = 1
            game_over = True
        if marker[0][y_pos] + marker[1][y_pos] + marker[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    if (
        marker[0][0] + marker[1][1] + marker[2][2] == 3
        or marker[2][0] + marker[1][1] + marker[0][2] == 3
    ):
        winner = 1
        game_over = True
    if (
        marker[0][0] + marker[1][1] + marker[2][2] == -3
        or marker[2][0] + marker[1][1] + marker[0][2] == -3
    ):
        winner = 2
        game_over = True


def draw_winner(winner):
    win_text = "Player " + str(winner) + " wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(
        screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50)
    )
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    ag_text = "Play Again?"
    ag_img = font.render(ag_text, True, blue)
    pygame.draw.rect(screen, green, ag_rect)
    screen.blit(ag_img, (screen_width // 2 - 80, screen_height // 2 + 10))


run = True
while run:
    draw_grid()
    draw_marker()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if marker[cell_x][cell_y] == 0:
                    marker[cell_x][cell_y] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if ag_rect.collidepoint(pos):
                marker = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    marker.append(row)

    pygame.display.update()

pygame.quit()
