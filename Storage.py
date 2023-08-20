def shape_checker(question):
  while True:
    response = input(question).lower
    if response == "":
      print("Please enter a shape from the list")
    else:
      return response


shape = input("Out of the shapes Square, Rectangle, circle and Parallelogram, Which would you like to use?: ").lower
while True:
  if shape == "square":
    print("Alright, shouldn't be to hard to calculate")
  elif shape == "rectangle":
    print("Interesting choice")
  elif shape == "circle":
    print("Might be a little difficult but I will try")
  elif shape == "Parallelogram":
    print("Ah ok")
  else:
    print("please answer from the list")
