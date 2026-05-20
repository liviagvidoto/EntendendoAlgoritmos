# união de conjuntos

frutas = set(["maçã", "banana", "tomate"])
vegetais = set(["alface", "cenoura", "tomate"])
alimentos = frutas | vegetais 

# isso é uma interseção de conjuntos

print(frutas & vegetais) # retorna {'tomate'}

# isso é uma diferença

print(frutas - vegetais) # retorna {'maçã', 'banana'}

# operações com conjuntos

print(vegetais - frutas) # retorna {'alface', 'cenoura'}