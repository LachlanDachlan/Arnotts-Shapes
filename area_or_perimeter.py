def a_or_p(question):
  error = "Please enter one of the two"
  while True:
    a_or_p = input(question)
    if a_or_p == "area" or a_or_p == "a":
      print("so its area")
      return a_or_p
    elif a_or_p == "perimeter" or a_or_p == "p":
      print("so its perimeter")
      return a_or_p
    else:
      print(error)

yeah = a_or_p("Please enter area or perimeter: ")
  