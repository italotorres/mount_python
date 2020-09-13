# -*- coding: utf-8 -*-
##################
#
# programa versão 0.1
#Nome: lança sorte em apostas
#descrição: progama que gera numeros aleatorios
#para jogos de azar 
#Criador Ítalo
#Data: 02/09/20 
# Correções: arrumar o caracter de espaço especial "\". e verificar o porque da repetição do 60 
##################

from random import choice, sample, randrange, randint

lstu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # numeros da unidade
lstd = [0, 1, 2, 3, 4, 5, 60] # numeros da dezena
c = int(input("Informe quantos numeros deseja apostar(6-7-8-9)")) # controle de quantidade de giros

if c < 6 or c > 9:
    print("fora da sequencia")
    
else:
    
    for i in range(1, c+1):
	    d = choice(lstd)
	    u = choice(lstu)
	    if d == 60:
	    	
	    	print('Dezena %s \º  Lance: 60'  %i)
	    elif u == 0 and d == 0:
	    	r = randrange(0, 60)
	    	print('Dezena %s \º  Lance: %s '  %(i,r))
	    else:
	    	print('Dezena %s \º  Lance: %s%s '  %(i,d,u))