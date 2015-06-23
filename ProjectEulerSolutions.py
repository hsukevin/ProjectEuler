# Kevin Hsu
# Project Euler Solutinons in Python

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
largestProductInSeries(13,7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)













