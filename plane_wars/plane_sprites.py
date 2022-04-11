import random
import pygame


# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PRE_SEC = 60
# 创建敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄飞机发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """定义飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类中的__init__()方法，否则在子类中调用父类方法时会出错
        super().__init__()

        self.image = pygame.image.load(image_name)  # image_name其实就是加载图片的路径
        self.rect = self.image.get_rect()           # 默认初始位置(0,0)，后面RectType参数是图片宽高
        self.speed = speed

    def update(self):

        # 敌机在垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类的__init__方法，给定Background类的默认初始图片路径
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    # 重写update类，使屏幕滚动
    def update(self):

        # 调用父类方法实现
        super().update()
        # 判断屏幕是否移出界面，如果移出，放回最上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类的__init__方法，给定敌机初始默认图片路径
        super().__init__("./images/enemy1.png")
        # 2.设置敌机随机飞行速度
        self.speed = random.randint(1, 3)
        # 3.设置敌机随机初始位置
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类方法，保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果飞出，将敌机从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("敌机飞出屏幕，需要将其从精灵组中移除")
            # kill方法可以把精灵从所用精灵组中移出，精灵会被自动销毁
            self.kill()

    # 有对象在内存中被销毁时，首先调用此方法
    # def __del__(self):
    #     print("敌机gg %s" % self.rect)


class Hero(GameSprite):
    """英雄精灵类"""

    def __init__(self):
        # 1.调用父类，给定英雄飞机默认图片路径以及初始速度
        super().__init__("./images/me1.png")
        # # 2.设置英雄飞机初始速度
        # self.speed = 0
        self.x_speed = 0
        self.y_speed = 0
        # 3.设置英雄飞机初始位置
        self.rect.x = (SCREEN_RECT.width-self.rect.width)/2
        self.rect.y = SCREEN_RECT.height-self.rect.height-50
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        # 英雄飞机移动
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # 控制英雄飞机移动边界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.width-self.rect.width:
            self.rect.x = SCREEN_RECT.width-self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_RECT.height-self.rect.height:
            self.rect.y = SCREEN_RECT.height-self.rect.height

    def fire(self):
        # 1.创建子弹精灵
        bullet = Bullet()
        # 2.设置子弹初始位置
        bullet.rect.y = self.rect.y-bullet.rect.height
        bullet.rect.x = self.rect.x+0.5*self.rect.width
        # 3.将子弹添加到子弹精灵组中
        self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵类"""

    def __init__(self):
        # 指定子弹图片以及子弹初始速度
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 子弹垂直方向移动
        super().update()

        # 如果子弹飞出屏幕，在内存中销毁子弹
        if self.rect.y < -self.rect.height:
            self.kill()

    # def __del__(self):
    #     print("子弹被销毁")



