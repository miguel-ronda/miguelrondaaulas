vendas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
meta = 10
qtde_bateu_meta = 0
for venda in vendas:
    if venda >= meta:
        qtde_bateu_meta += 1
qtde_funcionarios = len(vendas)
print ("o percentual de pessoas que bateram a meta foi de {:.3%}".format(qtde_bateu_meta/qtde_funcionarios))
