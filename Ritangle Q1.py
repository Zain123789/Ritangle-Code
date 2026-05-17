import math

dt = {}
for a in range(1,7):
	for b in range(1,7):
		for c in range(1,7):
			for d in range(1,7):
				z = [a,b,c,d]
				counter = 0
				for i in range(3):
					if z[i] not in z[i+1:]:
						counter += 1
						
				if counter == 3:
					x = a + c
					x /= 2
					y = b + d
					y /= 2
					
					if round(x) == x and round(y) == y:
						if x not in z and y not in z and x != y:
							length = (d-b) ** 2
							length += (c-a) ** 2
							length = math.sqrt(length)
							
							dt[(a,b,c,d,x,y)] = length
							
print(max(dt.values()))

					
				
						