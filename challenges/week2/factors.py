def driver():
  ##First I get the 2 integer inputs from the user
  print("Hi! I am going to use the Euclidean Algorithm to calculate the greatest common factor!")
  print("")
  print("What is your first integer?")
  int1 = input()
  print("What is your second integer?")
  int2 = input()
  
  #a1 and b1 are going to represent the "n" and this algorithm manipulates a and b until we get "nk"
  a1 = int1
  b1 = int2
  
  
  #this is the function that employs the Euclidean Algorithm to get the GCF
  def getGCF(a1,b1):
      #this if-else statement figures out which input is the greater
      #it sets a as the greater number and b as the smaller number
      if a1 < b1:
          (a1,b1) = (b1,a1)
  
      #this while loop repeats keeps on finding the remainder n until we get nk
      #The loop iterates along all the equations in the form m = qn + n1 until we obtain the GCF
      while (a1 % b1 != 0):
          (a1 ,b1) = (b1, a1 % b1)
      return b1
  
  #this is the GCF of the two integer
  g = getGCF(int(a1),int(b1))
  
  #a2 and b2 are our two integers and we will manipulate them till we solve our linear equation
  a2 = int1
  b2 = int2
  
  #This is the function that gets the solution to Diophantine  ax + by = g, where a,b,x,y,g are integers and g = gcf(a,b)
  def getDiophantine (a2, b2, g):
      assert (
              g % getGCF(a2, b2) == 0
      )  # greatest_common_divisor(a,b) function implemented below
      (d, x, y) = extended_gcf(a2, b2)  # extended_gcd(a,b) function implemented below
      r = g / d
      return (r * x, r * y)
  
  
  #Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x and y, then d = gcf(a,b). This returns our initial x and y values.
  def extended_gcf(a2, b2):
      assert a2 >= 0 and b2 >= 0
  
      if b2 == 0:
          d, x, y = a2, 1, 0
      else:
          (d, p, q) = extended_gcf(b2, a2 % b2)
          x = q
          y = p - q * (a2 // b2)
  
      assert a2 % d == 0 and b2 % d == 0
      assert d == a2 * x + b2 * y
  
      return (d, x, y)
  
  
  #print all answers
  print ("The GCF is = ")
  print (getGCF(int(a1),int(b1)))
  
  print("")
  print("The (x, y) solution to the Diophantine is = ")
  print(getDiophantine(int(a2), int(b2), int(g)))
  print("for integer 1 and integer 2 respectively")