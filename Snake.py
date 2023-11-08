import pygame
from game_items import *

class Game(object):
    main_window = None
    score = None
    sorce_label = None
    def __init__(self):
        self.main_window = pygame.dispaly.set_mode((640,480)) #画布
        pygame.display.set_caption("贪吃蛇")
        self.score = 0
        self.score_label = Label()
        
    def start(self):
        clock = pygame.time.Clock() #游戏时钟
        while True:
            #依次绘制游戏元素
            self.main_windows.fill(BACKGROUND_COLOR) #窗口背景
            self.score += 1 #增加游戏得分
            self.sorce_label.draw(self.main_window,"得分：%d " % self.score) #在主窗口绘制分数
            
            #更新显示
            pygame.dispaly.update()#刷新
            clock.tick(60) #刷新帧率       


if __name__ == '__main__' :
    pygame.init()
    Game().start()
    pygame.quit()
