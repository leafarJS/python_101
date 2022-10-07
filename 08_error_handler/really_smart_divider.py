def really_smart_divider(x:int, y:int)-> None:
  try:
    #code
    num = x / y
    print(num)
  except ZeroDivisionError:
    #do error
    print("Can't divide by zero! Use some other number")
  except TypeError:
    print("Both x & y needs to be numbers.")
  except Exception:
    print(f"Oops, something went wrong: {e}")
    
really_smart_divider(3,0)
really_smart_divider(3,'a')
really_smart_divider(3,2)
really_smart_divider(3.5,2)