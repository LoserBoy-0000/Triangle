import math

a= float (input("Enter the sides of the Triangle "))
b= float (input("Enter the sides of the Triangle "))
c= float (input("Enter the sides of the Triangle "))
s=(a+b+c)/2
f= s*(s-a)*(s-b)*(s-c)
Area=math.sqrt(f)
d=a*a
e=b*b
f=c*c

if ((a+b>c) and (a+c>b) and (b+c>a)) :
  print("It Form Triangle")
  print("The Area Of The Triangle is: {0} sq.unit".format(Area))

      

else :
  print("The Triangle Doesn't Form")

