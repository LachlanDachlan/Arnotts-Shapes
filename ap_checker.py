def ap_checker(question):
  error = "You need to enter a number between 2 and 200"
  valid = False
  while not valid:
    try:
      num_range = int(input(question))
      if num_range in range(2,201):
        print("alright")
        
      else:
        valid = False
    
    except ValueError:
      print(error)

num = ap_checker("Please enter a number between 2 and 200: ")

      