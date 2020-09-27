import turtle
import easygui
from PIL import Image
import numpy as np
im_dir = easygui.fileopenbox(multiple=False, default='*.jpg', filetypes=["*.jpg", "*.jpeg", "*.png"])
im = Image.open(im_dir)
width, height= im.size
data = np.array(im.getdata())
data= data.reshape(height, width,3).tolist()
turtle.screensize(width,height)
turtle.colormode(255)
turtle.penup()
turtle.setpos(-width//2, height//2)
turtle.delay(0)
for i in range(height):
    turtle.pendown()
    for z in range(width):
        turtle.pencolor(*data[i][z])
        turtle.forward(1)
    turtle.penup()
    turtle.back(width)
    turtle.right(90)
    turtle.forward(1)
    turtle.left(90)

while True:
    pass
