from table import table


# TODO Spieler anzahl abfragen

# TODO Spieler namen eintragen

# TODO SpielModi (301, 501, 701)

# class player:
#	def __init__(self, name, score):
#		self.name = name
#		self.score = score

def spiel_modi():
	game_mode = int(input("Bitte geben sie den Spiel Modus an (301/501/701): "))
	return game_mode


def player_numbers():
	pass


def main():
	score = spiel_modi()
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
