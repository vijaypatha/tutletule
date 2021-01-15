# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.pensize(10)

# timmy.forward(100)

# 1. Turtle Square

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)

# 2. Dashed line
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# 3. Shapes with Random Colors
import  random
# timmy.pensize(10)
# colors = ["CornflowerBlue", "IndianRed", "DeepSkyBlue", "Coral", "Black", "lime green", "light coral", "magenta"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(n)

# 4. Random Walk
# import  random
# direction = [0, 90, 180, 270]
# colors = ["CornflowerBlue", "IndianRed", "DeepSkyBlue", "Coral", "Black", "lime green", "light coral", "magenta"]
# for rand in range(200):
#     timmy.color(random.choice(colors))
#     timmy.forward(50)
#     timmy.setheading(random.choice(direction))

# 5. Random Walk with random color.

# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# direction = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))



#6. Circle

# import turtle as t
#
# tim = t.Turtle()
# tim.shape('turtle')
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# def draw_spirograph(size_of_gap):
#     for circle in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(10)

#7 Hirst SPOT PAINT


# import colorgram
#
# colors = colorgram.extract('spot_paint.jpg', 30)
# print(colors)
#
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]



tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()


















