def espalindromo():
	var = raw_input("Introduzca la cadena ::> ")
	if var==var[::-1]:
		print "Es un Palindromo"
	else:
		print "No es un palindromo"
espalindromo()