#ejericio 9 imprimir tabla de multiplicar 

#input para recibir valor del usuario
print("ingresa el numero del cual deseas la tabla de multiplicar")
numerotabla= int(input())

#usar ciclo for para imprimir resultado
print('la tabla es')
for i in range(1,11,1):
	resultado= numerotabla* i
	print(numerotabla,' x ',  i,' = ', resultado)

	############ DESARRROLLADO POR STIVEN MARTINEZ VILLAMIZAR CC. 1096064595 ###########