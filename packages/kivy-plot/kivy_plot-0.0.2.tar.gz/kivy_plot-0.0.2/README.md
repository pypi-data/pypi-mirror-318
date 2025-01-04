# kivy_plot
A drawing library based entirely on kivy implementation

1. ### LineLayout

   + ##### 演示代码

     ![image-20250103162050837](https://github.com/rcnn-retall/kivy_plot/blob/main/IMAGE/image-20250103162050837.png)

     ```python
     body = linelayout(meun=True)
     body.plot(x_list=[0,1,2,3,4,5,6],y_list=[12,52,34,43,50,61,24], color=(0,1,0,1))
     body.plot(x_list=[0, 1, 2, 3, 4, 5, 6], y_list=[11, 42, 33, 42, 54, 6, 25])
     ```


   + ##### title(string)

        图表的标题或者名字

   + ##### meun(Boole)

     + True:增加辅助虚线
     + Flase:没有辅助虚线

   + ##### size_hint(tuple)

      + width:比例宽度
      + height:比例高度
      + size(也可以使用)

   + ##### back(list)

      + 图表背景颜色（RBGA）

   + ##### x_name(string)

      + x轴的名字

   + ##### y_name(string)

      + y轴名字

   + ##### pos(tuple)

      + x:x坐标
      + y:y坐标
      + pos_hint(可以使用)

   + ##### del_axis(method)

      + axis:删除图表脊骨
        + axis_left (string)
        + axis_right(string)
        + axis_top(string)
        + axis_bottom(string)


   + ##### plot(method)

        + 添加折线数据
          + x_list:x轴数据列表（list）
          + y_list:y轴数据列表  (list)
          + color:折线颜色,默认黑色
          + width：折线粗细

2. ### HistLayout

   + ##### 演示代码

     ![image-20250103200330289](https://github.com/rcnn-retall/kivy_plot/blob/main/IMAGE/image-20250103200330289.png)

     ```python
     body = histlayout()
     body.bar(["iewv", "lls","llos"], [20,20,420], color=(0,1,0,1))
     body.bar(["iewv", "lls", "llos"], [50, 220, 420],color=(0,0,.2,1))
     body.bar(["iewv", "lls", "llos"], [20, 220, 210], color=(.2, 0, .2, 1))
     body.bar(["iewvs", "xx"], [280,204],color=(1,0,.5,1))
     body.bar(["iewvs", "xx"], [280, 204], color=(1, .5, .5, 1))
     body.bar(["iewvsok","235"],[150,253] )
     ```

     

   + ##### title(string)

     + 图表的标题或者名字

   + ##### size_hint(tuple)

     + width:比例宽度
     + height:比例高度
     + size(也可以使用)

   + ##### back(list)

     + 图表背景颜色（RBGA）

   + ##### x_name(string)

     + x轴的名字

   + ##### y_name(string)

     + y轴名字

   + ##### pos(tuple)

     + x:x坐标
     + y:y坐标
     + pos_hint(可以使用)

   + ##### del_axis(method)

     + axis:删除图表脊骨
       + axis_left (string)
       + axis_right(string)
       + axis_top(string)
       + axis_bottom(string)

   + ##### bar(method)

     + index:x轴名字（list)
     + y_list:数值列表（list)
     + meun=False(暂无)
     + color:圆柱颜色

3. ### PieLayout

   + ##### 演示代码

     ![image-20250104152100611](https://github.com/rcnn-retall/kivy_plot/blob/main/IMAGE/image-20250104152100611.png)

     ```python
     pie = pielayout(pos_hint={"top": 1, "center_x": .5}, size_hint=(1, 1)) labels = ['A', 'B', 'C', 'D', "E", "F"]  # 标签
     sizes = [15, 20, 30, 45, 20, 10]  # 对应的值
     colors = [(1, 0, 0), (1, .5, .5), (.2, 0, 1), (1, 2, 0), (1, .05, 0.2), (1, .5, .1)]
     pie.pie(sizes, labels, colors)
     ```

   + ##### title(string)

     + 图表的标题或者名字

   + ##### size_hint(tuple)

     + width:比例宽度(图表长宽尽量相等， 高度决定着饼图的大小。禁止宽度大于高度)
     + height:比例高度
     + size(也可以使用)

   + ##### back(list)

     + 图表背景颜色（RBGA，默认等于（1，1，1，1））

   + ##### title_size（string)

     + 标题字体大小

   + ##### pie(method)

     + y_list:图像数据(list)
     + labels:图像类别名字(list)
     + colors:图像着色列表（list)
     + label_font_size: 标签字体大小
     + proportiona_font_size：比例字体大小
