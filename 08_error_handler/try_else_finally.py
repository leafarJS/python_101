def really_smart_divider(x:int, y:int)-> None:
  try:
    #code
    num = x / y
    #print(num) # salida en el else para ver mensaje de exito
  except ZeroDivisionError:
    #do error
    print("Can't divide by zero! Use some other number")
  except TypeError:
    print("Both x & y needs to be numbers.")
  except Exception:
    print(f"Oops, something went wrong: {e}")
  else:
    print("Else: is execute only when try succeds")
    print("printing num...")
    print(num)
  finally:
    print("Finally: always executes irrespective of success or exceptions")




#really_smart_divider(3,0)
#really_smart_divider(3,'a')
really_smart_divider(3,2)
#really_smart_divider(3.5,2)