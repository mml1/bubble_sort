import random
import time



#variables
arr=[]
i = 0 

#print the random numbers
for x in range(100):
	arr.append(random.randint(0,10000))

# will go through the array and bubble sort
while i < len(arr)-1:
 	for item in range(0, len(arr)-1):
		if arr[item+1] < arr[item]:
			temp= arr[item+1]
			arr[item+1] = arr[item]
			arr[item] =temp	
	i +=1

print arr

start_time = time.time()

print(time.time() - start_time)