def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response
    except ValueError:
      print("Please enter an integer")



while True:
  name = input("enter a name or input 'xxx' to quit: ")
  if name == "xxx":
    break
  age = num_check("Age: ")
  if 12 <= age <= 120:
    pass
  elif age < 12:
    print("Sorry, you are too young to use this program ")
    continue
  else:
    print("?, can you redo that?")
