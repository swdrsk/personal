import math

def entropy(a):
    suma = sum(a)
    pa = [float(i)/suma for i in a]
    return sum([pi*math.log(pi) if pi>0 else 0 for pi in pa])
    	
