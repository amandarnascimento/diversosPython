# Cálculo Simples
# https://judge.beecrowd.com/pt/problems/view/1010


num_produtos = int(input("Quantos produtos você deseja inserir? "))

subtotais = []
total_geral = 0.0


while num_produtos > 0:

    id_produto = int(input("Digite o código do produto: "))
    qnt_produto = int(input("Digite a quantidade: "))
    valor_produto = float(input("Digite o preço unitário: "))


    subtotal = qnt_produto * valor_produto

    #armazenar resultado
    subtotais.append(subtotal)

    #adicionar o subtotal em total geral
    total_geral = total_geral + subtotal

    # Decrementa o contador de produtos 
    num_produtos -= 1

# Exibe o valor total geral
print(f"Valor total geral: R$ {total_geral:.2f}")

# Opcional para exibir os subtotais dos produtos
print("Subtotais por produto:")
for i, subtotal in enumerate(subtotais, start=1):
    print(f"Produto {i}: R$ {subtotal:.2f}")


