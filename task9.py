import random
s = 0
table = [] 
for i in range(20):  #table 20x10 creation#
	x = []
	for j in range(10):
		x.append(' ') #keno giati stin arxi tou paixnidiou kamia thesi tou pinaka den kaliptetai apo touvlaki# 
	table.append(x)
endgame="false"
while (endgame=="false"):
	r = random.randint(0,8) 	#i metabliti r deixnei tin aristeri pleura tou touvlou#
	x = 20 		#i metabliti x deixnei to kato meros toy touvlou#
	k = "false" 
	while(k=="false"):
		if ((table[x-1][r]==' ') and (table[x-1][r+1]==' ') and (x>0)): #elegxei an kato apo to touvlo vrisketai allo touvlaki i o "patos" tou pinaka#
			x =x-1 #an den yparxei apo kato touvlo, to touvlo peftei kata 1 thesi#
		else: 
			if (x>17): 
				endgame="true" #an to touvlo brisketai sto pano meros tou pinaka,tote to paixnidi termatizetai#
				k = "true"#i metabliti k dilonei oti an touvlo stamatise na peftei#
			else:
				table[x][r] = 'O' #to O shmainei oti auti i thesi kaliptetai apo touvlaki#
				table[x][r+1] = 'O'
				table[x+1][r] = 'O'
				table[x+2][r] = 'O'
				s = s+1 #mpainei ena akomi touvlo#
				k ="true"
print s #ektiposi tou arithmou twn toublwn pou kataferan na mpoun ston pinaka#