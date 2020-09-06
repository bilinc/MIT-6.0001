def removeDups(L1, L2):
	for e1 in L1[:]:
		if e1 in L2:
			L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
newL = L1
removeDups(newL, L2)
print('L1 =', L1)

L3 = list(L1)
L3.extend([23])
print(L3)
print(L1)