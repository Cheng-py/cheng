# -*- coding:utf-8 -*-
# 描述    :  练习FlyBird
# Author :  程小文
# @Time  :  
# @File  :

import sys

import time

import pygame


# 定义一个音效组

class Musci():
    def __init__(self):
        self.die = pygame.mixer.music.load('die.wav')
        self.hit = pygame.mixer.music.load('hit.wav')
        self.point = pygame.mixer.music.load('point.wav')

    def pay(self):
        pygame.mixer.music.play(self.point)


# 定义一个鸟类

class Bird:

    # 定义初始化方法
    def __init__(self):
        # 初始化
        self.birdRect = pygame.Rect(60, 50, 50, 50)  # 鸟的矩形 ，范围
        # 定义三种状态，飞翔动作与死亡状态
        # 三种状态的列表 (图片)
        self.birdStatus = [pygame.image.load("assets/1.png"),
                           pygame.image.load("assets/2.png"),
                           pygame.image.load("assets/dead.png")]

        self.status = 0  # 默认飞翔状态
        self.birdX = 120  # 鸟所在的 X 轴坐标，即是向右飞行的速度
        self.birdY = 350  # 鸟所在的 Y 轴坐标，即上下飞行高度
        self.jump = False  # 默认小鸟的情况自动降落
        self.jumpSpeed = 10  # 跳跃高度
        self.gravity = 5  # 重力
        self.dead = False  # 默认小鸟生命状态为活着,没死

    # 实现小鸟的动作流程
    def birdUpdate(self):
        if self.jump:
            # 如果小鸟跳跃为真:
            self.jumpSpeed -= 1  # 小鸟的跳跃距离越高速度越来越慢
            self.birdY -= self.jumpSpeed  # 鸟 Y 轴坐标减小，小鸟上升
        else:
            # 小鸟坠落
            self.gravity += 0.2  # 重力递增，下降速度越来越快
            self.birdY += self.gravity  # 鸟 Y 轴坐标增加，小鸟下降
        self.birdRect[1] = self.birdY  # 更改 Y 轴位置


class Pipeline:
    """定义一个管道类 """

    def __init__(self):
        """定义初始化方法"""
        self.wallx = 400  # 管道所在 X 轴坐标
        self.pineUp = pygame.image.load('assets/top.png')  # 上面的管道图
        self.pineDown = pygame.image.load('assets/bottom.png')  # 下面的管道图

    def updatePipeline(self):
        """管道移动方法"""
        self.wallx -= 6  # 管道X轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞跃管道，分数加1，并且重置管道

        global score
        if self.wallx < -80:  # 判断过了管道
            point = pygame.mixer.Sound('point.wav')
            point.play()
            point.set_volume(0.3)
            score += 1  # 分数加1
            self.wallx = 400  # 重置管道


def creatMap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))  # 填充颜色
    screen.blit(background, (0, 0))  # 填入到背景

    # 显示管道
    screen.blit(Pipeline.pineUp, (Pipeline.wallx, -300))  # 上管道坐标位置
    screen.blit(Pipeline.pineDown, (Pipeline.wallx, 500))  # 下管道坐标位置
    Pipeline.updatePipeline()  # 管道移动

    # 显示小鸟
    if Bird.dead:
        # 撞管道状态
        Bird.status = 2
    elif Bird.jump:
        # 起飞状态
        Bird.status = 0
        Bird.status = 1
    screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY))  # 设置小鸟坐标
    Bird.birdUpdate()  # 鸟移动

    # 显示分数
    screen.blit(font.render('Score' + str(score), -1, (255, 255, 255)), (150, 50))  # 设置颜色及坐标
    pygame.display.update()  # 更新显示


def checkDead():
    # 上方管子的矩形位置
    upRect = pygame.Rect(Pipeline.wallx, -300,
                         Pipeline.pineUp.get_width() - 10,
                         Pipeline.pineUp.get_height()
                         )

    # 下方管子的矩形位置
    downRect = pygame.Rect(Pipeline.wallx, 500,
                           Pipeline.pineDown.get_width() - 10,
                           Pipeline.pineDown.get_height()
                           )

    # 检测小鸟与上下方管子是否碰撞
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead = True

    # 检测 小鸟 是否飞出上下边界
    if not 0 < Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False


def getResutl():  # 结果
    final_text1 = "Game Over"

    final_text2 = "You final score is :" + str(score)

    ft1_font = pygame.font.SysFont("Arial", 70)  # 设置一行文字字体
    ft1_surf = font.render(final_text1, 1, (246, 24, 50))  # 设置第一行文字颜色

    ft2_font = pygame.font.SysFont("Arial", 50)  # 设置第二行文字字体
    ft2_surf = font.render(final_text2, 1, (253, 200, 6))  # 设置第二行文字颜色

    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置第二行文字显示位置

    pygame.display.flip()  # 更新整个待显示的Surface 对象


if __name__ == '__main__':
    pygame.init()  # 初始化pygame
    pygame.font.init()  # 初始化字体
    pygame.mixer.init()  # 初始化音乐

    font = pygame.font.SysFont('Arial', 45)  # 设置字体和大小
    size = width, height = 400, 650  # 设置窗口
    screen = pygame.display.set_mode(size)  # 显示窗口

    clock = pygame.time.Clock()  # 设置时钟

    Pipeline = Pipeline()  # 实例化管道类
    Bird = Bird()  # 实例化鸟类

    pygame.mixer.music.load('in.mp3')  # 添加背景音乐
    pygame.mixer.music.play(-1)  # 循环背景音乐
    pygame.mixer.music.set_volume(0.5)  # 背景音乐音量

    # music = Musci()
    score = 0
    die_music = 1  # 添加控制死亡音效的条件
    run = True
    while run:
        # 循环主体

        clock.tick(60)  # 每秒执行60次

        # 轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出
                sys.exit()

            if event.type == pygame.K_SPACE:
                time.sleep(1)
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                sw = pygame.mixer.Sound('swoosh.wav')
                sw.play(0)
                sw.set_volume(0.2)
                Bird.jump = True  # 跳跃
                Bird.gravity = 5  # 重力
                Bird.jumpSpeed = 10  # 跳跃速度
        background = pygame.image.load("assets/background.png")  # 加载背景图片

        if checkDead():
            """检测小鸟生命状态"""
            pygame.mixer.music.stop()
            # 添加死亡音效
            if die_music == 1:
                # 当小鸟死亡时，die_music+1，使音效循环条件不成立
                die_music += 1
                die = pygame.mixer.Sound('die.wav')
                die.play()
                die.set_volume(0.5)


            getResutl()  # 如果小鸟死亡，显示结果，分数


        else:
            creatMap()  # 创建地图

pygame.quit()
