from time import sleep
# code that makes sure you can only answer a yes or no question with yes or no  
def yes_no(question):
  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response  == "n":
      return "no"
    else:
      print("Sorry, that isn't a valid response. Please answer with yes or no")


def not_blank(question):

  while True:
    response = input(question)
    if response == "":
      print("Please input a name ")
    else:
      return response

def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response
    except ValueError:
      print("Please enter an integer")

def shape_checker(question):
  while True:
    response = input(question).lower()
    if response == "":
      print("Please enter a shape from the list")
    else:
      return response




want_instructions = yes_no("Do you want to read the instructions?: ").lower()
if want_instructions == "yes":
  print("This program will give you a variety of shapes to choose from")
  sleep(4)
  print("For whatever shape you choose, you will find the values for it's height")
  print("width, Area and Perimeter")
  sleep(4)
  print("The shapes you will be choosing from will be")
  print("Square, Rectangle, circle and Parallelogram")
  sleep(4)
  print("Now time to begin")
  sleep(4)
if want_instructions == "no":
  print("Ok")
  sleep(0)

shape = shape_checker("Out of the shapes Square, Rectangle, circle and Parallelogram, Which would you like to use?: ").lower()
while True:
  if shape == "square":
    print("Alright, shouldn't be to hard to calculate")
    print("The minimum value you can use for this shape is 2")
    sleep(4)
    print("The maximum value you can use for this shape is 200")
    sleep(4)
    side = num_check("what value would you like to use for the sides: ")
    if side < 2:
      print("please enter a value higher than 2")
    elif side > 200:
      print("please enter a value lower than 200")
    square_area = side * side
    print("The area of this shape is {} cm".format(square_area))
    break
  elif shape == "rectangle":
    print("Interesting choice")
    print("The minimum value you can use for this shape is 2")
    sleep(4)
    print("The maximum value you can use for this shape is 200")
    sleep(4)
    width = num_check("what value would you like to use for the width: ")
    length = num_check("what value would you like to use for the length: ")
    if width < 2:
      print("please enter a value higher than 2")
    elif width > 200:
      print("please enter a value lower than 200")

    if length < 2:
      print("please enter a value higher than 2")
    elif length > 200:
      print("please enter a value lower than 200")
    rectangle_area = width * length
    print("The area of this shape is {} cm".format(rectangle_area))
    break
  elif shape == "circle":
    print("Might be a little difficult but I will try")
    print("The minimum value you can use for this shape is 2")
    sleep(4)
    print("The maximum value you can use for this shape is 200")
    sleep(4)
    radius = num_check("what value would you like to use for the radius: ")
    if radius < 2:
      print("please enter a value higher than 2")
    elif radius > 200:
      print("please enter a value lower than 200")
    circle_area = 3.14 * (radius * radius)
    print("The are of this shape is {} cm".format(circle_area))
    break
  elif shape == "parallelogram":
    print("Ah ok")
    print("The minimum value you can use for this shape is 2")
    sleep(4)
    print("The maximum value you can use for this shape is 200")
    sleep(4)
    base = num_check("What value would you like to use for the base: ")
    height = num_check("What value would you like to use for the height: ")
    if height < 2:
      print("please enter a value higher than 2")
    elif height > 200:
      print("please enter a value lower than 200")

    if base < 2:
      print("please enter a value higher than 2")
    elif base > 200:
      print("please enter a value lower than 200")
    parallelogram_area = base * height
    print("The area of this shape is {} cm".format(parallelogram_area))
    break
  else:
    shape = shape_checker("please answer from the list: ")


