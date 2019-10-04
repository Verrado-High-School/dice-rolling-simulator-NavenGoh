import random

num_rolled = int(input("How many times will the dice be rolled?"))


ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

rolls= 0

while rolls< num_rolled:
	rolls+= 1
	D6 = random.randrange(1, 7, 1)

	print("Roll " + str(rolls) + "-------------" + "\n" + "Dice (1,6): " + str(D6))

	
	if D6 == 1:
		ones += 1
	elif D6 == 2:
		twos += 1
	elif D6 == 3:
		threes += 1
	elif D6 == 4:
		fours += 1
	elif D6 == 5:
		fives += 1
	else:
		sixes += 1

	print("1s - " + str(ones))
	print("2s - " + str(twos))
	print("3s - " + str(threes))
	print("4s - " + str(fours))
	print("5s - " + str(fives))
	print("6s - " + str(sixes))


	print("Percentages:")
	print("1s - " + str(ones/(rolls)*100) + "%")
	print("2s - " + str(twos/(rolls)*100) + "%")
	print("3s - " + str(threes/(rolls)*100) + "%")
	print("4s - " + str(fours/(rolls)*100) + "%")
	print("5s - " + str(fives/(rolls)*100) + "%")
	print("6s - " + str(sixes/(rolls)*100) + "%")