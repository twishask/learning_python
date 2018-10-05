class Department(object):
  
  def __init__(self,hod):
    self.hod = hod
    print self.hod,"is the head of the department"

  def subjects(self):
    print "There are 4 subjects"
    
  def students(self):
    print "There are 60 students in",self.name,"department"
    
class Cse(Department):
  
  def __init__(self,hod):
    super(Cse, self).__init__(hod)
    print "CSE created"
    
  def subjects(self):
    print "6 subjects in cse."
    
hod = raw_input("Name of the head of the department:")
c1 = Cse(hod)
c1.students()
c1.subjects()
