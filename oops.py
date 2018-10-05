class Rectangle:
  sides = 4
  
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth
  
  def perimeter(self):
    self.perimeter = 2 * (self.length + self.breadth)
    return self.perimeter
    
  def area(self):
    self.area = self.length * self.breadth
    return "The area is {}".format(self.area)
    
l = input("Length:")
b = input("Breadth:")
r = Rectangle(l,b)
print r.perimeter()
print r.area()
