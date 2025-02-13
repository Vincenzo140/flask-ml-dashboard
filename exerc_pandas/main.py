import pandas as pd

# aqui vai o arquivo que voce quer ler
df = pd.read_csv('vendas.csv')


# aqui ele faz a multiplicação da quantidade pelo preço unitário
df['faturamento'] = df['quantidade'] * df['preco_unitario']
faturamento_por_produto = df.groupby('produto')['faturamento'].sum()


# aqui ele pega o produto com maior e menor faturamento
maior_faturamento = faturamento_por_produto.idxmax()
menor_faturamento = faturamento_por_produto.idxmin()

# e aqui printa com as informações
print(f"Faturamento por produto:\n{faturamento_por_produto}")
print(f"\nProduto com maior faturamento: {maior_faturamento}")
print(f"Produto com menor faturamento: {menor_faturamento}")
