import pygame
import plane_sprites


class PlaneGame(object):

    def __init__(self):

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(plane_sprites.SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，创建游戏精灵和精灵组
        self.__create_sprites()

        # 设置定时器事件，创建敌机/s   两个参数分别是eventid和事件创建间隔，单位毫秒
        pygame.time.set_timer(plane_sprites.CREATE_ENEMY_EVENT, 1000)

        # 设置定时器事件，英雄飞机发射子弹/s  一秒三弹
        pygame.time.set_timer(plane_sprites.HERO_FIRE_EVENT, 333)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = plane_sprites.Background()
        bg2 = plane_sprites.Background(is_alt=True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建玩家飞机精灵和精灵组(因为需要检测玩家飞机是否与敌机或敌机子弹发生碰撞，所以把玩家飞机
        # 这个对象定义为属性，以便在其他方法中直接使用)
        self.hero = plane_sprites.Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        while True:

            # 1.设置刷新帧率
            self.clock.tick(plane_sprites.FRAME_PRE_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):

        event_list = pygame.event.get()
        for event in event_list:
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                # 静态方法用类名调用
                PlaneGame.__game_over()
            elif event.type == plane_sprites.CREATE_ENEMY_EVENT:
                # 1.创建敌机精灵
                enemy = plane_sprites.Enemy()
                # 2.添加到敌机精灵组
                self.enemy_group.add(enemy)
            # 此方法不支持长按一个键
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
            elif event.type == plane_sprites.HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘模块提供的方法获取键盘按键  ——>键盘元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值 bool型
        if keys_pressed[pygame.K_RIGHT]:
            # print("向右移动")
            self.hero.x_speed = 4
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.x_speed = -4
        else:
            self.hero.x_speed = 0
        if keys_pressed[pygame.K_UP]:
            self.hero.y_speed = -4
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.y_speed = 4
        else:
            self.hero.y_speed = 0
        # else:
        #     self.hero.speed = 0

    def __check_collide(self):
        # 1.子弹摧毁敌机 参数分别为两个精灵组，第三个True表示两精灵组中精灵发生碰撞，第一个精灵组中的精灵被销毁，第四个True相反
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # 2.敌机撞毁英雄飞机  参数为一个精灵，一个精灵组，True表示精灵与精灵组中的精灵碰撞，精灵组中的精灵被销毁，
        # 该方法返回一个精灵列表，里面保存的是与精灵发生碰撞的精灵组中的精灵
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 如果返回的精灵列表不为空，表示英雄飞机精灵与敌机精灵组发生了碰撞，游戏gg
        if len(enemies) > 0:
            # 英雄飞机被销毁
            self.hero.kill()
            # 游戏结束
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 背景精灵组更新+显示
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 敌机精灵组更新+显示
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 玩家飞机精灵组更新+显示
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹精灵组更新+显示
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():

        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 调用游戏开始方法
    game.start_game()