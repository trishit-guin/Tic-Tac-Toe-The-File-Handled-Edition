def record():
	global a, b, c, d, e, f, g, h, i
	global p1, p2
	global count
	file = open("record.txt", "a+")

	if count == 0:
		file.write(f"{p1} vs {p2}\n")
		count += 1
	file.write(f"\n{a} | {b} | {c} "
			   f"\n{d} | {e} | {f} "
			   f"\n{g} | {h} | {i} \n")


def game():
	print('\nWelcome to tic tac toe')
	print('the respective number corresponding to the position are as follows:')
	print('7|8|9')
	print('4|5|6')
	print('1|2|3')
	global p1, p2
	p1 = input("player1 enter your name: ").upper()
	p2 = input("player2 enter your name: ").upper()
	print(f'{p1} has O')
	print(f'{p2} has X')
	print('Game begins')
	print()

	global a, b, c, d, e, f, g, h, i
	a = b = c = d = e = f = g = h = i = "_"
	v = 1
	l = "X"
	o = "O"
	global x
	x = 0
	global count
	count = 0

	print(a, "|", b, "|", c)
	print(d, "|", e, "|", f)
	print(g, "|", h, "|", i)

	while x < 9:
		if v % 2 == 0:
			n = int(input(f'\nCHANCE OF {p2} '))

			if n == 1:
				if g == o or g == l:
					pass
				else:
					g = l
					x += 1
					v += 1
			if n == 2:
				if h == o or h == l:
					pass
				else:
					h = l
					x += 1
					v += 1
			if n == 3:
				if i == o or i == l:
					pass
				else:
					i = l
					x += 1
					v += 1
			if n == 4:
				if d == o or d == l:
					pass
				else:
					d = l
					x += 1
					v += 1
			if n == 5:
				if e == o or e == l:
					pass
				else:
					e = l
					x += 1
					v += 1
			if n == 6:
				if f == o or f == l:
					pass
				else:
					f = l
					x += 1
					v += 1
			if n == 7:
				if a == o or a == l:
					pass
				else:
					a = l
					x += 1
					v += 1
			if n == 8:
				if b == o or b == l:
					pass
				else:
					b = l
					x += 1
					v += 1
			if n == 9:
				if c == o or c == l:
					pass
				else:
					c = l
					x += 1
					v += 1
		else:
			n = int(input(f'\nCHANCE OF {p1} '))
			if n == 1:
				if g == l or g == o:
					pass
				else:
					g = o
					x += 1
					v += 1
			if n == 2:
				if h == l or h == o:
					pass
				else:
					h = o
					x += 1
					v += 1
			if n == 3:
				if i == l or i == o:
					pass
				else:
					i = o
					x += 1
					v += 1
			if n == 4:
				if d == l or d == o:
					pass
				else:
					d = o
					x += 1
					v += 1
			if n == 5:
				if e == l or e == o:
					pass
				else:
					e = o
					x += 1
					v += 1
			if n == 6:
				if f == l or f == o:
					pass
				else:
					f = o
					x += 1
					v += 1
			if n == 7:
				if a == l or a == o:
					pass
				else:
					a = o
					x += 1
					v += 1
			if n == 8:
				if b == l or b == o:
					pass
				else:
					b = o
					x += 1
					v += 1
			if n == 9:
				if c == l or c == o:
					pass
				else:
					c = o
					x += 1
					v += 1

		print(a, "|", b, "|", c)
		print(d, "|", e, "|", f)
		print(g, "|", h, "|", i)

		record()

		if a == b == c != "_" or d == e == f != "_" or \
			g == h == i != "_" or a == d == g != "_" or \
			b == e == h != "_" or c == f == i != "_" or \
			a == e == i != "_" or c == e == g != "_":
			if v % 2 == 0:
				print(f'{p1} is the winner')
				return "game over"
			else:
				print(f'{p2} is the winner')
				return "game over"

		if x == 9:
			print("game is tie")
			return "game over"


def read():
	f = open('record.txt', 'r')
	data = f.read()
	if data == '':
		print("file is empty")
	else:
		print(data)


def clear():
	f = open('record.txt', 'w+')
	f.truncate(0)
	print("Record file cleared")


count = 0
abc = 0
while True:
	if abc == 0:
		print("enter p to start playing")
	else:
		print("enter p to play again")
	print("enter r to read record")
	print("enter c to clear record")
	print("enter any other key to exit")
	ch = (input())

	if ch.upper() == "P":
		game()
		abc += 1
		print()
	elif ch.upper() == "R":
		read()
		print()
	elif ch.upper() == "C":
		clear()
		print()
	else:
		break

