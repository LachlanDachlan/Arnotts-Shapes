def shape_checker(question):
  while True:
    response = input(question).lower()
    if response == "":
      print("Please enter a shape from the list")
    else:
      return response



shape = shape_checker("Out of the shapes Square, Rectangle, circle and Parallelogram, Which would you like to use?: ").lower()
while True:
  if shape == "square":
    print("Alright, shouldn't be to hard to calculate")
    break
  elif shape == "rectangle":
    print("Interesting choice")
    break
  elif shape == "circle":
    print("Might be a little difficult but I will try")
    break
  elif shape == "parallelogram":
    print("Ah ok")
    break
  else:
    shape = shape_checker("please answer from the list: ")


    