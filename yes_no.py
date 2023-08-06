while True:
  yes_no = input("Would you like to read the instructions?")
  if yes_no == "yes" or yes_no == "y":
    print("Instructions go here")
  elif yes_no == "no" or yes_no == "n":
    print("ok lets begin")
  else:
    print("Sorry, that isn't a valid response. Please answer with yes or no")