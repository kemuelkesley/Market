#Compra e venda de Produtos.
print("-"*40)
print("Menu para compras de itens ver.1")
print("-"*40)

class ProdutosDeLimpeza:
    detergente = 29.99
    sabaoLiquido = 14.99
    amaciante = 15.55
    sabaoEmPo = 3.99
    desinfetante = 5.67

#Exibir menu com os nomes do produto e valor.    

def produtos_limpeza ():
    linhas()
    print("Produto de Limpeza\n")
    linhas()
    print("1-Detergente R$", ProdutosDeLimpeza.detergente)
    linhas()
    print("2-Sabão liquido R$", ProdutosDeLimpeza.sabaoLiquido)
    linhas()
    print("3-Amaciante R$", ProdutosDeLimpeza.amaciante)
    linhas()
    print("4-Sabão em Pó R$", ProdutosDeLimpeza.sabaoEmPo)
    linhas()
    print("5-Desinfetante R$", ProdutosDeLimpeza.desinfetante)
    linhas()

# linhas
def linhas():
    print("-"*30)

# Menu de forma de pagamento (cartão, credito ou debito)

def menu_pagamento():
    linhas()
    print("1 - Cartão de Crédito")
    linhas()
    print("2 - Cartão de Debito")
    linhas()
    print("3 - Dinheiro")
    linhas()

# print("Produtos de limpeza") 
# produtos_limpeza()
# print("\n")

add = int(input("Escolha 1 - Para produtos de limpeza e 2 - Para sair:"))

if add == 1:
    print("Produtos de limpeza disponivel: ")
    # Mostar o menu para o cliente comprar.
    produtos_limpeza()

    # Abrindo a opção de menu
    opc = int(input("Qual produto de limpeza deseja comprar:"))

    if opc == 1:
        linhas()
        comprar = int(input("Quantos Detergentes:"))
        linhas()
        produto = ProdutosDeLimpeza.detergente * comprar
        print("Valor a pagar %2f"%produto)
        menu_pagamento()
        forma_pagamento = int(input("Qual a forma de pagamento:"))
        
        if forma_pagamento == 1:
            print("Forma de pagamento escolhida - Cartão de Crédito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 2:
            print("Forma de pagamento escolhida - Cartão de Débito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 3:
            print("Forma de pagamento escolhida - Dinheiro")
            print("Valor a pagar %2f"%produto, "Desconto de 10%")
            desconto = (produto * 10)/100
            print("Desconto de R$", desconto)
            valor_total_desconto = (produto - desconto)
            print("Valor total com desconto R$", valor_total_desconto)

    elif opc == 2:
        comprar = int(input("Quantos Sabão liquido:"))
        produto = ProdutosDeLimpeza.sabaoLiquido * comprar
        print("Valor a pagar %2f"%produto)

        menu_pagamento()
        forma_pagamento = int(input("Qual a forma de pagamento:"))
        
        if forma_pagamento == 1:
            print("Forma de pagamento escolhida - Cartão de Crédito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 2:
            print("Forma de pagamento escolhida - Cartão de Débito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 3:
            print("Forma de pagamento escolhida - Dinheiro")
            print("Valor a pagar %2f"%produto, "Desconto de 10%")
            desconto = (produto * 10)/100
            print("Desconto de R$", desconto)
            valor_total_desconto = (produto - desconto)
            print("Valor total com desconto R$", valor_total_desconto)
    elif opc == 3:
        comprar = int(input("Quantos Amaciantes:"))
        produto = ProdutosDeLimpeza.amaciante * comprar
        print("Valor a pagar %2f"%produto)

        menu_pagamento()
        forma_pagamento = int(input("Qual a forma de pagamento:"))
        
        if forma_pagamento == 1:
            print("Forma de pagamento escolhida - Cartão de Crédito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 2:
            print("Forma de pagamento escolhida - Cartão de Débito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 3:
            print("Forma de pagamento escolhida - Dinheiro")
            print("Valor a pagar %2f"%produto, "Desconto de 10%")
            desconto = (produto * 10)/100
            print("Desconto de R$", desconto)
            valor_total_desconto = (produto - desconto)
            print("Valor total com desconto R$", valor_total_desconto)
    elif opc == 4:
        comprar = int(input("Quantos Sabão em pó:"))
        produto = ProdutosDeLimpeza.sabaoEmPo * comprar
        print("Valor a pagar %2f"%produto) 

        menu_pagamento()
        forma_pagamento = int(input("Qual a forma de pagamento:"))
        
        if forma_pagamento == 1:
            print("Forma de pagamento escolhida - Cartão de Crédito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 2:
            print("Forma de pagamento escolhida - Cartão de Débito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 3:
            print("Forma de pagamento escolhida - Dinheiro")
            print("Valor a pagar %2f"%produto, "Desconto de 10%")
            desconto = (produto * 10)/100
            print("Desconto de R$", desconto)
            valor_total_desconto = (produto - desconto)
            print("Valor total com desconto R$", valor_total_desconto)       
    elif opc == 5:
        comprar = int(input("Quantos Desinfetante:"))
        produto = ProdutosDeLimpeza.desinfetante * comprar
        print("Valor a pagar %2f"%produto)    

        menu_pagamento()
        forma_pagamento = int(input("Qual a forma de pagamento:"))
        
        if forma_pagamento == 1:
            print("Forma de pagamento escolhida - Cartão de Crédito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 2:
            print("Forma de pagamento escolhida - Cartão de Débito")
            print("Valor a pagar %2f"%produto)
        if forma_pagamento == 3:
            print("Forma de pagamento escolhida - Dinheiro")
            print("Valor a pagar %2f"%produto, "Desconto de 10%")
            desconto = (produto * 10)/100
            print("Desconto de R$", desconto)
            valor_total_desconto = (produto - desconto)
            print("Valor total com desconto R$", valor_total_desconto)            
    else:
        if opc > 5:
            print("Opção escolhida errada, escolhar entre 1 e 5")    
else:
    print("Obrigado, volte sempre")
    exit
