def yes_no(question):
  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response  == "n":
      return "no"
    else:
      print("Please answer yes or no")

want_instructions = yes_no("Do you want to read the instructions?: ").lower()
if want_instructions == "yes":
  print("")
  print("")
  print("")
  print("")
  