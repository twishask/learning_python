print "If else condition"
n = input("Type a number:")
if (n%2 == 0):
  print "No. is even"
else:
  print "No. is odd"

print "While loop"
n1 = input("Enter a number to find factorial")
fac = 1
while(n1!=0):
  fac = n1*fac
  n1 = n1-1
print fac

n2 = raw_input("Enter a string:")
l = len(n2)
s = 0
while s<=l:
  if n2[s] != n2[l-1]:
    print "Not palindrome"
    break
  else:
    s=s+1
    l=l-1
if s>l:
  print "palindrome"

print "For loop"
x = input("Enter 1st 3x3 matrix:")
y = input("Enter 2nd 3x3 matrix:")
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(x)):
   for j in range(len(y[0])):
       result[i][j] = x[i][j] + y[i][j]

print "Addition of 2 matrices is"
for r in result:
   print r
