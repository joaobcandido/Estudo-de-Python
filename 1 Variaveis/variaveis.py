# quando declaramos uma variavel estamos reservando um espaço na
# memoria RAM para guardar essa informação
# para declarar uma variavel em python não precizamos colocar o tipo

variavel_tipo_inteiro = 100 # armazena apenas numeros
variavel_tipo_string = " armazena cadeia de caracteres"
variavel_tipo_float = 1.1 # armazena numeros com ponto flutuante
variavel_tipo_bool = True # armazena verdadeiro ou falso

# para exibir uma string e um outro tipo de variavel no mesmo print()
# precizamos utilizar o f e os {}
idade = 25
print(f"eu tenho {idade} anos")

# outra forma é utilizar o .format
print("eu tenho {} anos".format(idade))

# para escrever na tela o valor da variavel utilizamos a função print()
print(variavel_tipo_inteiro)

# para sabermos o tipo de dado da variavel utilizamos a função type()
print(type(variavel_tipo_inteiro))

