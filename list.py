R = input("Enter a list element separated by space ")
list1  = R.split()
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    if int(num) >= 0: 
       print(num, end = " ") 