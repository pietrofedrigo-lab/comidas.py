# 1. Definição do cardápio com preços (Dicionário)
cardapio_precos = {
    'pizza': 10.0,
    'suco': 5.0,
    'bolo': 7.0,
    'refrigerante': 8.0
}

# Separação por categorias
comidas = ['pizza', 'bolo', 'salgado', 'hamburguer', 'pastel', 'coxinha']
bebidas = ['suco', 'refrigerante', 'água', 'café']
cardapio_completo = comidas + bebidas

print("--- CARDÁPIO COM PREÇOS ---")
for item, preco in cardapio_precos.items():
    print(f"item: {item}-preço R$ {preco:.0f}")

# Cálculo do valor total do cardápio
total_cardapio = sum(cardapio_precos.values())
print(f"valor total do cardápio R${total_cardapio:.0f}")

# 2. Pergunta ao usuário
item_desejado = input("\nO que você quer comer ou beber hoje? ").strip().lower()

if item_desejado in cardapio_precos:
    preco_item = cardapio_precos[item_desejado]
    print(f"Sua escolha '{item_desejado}' está no cardápio e custa R$ {preco_item:.0f}!")
elif item_desejado in cardapio_completo:
    print(f"Sua escolha '{item_desejado}' está no cardápio, mas não tem preço cadastrado.")
else:
    print(f"O item '{item_desejado}' não está no cardápio.")

# 3. Teste de manipulação de lista (sem erro de pop)
lista_nomes = []
lista_nomes.append("pizza")
lista_nomes.insert(0, "joao")

print("\nLista antes do pop:", lista_nomes)
lista_nomes.pop(1)  # Remove 'pizza' que está no índice 1
print("Lista final após pop(1):", lista_nomes) 


# --- CORREÇÕES APLICADAS AQUI ---
print("\nContagem do loop:")
for i in range(4):  # Mudado de 'in' para 'i'
    print(i)        # Indentação corrigida

# Definindo a variável antes de imprimir (pegando o último item da lista de comidas)
comida_final = comidas[-1] 
print("\nA comida final da lista é:", comida_final)











