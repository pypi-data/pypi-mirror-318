from kivy.graphics import Color, Line, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


"""
body = Histogram()
body.bar(["iewv", "lls","llos"], [20,20,420], color=(0,1,0,1))
body.bar(["iewv", "lls", "llos"], [50, 220, 420],color=(0,0,.2,1))
body.bar(["iewv", "lls", "llos"], [20, 220, 210], color=(.2, 0, .2, 1))
body.bar(["iewvs", "xx"], [280,204],color=(1,0,.5,1))
body.bar(["iewvs", "xx"], [280, 204], color=(1, .5, .5, 1))
body.bar(["iewvsok","235"],[150,253] )
"""

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

class RctHight(Rectangle):
    def __init__(self, **kwargs):
        super().__init__()
        for i in kwargs.items():
            self.__setattr__(*i)

class Histogram(Screen):
    def __init__(self,title="text_1",back=(1,1,1,1),x_name="",y_name="",**kwargs):
        super().__init__()
        self.back = back
        for i in kwargs.items():
            self.__setattr__(*i)
        self.lable_list = {}
        self.titless = Label(text=title, size_hint=(.8, .05), pos_hint={"top":1, "x":.1}, color=(0,0,0,1), font_size="18sp")
        self.add_widget(self.titless)
        self.ploath = Polyline()
        self.add_widget(self.ploath)
        self.ploath.bind(size=self.update)
        self.max_y = 10
        self.bar_data = {}

        self.bind(size=self.update_background)
        # self.bind(pos=self.update)
        self.y_name = Label(text=y_name, size_hint=(None, None), pos_hint={"x":0, "center_y":.5}, color=(0,0,0,1))
        self.y_name.bind(texture_size=self.y_name.setter("size"))
        self.add_widget(self.y_name)

        self.x_name = Label(text=x_name, size_hint=(None, None), pos_hint={"center_x":.5, "y":0}, color=(0,0,0,1))
        self.x_name.bind(texture_size=self.x_name.setter("size"))
        self.add_widget(self.x_name)

        with self.canvas.before:
            Color(*self.back)
            self.rects = Rectangle()
    def del_axis(self, axis):

        self.ploath.canvas.remove(getattr(self.ploath, axis))
    def update_background(self, widget,size):
        self.rects.size=widget.size
    def bar(self, index, y_list, meun=False,color=(0,0,0,1)):

        self.max_y = self.max_y if self.max_y > max(y_list) else max(y_list)

        for i in zip(index, y_list):
            rects = RctHight(name=i[0], y_list=i[1])
            self.ploath.canvas.add(Color(*color))
            self.ploath.canvas.add(rects)

            if i[0] in self.bar_data:
                self.bar_data[i[0]].append(rects)
            else:
                l1 = Label(text=str(i[0]), color=(0,0,0,1), size_hint=(None,None))
                l1.bind(texture_size=l1.setter("size"))
                self.ploath.add_widget(l1)
                self.lable_list[i[0]]=l1
                self.bar_data[i[0]] = []
                self.bar_data[i[0]].append(rects)

        # print(self.bar_data)
    def update(self,widget,size):
        widget.axis_left.points=[0,0,0,size[1]]
        widget.axis_right.points=[size[0],size[1],size[0],0]
        widget.axis_top.points=[size[0],size[1],0,size[1]]
        widget.axis_bottom.points=[0,0,size[0],0]

        whif = widget.width /len(self.bar_data)
        whifs = (widget.height /len(self.bar_data)) -(widget.height*0.05)
        for pos,j in enumerate(self.bar_data):
            pos = pos*whif+whif/2
            # l1 = Label(text=str(j), pos=(pos,-30), color=(0,0,0,1), size_hint=(None,None))
            # l1.bind(texture_size=l1.setter("size"))
            # self.ploath.add_widget(l1)
            self.lable_list[j].pos = pos,-30
            print(self.lable_list[j].width)
            print(self.lable_list[j].pos)
            list_all = len(self.bar_data[j])
            for index,i in enumerate(self.bar_data[j]):
                # print(i)
                # print(list_all)
                # print(pos+(index*whif))
                # i.pos=pos+(index*(whif+100/2)),0

                # i.pos = i.size[0]
                # i.pos = index*((whif/list_all) - (pos-(whif/2)))+whif/2,0

                i.size = whifs/list_all, i.y_list*(widget.height*(.95/self.max_y))
                i.pos =(pos-(whifs/2))+ (index*(whifs/list_all)),0

            for i in range(0, self.max_y, int(self.max_y / 10)):
                self.ploath.canvas.add(Color(0, 0, 0))
                self.ploath.canvas.add(Rectangle(size=[10, 2], pos=[0, i * (widget.height * (1 / self.max_y))]))
                lx = Label(text=str(i), size_hint=(None, None), pos=[-30, i * (widget.height * (1 / self.max_y))],
                           color=(0, 0, 0, 1))
                lx.bind(texture_size=lx.setter("size"))
                self.ploath.add_widget(lx)




# #
# from kivy.app import App
#
# class Clist(App):
#     def build(self):
#         self.body = Histogram()
#         self.body.bar(["iewv", "lls","llos"], [20,20,420], color=(0,1,0,1))
#         self.body.bar(["iewv", "lls", "llos"], [50, 220, 420],color=(0,0,.2,1))
#         self.body.bar(["iewv", "lls", "llos"], [20, 220, 210], color=(.2, 0, .2, 1))
#         self.body.bar(["iewvs", "xx"], [280,204],color=(1,0,.5,1))
#         self.body.bar(["iewvs", "xx"], [280, 204], color=(1, .5, .5, 1))
#         self.body.bar(["iewvsok","235"],[150,253] )
#         # self.body.bar(["iewv", "lls", "llos"], [20, 220, 20], color=(.2, 0, .2, 1))
#
#
#         # self.body.del_axis("axis_left")
#
#         return self.body
#
#
# Clist().run()