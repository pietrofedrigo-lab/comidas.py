
notas = [10, 3, 5]
nota_final = 0.0

# O len(notas) garante que o range vá até o tamanho exato da lista (3 itens)
for i in range(len(notas)):
    print(f"Nota {i + 1}: {notas[i]}")
    nota_final += notas[i]

print("-" * 15)
print(f"Soma total: {nota_final}")
notas = [10, 3, 5]
nota_final = 0.0

for i in range(len(notas)):
    nota_final += notas[i]

media = nota_final / len(notas)

print(f"Soma das notas: {nota_final}")
print(f"Média final: {media:.2f}")
notas = [10, 3, 5]

nota_final = sum(notas)
media = nota_final / len(notas)

print(f"Soma: {nota_final}")
print(f"Média: {media:.2f}")