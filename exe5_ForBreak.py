pessoas_presentes = ["john snow","jesse pinckman","aria stark","tyrion lannister" ]
# QUERO SABER SE UM PESSOA NAO ESTA PRESENTE 
chamada = "aria stark"
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print("{} esta presente.".format(chamada) )
        break
    else:
        print (" so um print ppara mostrar que o for passou por essa pessoa:"+ str(pessoa))