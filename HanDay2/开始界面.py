##作图 显示开始的界面
import sys
from itertools import product
import pygame
from random import choice


panel_width = 640
panel_height = 480
pygame.init() #它必须在导入pygame模块之后，且开始使用Pygame提供的任何函数前调用，你不必知道此函数的作用，只需要知道，为了使用pygame函数能正常工作，必须在一开始就调用它。如果你碰到像pygame.error: font not initialized这样的错识，请检查一下是否忘记了在程序前面调用pygame.init()。
window = pygame.display.set_mode((panel_width,panel_height))
pygame.display.set_caption('This is first')

def draw_Grid(screen,Window_Width,Window_Height,Cell_Size,result):
    # 垂直方向
    for x in range(0, Window_Width, Cell_Size):
        pygame.draw.line(screen, result, (x, 0), (x, Window_Height))
    # 水平方向
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(screen, result, (0, y), (Window_Width, y))

# color_list = [0,64,128,192,255]
# colors = product(color_list,repeat=3)
# colors = list(colors)
# result = choice(colors)

title_font = pygame.font.SysFont('arial',40)
start_panel = title_font.render('Welcome to Greedy Snake',True,(255,255,255),(0,0,0))
tips_font = pygame.font.SysFont('arial', 24)
start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))
close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))
window.blit(start_panel,(188,100))
window.blit(start_game_words, (236, 310))
window.blit(close_game_words, (233, 350))

while True:
	for event in pygame.event.get():
		print(len(list(pygame.event.get())))
		if event.type == pygame.KEYDOWN:
			print(event.key)
			if event.key == 27:
				pygame.quit()
				sys.exit()
		elif event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		else:
			print('Not key')
	pygame.display.update()
