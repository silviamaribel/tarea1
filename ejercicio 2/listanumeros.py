def lista(inicio, fin):
	a=inicio
	b=fin
	while a <= b:
		print a,
		a=a+1
def numpares(inicio, fin):
	a=inicio
	b=fin
	while a <= b:
		if a % 2 ==0:
			print a,
			a=a+1
		else :
			a=a+1	
p=input ("digite el primer numero")
q=input ("digite el segundo numero")
lista(p, q)
print " "
print "pares  "
numpares(p, q)