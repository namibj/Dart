def main():
	table = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
			 "d1": 2, "d2": 4}
	x = input()
	print(type(x))
	if x in table:
		print("yes")
		y = table[x]
		print(y)
		print(type(y))
	else:
		print("no")



if __name__ == '__main__':
	main()
