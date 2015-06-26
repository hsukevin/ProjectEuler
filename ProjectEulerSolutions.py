# Kevin Hsu
# Project Euler Solutions in Python

import math

# Problem1 Multiples of 3 and 5
def multiples_3and5(maxNumber):
	returnSum = 0
	for number in range(maxNumber):
		if((number % 3) == 0):
			returnSum = returnSum + number
		elif((number % 5) == 0):
			returnSum = returnSum + number
	print(returnSum)
# multiples_3and5(1000)



# Problem2 Even Fibonacci numbers
def evenFibonaccis(maxNumber):
	fib1 = 1
	fib2 = 2
	tempfib = 0
	evenSum = 0
	while (fib2 < maxNumber):
		if((fib2 % 2) == 0):
			evenSum = evenSum + fib2
		tempfib = fib1
		fib1 = fib2
		fib2 = tempfib + fib2
	print(evenSum)
# evenFibonaccis(4000000)



# Problem3 Largest Prime Factor
def largestPrimeFactor(number):
	factor = 2
	while(factor < number):
		if(number % factor == 0):
			print(factor)
			number = number / factor
			continue
		else:
			factor = factor + 1
	print(factor)
# largestPrimeFactor(600851475143)



# Problem4 Largest Palindrome Product
def largestPalindromeProduct(digits):
	num1 = num2 = 10 ** digits -1
	palindromeArray = []
	while(num1>0):
		# print(num1,num2,num1*num2)
		check = str(num1*num2)
		reverse = check[::-1]
		if(check == reverse):
			palindromeArray.append(num1*num2)
			# print(num1*num2)
		if(num1 < num2):
			num2 = num2 -1
		else:
			num1 = num1 -1
			num2 = 10 **digits -1
	print(max(palindromeArray))
# largestPalindromeProduct(3)



# Problem5 Smallest Multiple
def smallestMultiple(largestDivisor):
	number = 1
	while(True):
		divisor = largestDivisor
		isDivisible = True
		while(divisor > 0):
			if((number % divisor) == 0):
				divisor = divisor -1
			else:
				isDivisible = False
				break
		if(isDivisible):
			print(number)
			break
		else:
			number = number + 1
# smallestMultiple(20)



# Problem6 Sum Square Difference
def sumSqDifference(number):
	difference = 0
	for x in range(number + 1):
		difference = difference + x
	difference = difference ** 2
	for x in range(number + 1):
		difference = difference - (x ** 2 )
	print(difference)
# sumSqDifference(100)



# Problem7 10001stPrime
def stPrime(number):
	count = 0
	prime = 1
	while(count < number):
		prime = prime + 1
		isPrime = True
		for x in range(2,prime):
			if((prime % x) == 0):
				isPrime = False
				break
		if(isPrime):
			count = count + 1
	print(prime)
# stPrime(10001)



# Problem8 Largest Product in Series
def largestProductInSeries(adjacent, number):
	number = str(number)
	# print(len(number))
	largest = 1
	for x in range(adjacent):
		largest = largest * int(number[x])
	last = largest
	for x in range(len(number)):
		if(x < adjacent):
			print(x)
			continue
		if((number[x] == '0') or (number[x-adjacent] == '0')):
			last = 1
			for y in range(13):
				last = int(number[x-y]) * last
			continue
		last = last * int(number[x]) / int(number[x-adjacent])
		if(last > largest):
			largest = last
	print(largest)
# largestProductInSeries(13,7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)


# Problem9 Special Pythagorean Triplet
def pythagoreanTriplet(summation):
	found = False
	for a in range(1, summation+1):
		for b in range(a+1, summation+1):
			c = math.sqrt((a**2) + (b**2))
			if(a+b+c==summation):
				found = True
				break
		if(found):
			break
	print(a,b,c,a*b*c)
# pythagoreanTriplet(1000)



# Problem10 Summation of Prime Numbers
def sumOfPrimes(sumTo):
	if(sumTo < 2):
		print(0)
		return

	summation = 0
	array = []
	for numbers in range(0,sumTo+1):
		array.append([numbers,True])
	array[0][1] = array[1][1] = False
	# print(arrayprint(array))
	for index in array:
		# print(index)
		if(index[1] == False):
			continue
		else:
			# print(str(index) + " in here")
			summation = summation + index[0]
			multiple = 2
			while(multiple * index[0] < sumTo + 1):
				array[multiple*index[0]][1] = False
				multiple = multiple + 1
	print(summation)

	# for number in range(1,int(sumTo/2 + 0.5)):
	# 	number = 2 * number + 1
	# 	if(number%2 == 0):
	# 		continue
	# 	isPrime = True
	# 	for factors in range(2,number):
	# 		if(number%factors == 0):
	# 			isPrime = False
	# 	if(isPrime):
	# 		print(number)
	# 		summation = summation + number
	# print(summation)
# sumOfPrimes(2000000)



# Problem11 Largest Product in a Grid
def largestGridProduct(adjacent,size,grid):
	grid = grid.split(" ")
	# print(len(grid))
	maxProduct = 0
	twoDgrid = []
	for col in range(size):
		row = []
		for rows in range(size):
			row.append(int(grid[rows+col*size]))
		twoDgrid.append(row)

	for number in range(size**2):
		up = 1
		right = 1
		upRight = 1
		downRight = 1
		row = int(number/size)
		col = number%size
		for multiply in range(adjacent):
			upIndex = [row-multiply,col]
			rightIndex = [row,col+multiply]
			upRightIndex = [row-multiply,col+multiply]
			downRightIndex = [row+multiply,col+multiply]
			if upIndex[0] < size and upIndex[0] > -1 and upIndex[1] < size and upIndex[1] > -1:
				up = up * twoDgrid[upIndex[0]][upIndex[1]]
			if rightIndex[0] < size and rightIndex[0] > -1 and rightIndex[1] < size and rightIndex[1] > -1:
				right = right * twoDgrid[rightIndex[0]][rightIndex[1]]
			if upRightIndex[0] < size and upRightIndex[0] > -1 and upRightIndex[1] < size and upRightIndex[1] > -1:
				upRight = upRight * twoDgrid[upRightIndex[0]][upRightIndex[1]]
			if downRightIndex[0] < size and downRightIndex[0] > -1 and downRightIndex[1] < size and downRightIndex[1] > -1:
				downRight = downRight * twoDgrid[downRightIndex[0]][downRightIndex[1]]
		if(maxProduct < max(up,right,upRight,downRight)):
			maxProduct = max(up,right,upRight,downRight)
	print(maxProduct)
# largestGridProduct(4,20,"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")



# Problem12 Highly Divisible Triangular Number
def triangleNumber(divisors):
	naturalNumber = 0
	triangleNumber = 0
	divisorCount = 0
	lastBiggestDivisor = 0
	while(divisorCount<divisors + 1):
		naturalNumber = naturalNumber + 1
		triangleNumber = naturalNumber + triangleNumber
		divisorCount = 0
		for factor in range(int(triangleNumber**0.5)+1):
			if((triangleNumber%(factor+1)) == 0):
				divisorCount = divisorCount + 1
		divisorCount *= 2
	print(triangleNumber)
triangleNumber(500)