#enables sleep statements
from time import sleep
# a statement that makes sure you can only answer a yes or no question with yes or no  
def yes_no(question):
  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response  == "n":
      return "no"
    else:
      print("Sorry, that isn't a valid response. Please answer with yes or no")

# a statement that ensures you can only input numbers when needed
def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response
    except ValueError:
      print("Please enter an integer")

# a statement that ensures you can only answer from a list of shapes 
def shape_checker(question):
  while True:
    response = input(question).lower()
    if response == "":
      print("Please enter a shape from the list")
    else:
      return response
# a statement that gives users units of measurement to choose from
def unit(question):
  error = "you have not selected the avalible units:"
  valid = False
  while not valid:
    unit = input(question).lower().strip()
    if unit == "meters" or unit == "m":
      unit = "meters"
      return unit
    elif unit == "centimeters" or unit == "cm":
      unit = "centimeters"
      return unit
    elif unit == "millimeters" or unit == "mm":
      unit = "millimeters"
      return unit
    else:
      print(error)



# Displays instructions if yes, skips if no
want_instructions = yes_no("Do you want to read the instructions?: ").lower()
if want_instructions == "yes":
  #the instructions
  print("This program will give you a variety of shapes to choose from")
  sleep(4)
  print("For whatever shape you choose, you will find the values for it's height")
  print("and width, to find the Area or Perimeter")
  sleep(4)
  print("The shapes you will be choosing from will be")
  print("Square, Rectangle, circle and Parallelogram")
  sleep(4)
  print("Now time to begin")
  sleep(4)
if want_instructions == "no":
  print("Ok")
  sleep(0)
#Asks which unit of measurement the user wants  
measure = unit("What unit of measurement would you like to use: ")
#Asks what the user wants calculated
area_perimeter = input("Would you like to calculate the area or the perimeter?: ")
if area_perimeter == "area" or area_perimeter == "a":
  #asks for the shape they want, where shape checker is used
  shape = shape_checker("Out of the shapes Square, Rectangle, circle and Parallelogram, Which would you like to use?: ").lower()
  while True:
    if shape == "square":
      print("Alright, shouldn't be to hard to calculate")
      #gives the number range for users to follow
      print("The minimum value you can use for this shape is 2")
      sleep(4)
      print("The maximum value you can use for this shape is 200")
      sleep(4)
      #asks for a number input (num_checker)
      side = num_check("what value would you like to use for the sides: ")
      #ensures that users can only choose from the given range
      if side < 2:
        print("please enter a value higher than 2")
      elif side > 200:
        print("please enter a value lower than 200")
        #the calculation for the square's area
      square_area = side * side
      print("The area of this shape is {} {}".format(square_area, unit))
      break
    elif shape == "rectangle":
      print("ahh yes")
      #gives the number range for users to follow
      print("The minimum value you can use for this shape is 2")
      sleep(4)
      print("The maximum value you can use for this shape is 200")
      sleep(4)
      #asks for number input (num_checker)
      width = num_check("what value would you like to use for the width: ")
      length = num_check("what value would you like to use for the length: ")
      #ensures that users can only answer from the given range
      if width < 2:
        print("please enter a value higher than 2")
      elif width > 200:
        print("please enter a value lower than 200")

      #ensures that users can only answer from the given range
      if length < 2:
        print("please enter a value higher than 2")
      elif length > 200:
        print("please enter a value lower than 200")
      #calculates the area of the rectangle with the users inputs  
      rectangle_area = width * length
      print("The area of this shape is {} {}".format(rectangle_area, unit))
      break
    elif shape == "circle":
      print("Might be a little difficult but I will try")
      #gives the number range
      print("The minimum value you can use for this shape is 2")
      sleep(4)
      print("The maximum value you can use for this shape is 200")
      sleep(4)
      #asks for a number input (num_checker)
      radius = num_check("what value would you like to use for the radius: ")
      #ensures the user can only pick from the range
      if radius < 2:
        print("please enter a value higher than 2")
      elif radius > 200:
        print("please enter a value lower than 200")
      #calculates the circles area
      circle_area = 3.14 * (radius * radius)
      print("The are of this shape is {} {}".format(circle_area, unit))
      break
    elif shape == "parallelogram":
      print("Ah ok")
      #gives the user the number range
      print("The minimum value you can use for this shape is 2")
      sleep(4)
      print("The maximum value you can use for this shape is 200")
      sleep(4)
      #asks for a number input (num_checker)
      base = num_check("What value would you like to use for the base: ")
      height = num_check("What value would you like to use for the height: ")
      if height < 2:
        print("please enter a value higher than 2")
      elif height > 200:
        print("please enter a value lower than 200")
      #asks for a number input (num_checker)
      if base < 2:
        print("please enter a value higher than 2")
      elif base > 200:
        print("please enter a value lower than 200")
      #calculates area with the users inputs
      parallelogram_area = base * height
      print("The area of this shape is {} {}".format(parallelogram_area, unit))
      break
  else:
    shape = shape_checker("please answer from the list: ")
#
elif area_perimeter == "perimeter" or area_perimeter == "p":
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
      square_peri = 4 * side
      print("The perimeter of this shape is {} {}".format(square_peri, unit))
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
      rectangle_peri = 2 * (width * length)
      print("The perimeter of this shape is {} {}".format(rectangle_peri, unit))
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
      circle_peri = (3.14 * 2) * radius
      print("The are of this shape is {} {}".format(circle_peri, unit))
      break
    elif shape == "parallelogram":
      print("Ah ok")
      print("The minimum value you can use for this shape is 2")
      sleep(4)
      print("The maximum value you can use for this shape is 200")
      sleep(4)
      base = num_check("What value would you like to use for the base: ")
      side = num_check("What value would you like to use for the sides: ")
      if side < 2:
        print("please enter a value higher than 2")
      elif side > 200:
        print("please enter a value lower than 200")

      if base < 2:
        print("please enter a value higher than 2")
      elif base > 200:
        print("please enter a value lower than 200")
      parallelogram_peri = 2 * (base * side)
      print("The perimeter of this shape is {} {}".format(parallelogram_peri, unit))
      break


  
