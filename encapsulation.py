class Human():
  def __init__(self):
    self.__distance = 5.4
    
  def walk(self):
    print "The man walked",self.__distance,"kms"
    
  def setdistance(self,dist):
    self.__distance = dist
    

h = Human()
h.walk()
h.__distance = 2
h.walk()
h.setdistance(3)
h.walk()
