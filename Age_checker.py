def num_check(question):
  while True:
    try:
      response = int(input(question))
      return response
    except ValueError:
      print("Please enter an integer")

tickets_sold = 0

while True:
  name = input("enter a name or input 'xxx' to quit: ")
  if name == "xxx":
    break
  age = num_check("Age: ")
  if 12 <= age <= 120:
    pass
  elif age < 12:
    print("Sorry, you are too young for this movie ")
    continue
  else:
    print("?, can you redo that?")
    continue
  tickets_sold += 1
print("You sold {} tickets".format(tickets_sold))