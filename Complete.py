from time import sleep
# 
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

want_instructions = yes_no("Do you want to read the instructions?: ").lower()
if want_instructions == "yes":
  print("This program will give you a variety of shapes to choose from")
  sleep(4)
  print("For whatever shape you choose, you will find the values for it's height")
  print("width, Area and Perimeter")
  sleep(4)
  print("The shapes you will be choosing from will be")
  print("Square, Rectangle, Triangle and Circle")
  sleep(4)
  print("Now time to begin")
  sleep(4)
if want_instructions == "no":
  print("Ok")
  
  