def ValorCadena(cad1, cad2):
	a=len(cad1)
	b=len(cad2)
	if a > b:
		print cad1
	else:
		if a==b:
			print cad1 + cad2
		else:
			print cad2
p=raw_input("digite la primera cadena: ")
q=raw_input("digite la segunda cadena: ")
ValorCadena(p, q)