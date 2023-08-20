def not_blank(question):

  while True:
    response = input(question)
    if response == "":
      print("Please input a name ")
    else:
      return response
while True:  
  name = not_blank("Please input your name or write 'xxx' to quit: ")
  if name == 'xxx':
    break
  