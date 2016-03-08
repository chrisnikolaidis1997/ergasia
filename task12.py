import random
table = []
for i in range(50):
	x = []
	for j in range(50):
		x.append(' ')
	table.append(x)
r = random.randint(5,30)
x_top = 49
x_bottom=0
y_left = 49
y_right = 0
for i in range(r):
	x = random.randint(0,49)
	y = random.randint(0,49)
	table[y][x] = 'O' 
	if (y<y_left): y_left = y
	if (y>y_right): y_right = y
	if (x<x_top) : x_top = x
	if (x>x_bottom) : x_bottom = x
for x in range(50):
	for y in range(50):
		if (x<x_bottom and x>x_top and y>y_left and y<y_right):
			table[y][x] = 'O'
point = 0
for i in range(1000):
	x = random.randint(0,49)
	y = random.randint(0,49)
	if (table[y][x]=='O'): point = point+1
print point
		