estoque = [1,2,3,4,5,6,7,8,9,10,11,12,13]
produtos = ["coca","pepsi","guarana","skol","brahma","agua","del valle","red bull","dolly","fanta","sprite","sukita","tubaina"]
nivelminimo = 5 
for i, qtde in enumerate(estoque) :
    if qtde < nivelminimo:
        print(produtos[i],qtde)
