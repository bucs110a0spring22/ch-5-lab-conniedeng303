'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random

def setupWindow(wn=None):
  wn.setworldcoordinates(-1,-1,1,1)

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.reset()
  myturtle.penup()
  myturtle.goto(-1,-1)
  myturtle.pendown()
  myturtle.goto(top_left_x+width,top_left_y) 
  myturtle.goto(top_left_x+width,top_left_y+width)
  myturtle.goto(top_left_x,top_left_y+width)
  myturtle.goto(top_left_x,top_left_y)
  myturtle.penup()
  
def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.penup()
  myturtle.goto(x_start,y_start)
  if (x_start == 0):
    myturtle.setheading(90)
  else:
    myturtle.setheading(0)
  myturtle.pendown()
  myturtle.forward(2)
  myturtle.penup()
  # dart.goto(y_start,y_end)
  
def drawCircle(myturtle=None, radius=0):
  myturtle.penup()
  myturtle.goto(0,-1)
  myturtle.pendown()
  myturtle.circle(radius)
  myturtle.penup()

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  if myturtle.distance(circle_center_x,circle_center_y) <= radius:
    myturtle.pendown()
    myturtle.dot(3, "blue")
    myturtle.penup()
    return True
  else:
    myturtle.pendown()
    myturtle.dot(3, "red")
    myturtle.penup()
    return False

def setUpDartboard(myscreen=None,myturtle=None):
  setupWindow(myscreen)
  drawSquare(myturtle,width=2, top_left_x=-1, top_left_y=-1)
  drawCircle(myturtle, radius=1)
  drawLine(myturtle, x_start=-1, y_start=0, x_end=0, y_end=0)
  drawLine(myturtle, x_start=0, y_start=-1, x_end=0, y_end=1)
#throwdart: 
  
def throwDart(myturtle=None):
  myturtle.goto(random.uniform(-1,1),random.uniform(-1,1))
  isInCircle(myturtle,0,0,1)
  myturtle.penup()

def playDarts(myturtle=None):
  player1_score = 0  #odd
  player2_score = 0  #even
  for i in range(10):
    throwDart(myturtle)
    if (i%2 == 1) and isInCircle(myturtle,0,0,1) == True:
      player1_score += 1
    if (i%2 == 0) and isInCircle(myturtle,0,0,1) == True:
      player2_score += 1
  print("Player 1 score: " ,player1_score)
  print("Player 2 score: " ,player2_score)
  if player1_score < player2_score:
    print("player2 wins!")
  elif player1_score > player2_score:
    print("player1 wins!")
  else:
    print("Tie")

#PART C 
def montePi(myturtle=None, number_darts=0):
  inside_count = 0
  for i in range(number_darts):
    throwDart(myturtle)
    if isInCircle(myturtle,0,0,1) == True:
      inside_count += 1
  return (inside_count/number_darts)*4
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
