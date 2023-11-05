#imports time module
import time
# creates multiple inputs as variables
inp = input("Enter a number: ")
xsgv = input(f"your number is {str(inp)}, y/n: ")

if inp is isinstance(inp, int):
  # checks if the input is "y"
  if xsgv == "y":
    global x
    print("I thought so")
    x= "I was right!"
  # if the input is not y...
  else:
    print("your lying!")
    x= "your lying!"
  # creates  small function called x
  x = f"so your number was {str(inp)}, and {x}"
  time.sleep(1)
  print(x)
elif xsgv is isinstance(xsgv, str):
  if xsgv == "y":
    print("I thought so")
    x= "I was right!"
  # if the input is not y...
  else:
    print("your lying!")
    x= "your lying!"
  # creates  small function called x
  x = f"so your number was {str(inp)}, and {x}"
  time.sleep(1)
  print(x)