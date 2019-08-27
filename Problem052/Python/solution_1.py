for i in range(101,1000000): #bruuuuuute force 
  if set(list(str(i))) == set(list(str(2*i))) == set(list(str(3*i))) == set(list(str(4*i))) == set(list(str(5*i))) == set(list(str(6*i))):
    print(i)
    break
