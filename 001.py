# 1. Definição do cardápio
itens_de_comidas_do_cardapio = ['pizza', 'bolo', 'salgado', 'hamburguer']
itens_de_bebida_cardapio = ['suco', 'refrigerante', 'água', 'café']

# Adicionando novos itens sem repetir o que já existia na lista
itens_de_comidas_do_cardapio.append('pastel')
itens_de_comidas_do_cardapio.append('coxinha')

# Junta comidas e bebidas em uma lista só
cardapio_completo = itens_de_comidas_do_cardapio + itens_de_bebida_cardapio

print("Cardápio completo atualizado:")
print(cardapio_completo)

# 2. Pergunta ao usuário
item_desejado = input("\nO que você quer comer ou beber hoje? ").strip().lower()

# Verifica se o item está no cardápio
if item_desejado in cardapio_completo:
    print(f"Sua escolha '{item_desejado}' está no cardápio!")
else:
    print(f"O item '{item_desejado}' não está no cardápio.")

# 3. Teste de manipular a lista de nomes
lista_nomes = []
lista_nomes.append("pizza")
lista_nomes.remove("pizza")

print("\nLista de nomes final (deve estar vazia):")
print(lista_nomes)


