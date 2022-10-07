def find_zohan(name:str)->None:
  friends: list[str] = ["cece", "coco", "caca", "cucu"]
  try:
    assert name in friends
  except AssertionError:
    print(f"{name} not found!")
  else:
    print(f"Found {name}")
  finally:
    print("Goodbye!!!")


find_zohan("coco")
find_zohan("caco")