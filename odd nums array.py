import numpy as np

array = np.arange(10)    

result = [1, 3, 5, 7, 9]   

print()

result2 = [2, 4, 6, 8, 10]   

for i in array:

 if i % 1 != 0:

   result.append(i)

print(np.array(result)) 
print(np.array(result2)) 

#Did this both ways because i wasnt sure if you (Neal) wanted the odd numbers extracted and displayed, or the odd numbers extracted and the even numbers displayed. 

