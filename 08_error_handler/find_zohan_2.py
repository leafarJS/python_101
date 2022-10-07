def find_zohan(name:str)->None:
  friends: list[str] = ["cece", "coco", "caca", "cucu"]
  
  if name not in friends:
    raise ValueError(f"{name} NOT Fount!!!")
  else:
    print(f"Found {name}")

find_zohan("coco")
find_zohan("caco")