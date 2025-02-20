
lucro_1tri = {'jan': 1, 'fev':2 , 'mar':3, }
lucro_2tri = {'abr': 4, 'mai':5 , 'jun':6 }
#del = exlcuir
del lucro_2tri['jun']
print(lucro_2tri)
#pop = retirar 
lucro_1tri = {'jan': 1, 'fev':2 , 'mar':3, }
lucro_2tri = {'abr': 4, 'mai':5 , 'jun':6 }
lucro_jun=lucro_2tri.pop('jun')
print(lucro_2tri)
print(lucro_jun)
#clear
lucro_1tri = {'jan': 1, 'fev':2 , 'mar':3, }
lucro_2tri = {'abr': 4, 'mai':5 , 'jun':6 }
lucro_2tri.clear()
print(lucro_2tri)
