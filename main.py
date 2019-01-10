from table import table


# TODO Spieler anzahl abfragen

# TODO Spieler namen eintragen

# TODO SpielModi (301, 501, 701)


def main():
	score = 501
	while score != 0:
		throw = 1
		sum = 0
		while throw < 4:

			print("Wurf :{0}".format(throw))
			x = input()
			if x in table:
				sum = sum + table[x]
				print("Summe: {}".format(sum))
			else:
				print("falsche eingabe")
				throw -= 1
			throw += 1
		score = score - sum
		print("Rest: {}".format(score))


if __name__ == '__main__':
	main()
