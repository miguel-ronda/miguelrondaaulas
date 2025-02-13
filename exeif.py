faturamento = input("qual foi o faturamento da loja nesse mes?")
custo = input("qual o custo da loja nesse mes?")
if faturamento!= '' and custo!= '': 
 lucro = int(faturamento) - int(custo)
 print ("o lucro da loja foi de {} R$".format(lucro))
else:
 print("algum valor nao foi fornecido")

#faturamento = input("qual foi o faturamento da loja nesse mes?")
#custo = input("qual o custo da loja nesse mes?")
#if faturamento and custo: 
 #lucro = int(faturamento) - int(custo)
 #print ("o lucro da loja foi de {} R$".format(lucro))
#else:
 #print("algum valor nao foi fornecido")