vendas_tec = {"iphone":1500,"samsung galaxy":1200, "tv samsung":1000,"ps5":14300,"tablet":17020,"ipad":1200}
for chave in vendas_tec:
    print(chave)




# mostrando chave e valor com for
vendas_tec = {"iphone":1500,"samsung galaxy":1200, "tv samsung":1000,"ps5":14300,"tablet":17020,"ipad":1200}
for chave in vendas_tec:
    print("o produto {} vendeu {} unidades". format(chave,vendas_tec[chave]))
#
vendas_tec = {"iphone":1500,"samsung galaxy":1200, "tv samsung":1000,"ps5":14300,"tablet":17020,"ipad":1200}
for produtos, vendas in vendas_tec.items():
    print('{}:{} de unidades'.format(produtos,vendas))

