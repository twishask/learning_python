num = 5

def rec(x):
  if(x>1):
    return x * rec(x-1)
  else:
    return 1
  
print "Factorial of ",num," is ",rec(num)
