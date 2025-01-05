from kivy.graphics import Color, Line, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

"""
    https://pypi.org/project/kivy-plot/0.0.1/
    https://github.com/rcnn-retall/kivy_plot

"""
class Rects_line(Rectangle):
    def __init__(self, **kwargs):
        super(Rects_line, self).__init__()
        for i in kwargs.items():
            self.__setattr__(*i)

class Line_lis(Line):
    def __init__(self, **kwargs):
        super(Line_lis, self).__init__()
        for i in kwargs.items():
            self.__setattr__(*i)


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

class LineLayout(Screen):
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

        self.axis_x = []
        self.axis_y = []
        self.axis_x_label = []
        self.axis_y_label = []


        self.axis_x_m = []
        self.axis_y_m = []
        self.axis_x_line = []
        self.axis_y_line = []

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
        # print(self.max_y)
        # print(self.max_x)
        self.ploath.canvas.add(Color(*color))
        self.ploath.canvas.add(add_line)
        self.ploath.data_line.append(add_line)
        if not self.meun:
            [self.ploath.remove_widget(l) for l in self.axis_x_label]
            [self.ploath.canvas.remove(i) for i in self.axis_x]
            self.axis_x_label=[]
            self.axis_x = []
            # [(, self.ploath.canvas.remove(i)) for l, i in (self.axis_y_label, self.axis_y)]
            [self.ploath.remove_widget(l) for l in self.axis_y_label]
            [self.ploath.canvas.remove(i) for i in self.axis_y]
            self.axis_y_label=[]
            self.axis_y=[]

            for i in range(0, self.max_x, int(self.max_x / 10)):
                lx = Label(text=str(i), size_hint=(None, None),
                           # pos=[i * (widget.width * (1 / self.max_x)), -30],
                           color=(0, 0, 0, 1))
                lx.bind(texture_size=lx.setter("size"))
                lx.index = i
                self.ploath.add_widget(lx)
                self.axis_x_label.append(lx)

                self.ploath.canvas.add(Color(0, 0, 0))
                rect_x =Rects_line(size=[2, 10])
                self.ploath.canvas.add(rect_x)
                rect_x.index = i
                self.axis_x.append(rect_x)

                                                 # , pos=[i * (widget.width * (1 / self.max_x)), 0]))

            for i in range(0, self.max_y, int(self.max_y / 10)):
                self.ploath.canvas.add(Color(0, 0, 0))

                rect_y = Rects_line(size=[10, 2])
                self.ploath.canvas.add(rect_y)
                rect_y.index = i
                self.axis_y.append(rect_y)
                                                 # , pos=[0, i * (widget.height * (1 / self.max_y))]))
                lx = Label(text=str(i), size_hint=(None, None),
                           # , pos=[-30, i * (widget.height * (1 / self.max_y))],
                           color=(0, 0, 0, 1))
                lx.bind(texture_size=lx.setter("size"))
                lx.index = i
                self.axis_y_label.append(lx)
                self.ploath.add_widget(lx)
        else:
            # print(len(self.ploath.data_line))
            # print(len(self.axis_x_line))
            # print(len(self.axis_x_m))
            # print(self.ploath.data_line)
            # for i in self.ploath.data_line:

            for x, y in zip(self.ploath.data_line[-1].xlist, self.ploath.data_line[-1].ylist):
                # print(x,y)


                lxs = Label(text=str(x), size_hint=(None, None),color=self.ploath.data_line[-1].color)
                lxs.xs = x
                lxs.bind(texture_size=lxs.setter("size"))
                self.axis_x_m.append(lxs)
                self.ploath.add_widget(lxs)

                self.ploath.canvas.add(Color(*self.ploath.data_line[-1].color))
                x_lines = Line_lis(dash_length=1, dash_offset=1, width=1)
                x_lines.xs = x
                x_lines.ys = y
                self.axis_x_line.append(x_lines)
                self.ploath.canvas.add(x_lines)
                # axis_y_m
                lys = Label(text=str(y), size_hint=(None, None),color=self.ploath.data_line[-1].color)
                lys.ys = y
                # self.axis_y_label.append(lys)
                lys.bind(texture_size=lys.setter("size"))
                self.axis_y_m.append(lys)

                self.ploath.canvas.add(Color(*self.ploath.data_line[-1].color))
                y_lines = Line_lis(dash_length=1, dash_offset=1, width=1)
                y_lines.ys = y
                y_lines.xs = x
                self.axis_y_line.append(y_lines)
                self.ploath.canvas.add(y_lines)
                                            # points=[0, y * widget.height * (1 / self.max_y),
                                            #         x * (widget.width * (1 / self.max_x)),
                                            #         y * widget.height * (1 / self.max_y)],
                self.ploath.add_widget(lys)


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

        # print(self.meun)
        if not self.meun:
            # for i in range(0, self.max_x, int(self.max_x / 10)):
            for xint, x_label in zip(self.axis_x, self.axis_x_label):


                # print(xint, yint, x_label, y_label)
                x_label.pos = [x_label.index * (widget.width * (1 / self.max_x)), -30]
                xint.pos = [xint.index * (widget.width * (1 / self.max_x)), 0]


                # lx = Label(text=str(i), size_hint=(None, None), ,
                #            color=(0, 0, 0, 1))
                # lx.bind(texture_size=lx.setter("size"))
                # self.ploath.add_widget(lx)
                # self.ploath.canvas.add(Color(0, 0, 0))
                # self.ploath.canvas.add(Rectangle(size=[2, 10], ))
            for yint, y_label in zip(self.axis_y, self.axis_y_label):
                y_label.pos=[-30, y_label.index * (widget.height * (1 / self.max_y))]
                yint.pos = [0, yint.index * (widget.height * (1 / self.max_y))]

        else:

            # print(123)
            # print(self.axis_x_m)
            # print(self.axis_x_line)
            # print(self.axis_y_m)
            # print(self.axis_y_line)
            for x_label,x_line,y_label,y_line in zip(self.axis_x_m, self.axis_x_line,self.axis_y_m, self.axis_y_line):
                x_label.pos=[x_label.xs * (widget.width * (1 / self.max_x)), -30]
                # print(self.meun)
                # print(x_label.pos)
                # print(x_label)
                # lxs.bind(texture_size=lxs.setter("size"))
                # self.ploath.add_widget(lxs)

                x_line.points=[x_line.xs * (widget.width * (1 / self.max_x)), 0,
                        x_line.xs * (widget.width * (1 / self.max_x)),
                        x_line.ys * widget.height * (1 / self.max_y)]

                # lys = Label(text=str(y), size_hint=(None, None), ,
                #             color=i.color)
                y_label.pos=[-30, y_label.ys * (widget.height * (1 / self.max_y))]
                # lys.bind(texture_size=lys.setter("size"))
                # self.ploath.canvas.add(Color(*i.color))
                y_line.points = [0, y_line.ys * widget.height * (1 / self.max_y),
                          y_line.xs * (widget.width * (1 / self.max_x)),
                          y_line.ys * widget.height * (1 / self.max_y)]


