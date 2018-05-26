count=0
for i in range (1,101):
	for j in range(0,i):
		factn=factr=fact=1
		ncr=0
		m=i-j
		for x in range(1,i+1):
			factn*=x
		if j==0 or j==1:
			factr=1
		else:
			for x in range(2,j+1):
				factr*=x
		for x in range(2,m+1):
			fact*=x
		ncr= factn / factr / fact
		if ncr>1000000:
			count+=1
print(count)
