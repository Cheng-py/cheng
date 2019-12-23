import pygame
import sys
import time
# pygame.init()
# pygame.mixer.init()
# lujing = 'sunny.mp3'
# i = 1
# pygame.mixer.music.load(lujing)
# res =pygame.mixer_music.play()
# size = widht,height = 600,1000
# screen = pygame.display.set_mode(size)
# pan = True
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

class Bird:
    def __init__(self):
        # 初始化方法
        self.BirdStatus = [pygame.image.load("assets/1.png"),
                           pygame.image.load("assets/2.png"),
                           pygame.image.load("assets/dead.png")]
        self.status = 0
        self.birdx = 120
        self.birdy = 350
        self.jump = False
        self.jumpspeed = 10
        self.graviry = 5
        self.dead = False

    def BirdUpdate(self):
        # 定义移动方法
        if self.jump:
            self.jumpspeed -= 1
            self.birdy -= self.jumpspeed
        else:
            self.graviry += 0.2
            self.birdy +=self.graviry

class PipeLine:
    def __init__(self):
        # 初始化方法
        pass
    def UpdatePipe(self):
        # 定义移动方法
        pass

def creatMap():
        # 创建地图
        screen.blit(background, (0, 0))
        pygame.display.flip()
        # 创建小鸟
        if Bird.dead:
            Bird.Status = 2
        elif Bird.jump:
            Bird.status = 1
        screen.blit(Bird.birdStatus[Bird.status],(Bird.birdx,Bird.birdy))

        pygame.display.update()


if __name__ == '__main__':
    # 编写主程序
    pygame.init()
    pygame.mixer.init()
    size = width,height = 400,650
    screen =pygame.display.set_mode(size) # 添加窗口
    clock = pygame.time.Clock()
    color = (255,255,255)
    bird = Bird()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN and not bird.dead:
                bird.jump = True
                bird.jumpspeed = 10
                bird.graviry = 5
        background = pygame.image.load("assets/background.png")
        creatMap() #生成地图




    pygame.quit()
