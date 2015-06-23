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

	print(reversed("NERD"))
	while(True):
		# print(num1,num2,num1*num2)
		check = str(num1*num2)
		if(check == reversed(check)):
			print(num1*num2)
			break
		else:
			if(num1 < num2):
				num2 = num2 -1
			else:
				num1 = num1 -1
				num2 = 10 **digits -1
largestPalindromeProduct(3)