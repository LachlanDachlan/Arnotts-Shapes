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

def ap_checker(question):
  error = "You need to enter a number between 2 and 200"
  while True:
    num_range = int(input(question))
    if num_range in range(2,201):
      print("goooood")
    else:
      print(error)
num = ap_checker("Please enter a number between 2 and 200: ")
