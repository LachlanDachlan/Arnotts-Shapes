def num_check(question):
  error = "Please enter a number between 1 and 200"
  try:
    number = int(input(question))
    if number < 1:
      print(error)
    elif number > 200:
      print(error)
    else:
      return number
  except ValueError:
    print("Enter a number: ").lower()

var = num_check("please enter a number")
