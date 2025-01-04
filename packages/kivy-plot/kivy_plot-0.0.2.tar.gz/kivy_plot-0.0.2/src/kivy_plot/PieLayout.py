from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle,Ellipse,Color
from kivy.uix.label import Label
from kivy.vector import Vector




"""
    https://pypi.org/project/kivy-plot/0.0.1/
    https://github.com/rcnn-retall/kivy_plot
    
"""


class Ell_widget(Ellipse):
    def __init__(self,**kwargs):
        super().__init__()
class Ple(Screen):
    def __init__(self):
        super().__init__()
        self.size_hint = (None,.9)
        self.pos_hint = {"center_x":.5, "center_y":.5}

class pielayout(Screen):
    def __init__(self,tilte="text1",back=(1,1,1,1),title_size="16sp", **kwargs):
        super().__init__()
        for i in kwargs.items():
            self.__setattr__(*i)
        self.max_lent = 0
        self.data_chen = []
        with self.canvas:
            Color(*back)
            self.rect = Rectangle()
        self.ples = Ple()
        self.add_widget(self.ples)
        self.bind(size = self.bg_updata)
        self.ples.bind(size=self.update)
        self.add_widget(Label(text=tilte, size_hint=(1, .05), pos_hint={"top": 1}, color=(0, 0, 0, 1), font_size=title_size))
        # self.ls_al = BoxLayout(size_hint=(.1,None),pos_hint={"top": 1}, orientation="vertical")
        # self.ls_al.bind(minimum_height=self.ls_al.setter("height"))
        # self.add_widget(self.ls_al)
    def pie(self,y_list, labels, colors, label_font_size = "16sp", proportiona_font_size = "16sp"):
        for data,label,color in zip(y_list,labels,colors):
            # print(data,label,color)
            els = Ell_widget()
            els.label = label
            els.color = color
            els.data = data
            self.data_chen.append(els)
            self.max_lent += data
            self.ples.canvas.add(Color(*color))
            self.ples.canvas.add(els)
        for i in self.data_chen:

            # "%s\n"%i.label
            lx11 = Label(text=i.label, size_hint=(None,None), markup=True, color=(0,0,0,1), font_size=label_font_size)
            lx11.bind(texture_size=lx11.setter("size"))
            self.ples.add_widget(lx11)
            i.lx11 = lx11

            lx22 = Label(text=str(round(i.data/self.max_lent*100,2))+"%", size_hint=(None,None), markup=True, color=(0,0,0,1), font_size=proportiona_font_size)
            lx22.bind(texture_size=lx22.setter("size"))
            self.ples.add_widget(lx22)
            i.lx22 = lx22

    def update(self,widget, size):
        widget.width = size[1]
        sten = 0
        s_pos = 0, (widget.height/4)
        ss_pos = 0,(widget.width/2)
        for i in self.data_chen:
            i.size = widget.size
            i.angle_start = sten
            end = 360*i.data/self.max_lent+sten
            # print(end)
            i.angle_end = end
            radians = (end - sten)/2
            v = Vector(*s_pos)
            epos =v.rotate(-end+radians)
            vs = Vector(*ss_pos)
            epos_ = vs.rotate(-end+(radians))
            i.lx11.pos = epos_ + (widget.width / 2, (widget.height / 2))
            i.lx22.pos = epos+(widget.width/2,widget.height/2) - Vector(i.lx22.width/4,i.lx22.height/4)
            sten = end


    def bg_updata(self,widget, size):
        self.rect.size= size





#
# if __name__ == '__main__':
#     pie = pielayout(pos_hint={"top": 1, "center_x": .5}, size_hint=(1, 1))
#     labels = ['A', 'B', 'C', 'D', "E", "F"]  # 标签
#     sizes = [15, 20, 30, 45, 20, 10]  # 对应的值
#     colors = [(1, 0, 0), (1, .5, .5), (.2, 0, 1), (1, 2, 0), (1, .05, 0.2), (1, .5, .1)]
#     pie.pie(sizes, labels, colors)
#
#     from kivy.app import App
#     a = App()
#     a.build = lambda *args:pie
#     a.run()
