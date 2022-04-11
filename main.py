import turtle
import random

turtle.bgcolor('black')
myTurtle = turtle.Turtle()

colourList = ['#ff0000','#ff00ff','#00ff00','#0000ff','#ffffff','#ffff00','#00ffff']

for n in range(18):
  randomColour = random.randint(0, len(colourList) - 1)
  randomSides = random.randint(3, 8)
  randomSize = random.randint(50, 200)
  myTurtle.color(colourList[randomColour])
  for i in range(randomSides):
    myTurtle.forward(randomSize)
    myTurtle.left(360/randomSides)
  myTurtle.left(20)
