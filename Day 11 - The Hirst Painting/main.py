import turtle as turtle_module
import random

turtle_module.colormode(255)
tim=turtle_module.Turtle()
color_list=[(223, 232, 226), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (128, 189, 143), (83, 20, 44), (37, 42, 67), (186, 93, 106), (186, 140, 171), (84, 122, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91), (194, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (57, 130, 122), (217, 176, 188), (220, 182, 167), (166, 207, 164)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range (1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen=turtle_module.Screen()
screen.exitonclick()



























# from turtle import Turtle , Screen

# timmy_the_turtle=Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)


# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# import turtle as t
# import random
# tim=t.Turtle()
# t.colormode(255)

# colours=["medium aquamarine", "pale goldenrod","dark slate gray","tomato","sienna","slate blue","dim gray"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# directions=[0,90, 180, 270]
#
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


#
# def random_color():
#     r=random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     color=(r,g,b)
#     return random_color()
#
# tim.speed("fastest")
#
# def draw_spiroghaph(size_of_gap):
#
#     for _ in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading()+size_of_gap)
#
# draw_spiroghaph(5)
#
#
#
#
#
#
#
#
#
#
#
#
#
# screen=t.Screen()
# screen.exitonclick()


# import colorgram

# rgb_colors=[]
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)




















