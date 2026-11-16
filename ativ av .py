 # Listas iniciais fornecidas no desafio
itens = ["pizza", "suco", "bolo", "refrigerante"] #
precos = [10, 5, 7, 8] #[cite: 4]
total_compra = 0

print("--- Cardápio da Cantina ---")
# 1. Mostrar os itens do cardápio e os seus preços[cite: 4]
for i in range(len(itens)):
    print(f"{i} - {itens[i]} (Preço: {precos[i]})")

print("\nDigite -1 a qualquer momento para encerrar o pedido.") #[cite: 4]

# 2. Permitir, com while, que os utilizadores escolham os itens pelo número[cite: 4]
while True:
    escolha = int(input("\nEscolha o número do item: "))

    # 4. Encerrar a escolha ao digitar -1[cite: 4]
    if escolha == -1:
        break
    
    # Validar se o número escolhido existe na lista
    if 0 <= escolha < len(itens):
        # 3. Somar o valor de cada item escolhido[cite: 4]
        total_compra += precos[escolha]
        print(f"-> {itens[escolha]} adicionado(a) com sucesso!")
    else:
        print("-> Opção inválida. Por favor, escolha um número do cardápio.")

# 5. Mostrar o valor total da compra[cite: 4]
print("\n--- Resumo do Pedido ---")
print(f"O valor total da sua compra é: {total_compra}") #[cite: 4]














