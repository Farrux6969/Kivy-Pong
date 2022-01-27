# from random import randint
#
# from kivy.app import App
# from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, Clock
# from kivy.uix.widget import Widget
# from kivy.uix.bubble import Button
# from kivy.vector import Vector
#
# class PongPaddle(Widget):
#
#     score = NumericProperty(0)
#
#     def bounce_ball(self, ball):
#         if self.collide_widget(ball):
#             speedup  = 1.1
#             offset = 0.02 * Vector(0, ball.center_y-self.center_y)
#             ball.velocity =  speedup * (offset - ball.velocity)
#
# class PongBall(Widget):
#     velocity_x = NumericProperty(0)
#     velocity_y = NumericProperty(0)
#     velocity = ReferenceListProperty(velocity_x,velocity_y)
#     def move(self):
#         self.pos = Vector(*self.velocity) + self.pos
#
# class PongGame(Widget):
#     ball = ObjectProperty(None)
#
#     def serve_ball(self):
#         self.ball.center = self.center
#         self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))
#
#     def update(self, dt):
#         self.ball.move()
#
#       # bounce off top and bottom
#         if (self.ball.y < 0) or (self.ball.top > self.height):
#             self.ball.velocity_y *= -1
#         # bounce off left and right
#         if (self.ball.x < 0) or (self.ball.right > self.width):
#             self.ball.velocity_x *= -1
#
#     def on_touch_move(self, touch):
#
#         if touch.x < self.width / 3:
#
#             self.player1.center_y = touch.y
#
#         if touch.x > self.width - self.width / 3:
#             self.player2.center_y = touch.y
#
# class PongApp(App):
#     def build(self):
#         game=PongGame()
#         game.serve_ball()
#         Clock.schedule_interval(game.update, 1.0 / 60.0)
#         return game
#
# if __name__ == '__main__':
#     PongApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos



class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
def finish(self):
    velocity_y = NumericProperty(0)
    velocity_x = NumericProperty(0)
    if velocity_x==10:
        print("Player1 WINS")
        breakpoint()
    elif velocity_y==10:
        print("Player2 WINS")
        breakpoint()
if __name__ == '__main__':
    PongApp().run()