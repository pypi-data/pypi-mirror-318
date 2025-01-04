from kivy.graphics import Color, Line, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
"""
        body= Polyline_Drawing(meun=True, size_hint=(.5, .5))
        body.plot(x_list=[0,1,2,3,4,5,6,7,10],y_list=[1,2,3,4,5,6,7,8,10], color=(0,1,0,1))
        body.plot(x_list=[0,1,2,3,4,5,6,7,9,10],y_list=[0,10,2,3,56,55,30,44,35,10])
        body.plot(x_list=[0,1,2,3,4,5,6], y_list=[12,52,23,24,45,66], color=(1,0,0,1),dash = True)
"""





class list1(Line):
    def __init__(self, **kwargs):
        super().__init__()
        # print(kwargs)
        for i in kwargs.items():
            self.__setattr__(*i)
        # self.width =2
        # if self.dash
class Polyline(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.size_hint = (.9, .9)
        self.pos_hint = {'x': .05, 'y': .05}
        self.axis = []
        self.data_line = []
        with self.canvas:
            Color(0, 0, 0, 1)
            self.axis_left = Line()
            self.axis_right = Line()
            self.axis_top = Line()
            self.axis_bottom = Line()
        self.axis.append(self.axis_left)
        self.axis.append(self.axis_right)
        self.axis.append(self.axis_top)
        self.axis.append(self.axis_bottom)

class Polyline_Drawing(Screen):
    def __init__(self,title="text_1", meun=False,back=(1,1,1,1),x_name="",y_name="",**kwargs):
        super().__init__()
        self.back = back
        # print(kwargs)
        for i in kwargs.items():
            self.__setattr__(*i)
        self.meun = meun
        self.titless = Label(text=title, size_hint=(.8, .05), pos_hint={"top":1, "x":.1}, color=(0,0,0,1), font_size="18sp")
        self.add_widget(self.titless)
        self.ploath = Polyline()
        self.add_widget(self.ploath)
        self.ploath.bind(size=self.update)
        self.bind(size=self.update_background)
        # self.bind(pos=self.update)
        self.max_x = 10
        self.max_y = 10
        self.y_name = Label(text=y_name, size_hint=(None, None), pos_hint={"x":0, "center_y":.5}, color=(0,0,0,1))
        self.y_name.bind(texture_size=self.y_name.setter("size"))
        self.add_widget(self.y_name)

        self.x_name = Label(text=x_name, size_hint=(None, None), pos_hint={"center_x":.5, "y":0}, color=(0,0,0,1))
        self.x_name.bind(texture_size=self.x_name.setter("size"))

        self.add_widget(self.x_name)


        with self.canvas.before:
            Color(*self.back)
            self.rects = Rectangle()
    def plot(self, x_list, y_list, color=(0,0,0), width=2, **kwargs):
        add_line = list1(xlist=x_list,ylist=y_list,color=color, width=width, **kwargs)
        self.max_x = self.max_x if self.max_x>max(x_list) else max(x_list)
        self.max_y = self.max_y if self.max_y>max(y_list) else max(y_list)

        print(self.max_y)
        print(self.max_x)
        self.ploath.canvas.add(Color(*color))
        self.ploath.canvas.add(add_line)
        self.ploath.data_line.append(add_line)
    def del_axis(self, axis):
        # self.ploath.delete(axis)
        self.ploath.canvas.remove(getattr(self.ploath, axis))

    def update_background(self, widget,size):

        self.rects.size=widget.size

    def update(self,widget,size):
        # widget.canvas.

        widget.axis_left.points=[0,0,0,size[1]]
        widget.axis_right.points=[size[0],size[1],size[0],0]
        widget.axis_top.points=[size[0],size[1],0,size[1]]
        widget.axis_bottom.points=[0,0,size[0],0]

        for i in widget.data_line:
            i.points =[]
            for x,y in zip(i.xlist, i.ylist):

                i.points.append(x*(widget.width*(1/self.max_x)))
                i.points.append(y*(widget.height*(1/self.max_y)))
                # if i.dash:
                if self.meun:
                    lxs = Label(text=str(x), size_hint=(None, None), pos=[x * (widget.width * (1 / self.max_x)), -30],
                               color=i.color)
                    lxs.bind(texture_size=lxs.setter("size"))
                    self.ploath.add_widget(lxs)
                    self.ploath.canvas.add(Color(*i.color))
                    self.ploath.canvas.add(Line(dash_length=1,dash_offset=1, points=[x * (widget.width * (1 / self.max_x)), 0,x * (widget.width * (1 / self.max_x)), y*widget.height * (1 / self.max_y)], width=1))

                    lys = Label(text=str(y), size_hint=(None, None), pos=[-30,y * (widget.height * (1 / self.max_y))],
                               color=i.color)
                    lys.bind(texture_size=lys.setter("size"))
                    self.ploath.canvas.add(Color(*i.color))

                    self.ploath.canvas.add(Line(dash_length=1,dash_offset=1, points=[0,y*widget.height * (1 / self.max_y),x * (widget.width * (1 / self.max_x)), y*widget.height * (1 / self.max_y)], width=1))

                    self.ploath.add_widget(lys)

        if not self.meun:
            for i in range(0, self.max_x, int(self.max_x / 10)):
                lx = Label(text=str(i), size_hint=(None, None), pos=[i * (widget.width * (1 / self.max_x)), -30],
                           color=(0, 0, 0, 1))
                lx.bind(texture_size=lx.setter("size"))
                self.ploath.add_widget(lx)
                self.ploath.canvas.add(Color(0, 0, 0))
                self.ploath.canvas.add(Rectangle(size=[2, 10], pos=[i * (widget.width * (1 / self.max_x)), 0]))

            for i in range(0, self.max_y, int(self.max_y / 10)):
                self.ploath.canvas.add(Color(0, 0, 0))
                self.ploath.canvas.add(Rectangle(size=[10, 2], pos=[0, i * (widget.height * (1 / self.max_y))]))
                lx = Label(text=str(i), size_hint=(None, None), pos=[-30, i * (widget.height * (1 / self.max_y))],
                           color=(0, 0, 0, 1))
                lx.bind(texture_size=lx.setter("size"))
                self.ploath.add_widget(lx)

