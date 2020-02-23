import random
import time

def prasino(arr):
	if arr[0] > arr[1] and arr[0] > arr[2]:
		return 0
	elif arr[1] > arr[0] and arr[1] > arr[2]:
		return 1
	elif arr[2] > arr[0] and arr[2] > arr[1]:
		return 2
	elif arr[0] < arr[1] and arr[0] < arr[2]:
		return random.choice([1,2])
	elif arr[1] < arr[0] and arr[1] < arr[2]:
		return random.choice([0,2])
	else:
		return random.choice([0,1])



stoplights = []
for i in range(3):
	stoplights.append(random.randint(5,50))
	print(stoplights[i])
print()
while True:
	time.sleep(1)
	prasinofanari = prasino(stoplights)
	feygoun = random.randint(5,10)
	erxontai1 = random.randint(0,5)
	random.seed()
	erxontai2 = random.randint(0,5)
	fanaria = ""
	for i in range(3):
		if i == prasinofanari:
			stoplights[i] -= feygoun
			fanaria += str(stoplights[i]) + "\t\t-" + str(feygoun) + "\n"
		else:
			if erxontai1 == -1:
				stoplights[i] += erxontai2
				fanaria += str(stoplights[i]) + "\t\t+" + str(erxontai2) + "\n"
			else:
				stoplights[i] += erxontai1
				fanaria += str(stoplights[i]) + "\t\t+" + str(erxontai1) + "\n"
				erxontai1 = -1
	print(fanaria)