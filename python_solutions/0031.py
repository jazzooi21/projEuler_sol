coin_vals = [200,100,50,20,10,5,2,1]

tot_comb = 0

for n200 in range(200//200 +1):
	if n200*200 > 200:
		break
	for n100 in range(200//100 +1):
		if n200*200+n100*100 > 200:
			break 
		for n50 in range(200//50 +1):
			if n200*200+n100*100+n50*50 > 200:
				break 
			for n20 in range(200//20 +1):
				if n200*200+n100*100+n50*50+n20*20 > 200:
					break 
				for n10 in range(200//10 +1):
					if n200*200+n100*100+n50*50+n20*20+n10*10 > 200:
						break 
					for n5 in range(200//5 +1):
						if n200*200+n100*100+n50*50+n20*20+n10*10+n5*5 > 200:
							break 
						for n2 in range(200//2 +1):
							if n200*200+n100*100+n50*50+n20*20+n10*10+n5*5+n2*2 > 200:
								break
							else:
								tot_comb += 1

								n1 = 200-(n200*200+n100*100+n50*50+n20*20+n10*10+n5*5+n2*2)
								print('comb number ', tot_comb, ': ', n200,n100,n50,n20,n10,n5,n2,n1)
print(tot_comb)