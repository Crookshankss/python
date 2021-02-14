print("Fibonacci sequence:")
nt = int(input("Enter the number of terms:"))

n1, n2 = 0, 1
count = 0


if nt <= 0:
   print("Error")

else:
  
   while count < nt:
       print(n1)
       nth = n1 + n2
     
       n1 = n2
       n2 = nth
       count += 1