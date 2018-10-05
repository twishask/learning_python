class Grapes:
  def color(self):
    print "This fruit is green in color"

class Apple:
  def color(self):
    print "This fruit is red in color"
  
def identify_color(fruit):
  fruit.color()
  
fruit1 = Grapes()
fruit2 = Apple()

identify_color(fruit1)
identify_color(fruit2)
