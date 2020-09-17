# -*- coding: utf-8 -*-
##################
#
# programa versão 0.2
#Nome: lança sorte em apostas
#descrição: progama que gera numeros aleatorios
#para jogos de azar
#Criador Ítalo
#Data: 02/09/20
# Data de atualização: 17/09/20
# Correções:  Verificar uma função que filtre os valores alfa-numericos em na variavel c
#. e verificar o porque do envio dos valores > q 60
##################

from random import choice, sample, randrange, randint

lstu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # numeros da unidade
lstd = [0, 1, 2, 3, 4, 5, 6] # numeros da dezena
c = 1
while c != 0:
  c = int(input("Informe quantos numeros deseja apostar(6-7-8-9) ou digite 0 para sair")) # controle de quantidade de giros
  if c < 6 or c > 9:
   print("fora da sequencia")
  else:
        for i in range(1, c+1):
          d = choice(lstd)
          u = choice(lstu)
          if d > 6 and u > 0:
            r = randrange(1, 60)
            print('Dezena %s º  Lance: %s'  %(i,r))
          elif u == 0 and d == 0:
            r = randrange(1, 60)
            print('Dezena %s º  Lance: %s '  %(i,r))
          else:
          	print('%s º Dezena: %s%s '  %(i,d,u))