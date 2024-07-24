# para conseguir capturar uma entra de dados utilizamos a função input()
# podemos passar como parametro uma string
# input("digite sua idade: ")
# podemos salvar esse dado dentro de uma variavel
idade = input("digite a sua idade: ")

# por padrao esse dados sao salvos como string
print(type(idade))

# nesse caso podemos converter de string para inteiro para facitar a manipulacao do dado
idade = int(input("digite a sua idade: "))
print(type(idade))