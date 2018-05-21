def substr(y,p):
	for i in xrange(0,len(y)):
		if p[i] not in y:
			return 1
	return 0
for i in xrange(1,1000000):
	count=0
	x=i
	y=str(x)
	for a in xrange(2,7):
		p=str(a*x)
		if substr(y,p)==0:
			count+=1
	if count==5:
		print(x)
		break
