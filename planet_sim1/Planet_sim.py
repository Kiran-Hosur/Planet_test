from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse ,Line
from kivy.clock import Clock
import random
from kivy.config import Config
from kivy.core.window import Window

G = 1
scale = 10
class ball(Widget):
    # pass
    def __init__(self, mass=1,radius=200,x=400,y=300,colour = (1,0,0) ):
        super(ball, self).__init__()
        self.mass = mass
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        with self.canvas:
            Color(colour[0],colour[1],colour[2])
            self.circ = Ellipse(pos=(self.x,self.y),size=(self.radius,self.radius))
            self.line = Line(points = [self.x,self.y])

    def calc_position(self,Ax,Ay,dt):
        self.vx = self.vx + Ax * dt * scale
        self.vy = self.vy + Ay * dt * scale
        self.x = self.x + self.vx * dt * scale
        self.y = self.y + self.vy * dt * scale
        self.circ.pos = (self.x-self.radius/2,self.y-self.radius/2)
        self.update_line()
    
    def update_line(self):
        if len(self.line.points)<100:
            self.line.points.extend([self.x,self.y])
        else:
            self.line.points = self.line.points[2:]
            self.line.points.extend([self.x,self.y])

class system(Widget):
    def __init__(self):
        super().__init__()
        self.objects = []
        h = Config.get('graphics', 'height')
        w = Config.get('graphics', 'width')
        # wid = ball(radius=50,x=self.width/2,y=self.height/2)
        wid = ball(mass=100000,radius=100,x=w,y=h)
        self.objects.append(wid)
        self.add_widget(wid)

    def update(self,dt):
        for obj1 in self.objects:
            Ax,Ay = 0,0
            for obj2 in self.objects:
                if not (obj1==obj2):
                    r = ((obj1.x - obj2.x)**2 + ((obj1.y - obj2.y)**2))**0.5
                    g = obj1.mass * obj2.mass * G /r**2
                    ax = g * (obj2.x - obj1.x)/r / obj1.mass
                    ay = g * (obj2.y - obj1.y)/r / obj1.mass
                    Ax += ax
                    Ay += ay
            obj1.calc_position(Ax,Ay,dt)

    def on_touch_down(self, touch):
        # return super().on_touch_down(touch)
        self.tmp_x = touch.x        
        self.tmp_y = touch.y

    def on_touch_up(self, touch):
        wid = ball(radius=30,x=touch.x,y=touch.y,colour=(0,1,0))
        self.objects.append(wid)
        self.add_widget(wid)
        wid.vx = (self.tmp_x - touch.x)/10
        wid.vy = (self.tmp_y - touch.y)/10
        
class view3App(App):
    def build(self):
        motion = system()
        # motion.start()
        Clock.schedule_interval(motion.update, 1.0 / 60.0)
        return motion

if __name__ == '__main__':
    view3App().run()