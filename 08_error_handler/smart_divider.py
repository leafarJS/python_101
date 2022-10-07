def smart_divider(x:int, y:int)-> None:
  try:
    #code
    num = x / y
    print(num)
  except ZeroDivisionError:
    #do error
    print("Can't divide by zero! Use some other number")

