from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1800)
        self.y = y if y else random.randint(100, 924)
        self.sx, self.sy = 0, 0
    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(self.sx, self.sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10

    def handle_collision(self, group, other):
        if group =="boy:ball":
            game_world.remove_object(self)
            pass
