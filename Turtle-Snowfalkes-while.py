import turtle
import random
melissa=turtle.Turtle()

turtle.Screen().bgcolor("blue2")
colours=["cyan","purple","red","gold2"]
melissa.color("gold2")
melissa.penup()
melissa.forward(90)
melissa.left(45)
melissa.pendown()

def branch():
  count1 = 0
  while count1 < 10:
      count2 = 0
      while count2 < 2:
          melissa.forward(30)
          melissa.backward(30)
          melissa.right(45)
          count2 += 1
      melissa.left(90)
      melissa.backward(30)
      melissa.left(45)
      count1 += 1
  melissa.right(90)
  melissa.forward(90)



i = 0
while i < 8:
    branch()
    melissa.left(45)
    i += 1


# melissa.color(random.choice(colours))

