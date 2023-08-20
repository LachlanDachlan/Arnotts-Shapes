from time import sleep


def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response
    except ValueError:
      print("Please enter an integer")





while True:
  shape = input("Out of the shapes Square, Rectangle, circle and Parallelogram, Which would you like to use?:")
  if shape == "parallelogram":
    print("The minimum value you can use for this shape is 2")
    sleep(0)
    print("The maximum value you can use for this shape is 200")
    sleep(0)
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
    print("The area of this shape is {}".format(parallelogram_area))

  if shape == "square":
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
    print("The area of this shape is {}".format(square_area))

  if shape == "circle":
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
    print("The are of this shape is {}".format(circle_area))

  if shape == "rectangle":
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
    print("The area of this shape is {}".format(rectangle_area))
  
  
    
    
    