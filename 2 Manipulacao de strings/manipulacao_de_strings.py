# utilizando o metodo uper() todas as letras da string ficarão maiusculas
print(("letras minusculas para maiusculas").upper())

# utilizando o metodo lower() todas as letras da string ficarão minusculas
print(("LETRAS MAIUSCULAS PARA MINUSCULAS").lower())

# utilizando a funcao len() para saber quantos caracteres temos na string
print(len("12345"))

# utilizamos a funcao replace para trocar um caractere por outro , 
#  nesse caso utilizei para tirar os espaços da estring
print("==="* 10) 
nome = "    j  oão   " 
print(nome) 
print(f"o tamanho da string é : {len(nome)}") # string com 13 caracteres
nome = nome.replace(" ", "")
print(nome)
print(f"o tramanho da string depois do replace é: {len(nome)}") # string com 4 caracteres

# utilizamos o metodo count() para saber quantas vezes um caractere se repete numa string
print("==="* 10) 
exemplo = "111 1234"
print(exemplo.count("1"))

# utilizamos o metodo find() para  saber em qual posicao do array esta algum caractere
# obs se existir mais de um caractere igual ,o metodo find() pega a posicao do primeiro caractere repetido
print("==="* 10) 
array = "a122221a"
print(array.find("a"))

# utilizamos o metodo title() para colocar letra maiusculas no inicio das palavras dentro da string
print("==="* 10)
titulo = " joao batista candido"
print(titulo.title())

