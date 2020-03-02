from colorama import init, Fore, Style, Back
import pyfiglet
init(autoreset=True)

mod = None
mods = []
num_str = ""

# function makes the string usable for other functions

def convert(user_input):
	global num_str
	global mods

	equation = user_input.split()
	num_str = equation[0::2]
	numbers = []
	mods = equation[1::2]
	for num in num_str:
		try:
			numbers.append(int(num))
		except:
			return numbers
	return numbers

# define a function to use the math opps

def numAdd(num1=0, num2=0):
	return num1 + num2

def numDif(num1=0, num2=0):
	return num1 - num2

def numMul(num1=0, num2=0):
	return num1 * num2

def numDiv(num1=0, num2=0):
	return num1 / num2

def numPow(num1=0, num2=0):
	return num1 ** num2

# set up conditional logic to to reconize the symbols (+ , - , * , /)

def numMod(Mod, num1, num2):
	if mod == "+":
		return numAdd(num1, num2)
	elif mod == "-":
		return numDif(num1, num2)
	elif mod == "*":
		return numMul(num1, num2)
	elif mod == "/":
		return numDiv(num1, num2)
	elif mod == "**":
		return numPow(num1, num2)
	else:
		print(f'"{mod}" is invalid')

# loop to run the equation from left -> right not OoO

def exe(num_list):
	global mod
	answer = "Nothing cause ur stupid"
	for x in range(1, len(num_str) + 1):
		while len(numbers) != 1:
			if numbers != []:
				num1 = numbers.pop(0)
				num2 = numbers.pop(0)
				mod = mods.pop(0)
				temp = numMod(mod, num1 ,num2)
				numbers.insert(0, temp)
				answer = numbers[0]
	return answer

print(Fore.YELLOW + "################################################################")
print(Fore.MAGENTA + Style.BRIGHT + pyfiglet.figlet_format("EQUATION"))
print(Fore.YELLOW + "################################################################")
print(Fore.MAGENTA + Style.BRIGHT + pyfiglet.figlet_format("CALCULATOR"))
print(Fore.YELLOW + "################################################################")
# ask for an imput in format (num (mod) num ->)
while True:
	print(Fore.CYAN + Style.BRIGHT +"format: [v * w / x + y - z]")
	print(Fore.RED + Style.BRIGHT + "*\U0001f600rember to use spaces\U0001f600*")
	user_input = input(Fore.GREEN + Style.BRIGHT + ">>> ")

	# calling functions to do math
	numbers = convert(user_input)
	if numbers == False:
		print(Fore.RED + "you can only input numbers")
		print(Fore.CYAN + Style.BRIGHT +"format: [v * w / x + y - z]")
		print(Fore.RED + Style.BRIGHT + "*no order of operations yet*")
		user_input = input(Fore.GREEN + Style.BRIGHT + ">>> ")
		numbers = []
	
	numbers = convert(user_input)	
	answer = exe(numbers)

	# print answer

	print(Fore.YELLOW + Style.BRIGHT + f"{user_input} = " + Fore.GREEN + f" {answer}")
	print(Style.RESET_ALL)


	while True:
		loop = input("do you want to try another? " + Fore.RED + Style.BRIGHT + "[Y/n]> ")
		if loop.lower() == "y":
			user_input = input(Fore.GREEN + Style.BRIGHT + ">>> ")
			if numbers == []:
				print(Fore.RED + "you can only input numbers")
				break
			else:
				numbers = convert(user_input)
				answer = exe(numbers)
				print(Fore.YELLOW + Style.BRIGHT + f"{user_input} = " + Fore.GREEN + f" {answer}")
		else:
			print(Fore.BLUE + Style.BRIGHT + pyfiglet.figlet_format("Good Bye!"))
			quit()