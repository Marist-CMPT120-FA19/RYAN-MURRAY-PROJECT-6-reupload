#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from graphics import *

win= GraphWin("Traffic_light" , 500, 500)

def draw_light_body(x, y, length, width):
    body=Rectangle (Point(x,y), Point(length, width))
    body.setOutline("black")
    body.setFill("white")
    body.draw(win)

def draw_lamp(color, a, b, radius):
    lamp = Circle(Point(a,b), radius)
    lamp.setOutline("black")
    lamp.setFill(color)
    lamp.setWidth(3)
    lamp.draw(win)

def draw_traffic_light(x, y):
    draw_light_body(x,y,90, 153)
    draw_lamp("red", 60,35,20)
    draw_lamp("yellow", 60,82,20)
    draw_lamp("green", 60,128, 20)

draw_traffic_light(30,10)


# In[ ]:




