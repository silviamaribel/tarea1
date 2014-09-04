def generar(numero):
	aux=numero
	cont=0
	rep=""
	while numero>=1:
		numero-=1
		cont=cont+1
		for i in range(cont):
			i=cont
			resp=i
			print resp
	cont=i
	resp=""
	while numero< aux:
		numero+=1
		cont-=1
		for j in range(cont):
			i=cont
			resp=i
			print resp
print generar(5)