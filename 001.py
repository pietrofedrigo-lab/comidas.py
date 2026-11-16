# Listas exigidas no desafio
itens = ["pizza", "suco", "bolo", "refrigerante"]
precos = [10, 5, 7, 8]
total_compra = 0

print("--- Cardápio da Cantina ---")
# Mostrar os itens do cardápio e os seus preços
for i in range(len(itens)):
    print(f"{i} - {itens[i]}: R$ {precos[i]}")

# Estrutura de repetição condicional (while)
while True:
    escolha = int(input("\nEscolha o número do item (ou -1 para encerrar): "))

    # Encerrar a escolha ao digitar -1
    if escolha == -1:
        break
    
    # Validar se o número digitado existe no cardápio
    if 0 <= escolha < len(itens):
        # Somar o valor de cada item escolhido
        total_compra += precos[escolha]
        print(f"-> {itens[escolha]} adicionado(a) com sucesso!")
    else:
        print("-> Opção inválida. Digite um número válido do cardápio.")

# Mostrar o valor total da compra
print(f"\nO valor total da sua compra é: R$ {total_compra}")