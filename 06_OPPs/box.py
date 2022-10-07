from __future__ import annotations


class Box:
    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b
        
    @property
    def area(self) -> int:
        return self.side_a * self.side_b
      

    def __repr__(self) -> str:
        return "<class 'Box'>"

    def __str__(self) -> str:
        return f"Box => Side A: {self.side_a}, Side B: {self.side_b}"

    def __contains__(self, num: object) -> bool:
        """Use `in` operator"""
        if not isinstance(num, int):
            raise NotImplementedError
        return num in [self.side_a, self.side_b]

    def __eq__(self, other: object) -> bool:
        """Checks if two Boxes are equal"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.side_a == other.side_a and self.side_b == other.side_b
      
    def __lt__(self, other: object) -> bool:
        """Checks if the other box is smaller"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area < other.area
      
    def __le__(self, other: object) -> bool:
        """Checks if the other box is smaller"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area <= other.area  
      
    def __add__(self, other: object) -> int:
        """adds two boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area + other.area  
      
    def __sub__(self, other: object) -> int:
        """sub two boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area - other.area 
      
    def __mul__(self, other: object) -> int:
        """multiples two boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area * other.area  
      
    def __truediv__(self, other: object) -> float:
        """multiples two boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area / other.area 
      
    def __floordiv__(self, other: object) -> float:
        """multiples two boxes"""
        if not isinstance(other, Box):
            return NotImplemented
        return self.area // other.area   
#==============================================

box1 = Box(3,4)
box2 = Box(5,7)

print(box1)
print(box2)

print("*-" *10)
print(box1 == box2)
print(box1 <= box2)
print(box1 < box2)
print(box1 >= box2)
print(box1 > box2)
print("*-" *10)

print(3 in box1)
print(4 in box1)
#print("a" in box1)
print("*-" *10)
print(box1 + box2)
print(box1 - box2)
print(box1 * box2)
print(box1 / box2)
print(box1 // box2)
print("*-" *10)