#                 self.ploath.canvas.add(Line(dash_length=1, dash_offset=1,
# , width=1))

                # self.ploath.add_widget(lys)

            # for i in range(0, self.max_y, int(self.max_y / 10)):
            #     self.ploath.canvas.add(Color(0, 0, 0))
            #     self.ploath.canvas.add(Rectangle(size=[10, 2], ))
                # lx = Label(text=str(i), size_hint=(None, None), ],
                #            color=(0, 0, 0, 1))
                # lx.bind(texture_size=lx.setter("size"))
                # self.ploath.add_widget(lx)



# if __name__ == '__main__':
#
#
#     body= LineLayout(meun=True)
#     # body = linelayout()
#     body.plot(x_list=[0,1,2,3,4,5,6,7,10],y_list=[1,2,3,4,5,6,7,8,10], color=(0,1,0,1))
#     body.plot(x_list=[0,1,2,3,4,5,6,7,9,10],y_list=[0,10,2,3,56,55,30,44,35,10])
#     body.plot(x_list=[0,1,2,3,4,5,6], y_list=[12,52,23,24,45,66], color=(1,0,0,1),dash = True)
# #
#     from kivy.app import App
#
#
#     class New_App(App):
#         def __init__(self):
#             super().__init__()
#             self.body = Screen()
#             self.body.add_widget(body)
#
#         def build(self):
#             return self.body
#
#
#     New_App().run()


