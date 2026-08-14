# Frequência de Palavras

frase = input("Digite uma frase: ")

# Transforma a frase em uma lista de palavras
palavras = frase.split()

# Dicionário para armazenar a quantidade de cada palavra
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

# Ordena as palavras da mais frequente para a menos frequente
ordenadas = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

print("\n=== Frequência de palavras ===")

for palavra, quantidade in ordenadas:
    print(f"{palavra} : {quantidade}x")

# Informações gerais
total_palavras = len(palavras)
palavras_unicas = len(contagem)

palavra_mais_frequente = ordenadas[0][0]
maior_frequencia = ordenadas[0][1]

print(f"\nTotal de palavras: {total_palavras}")
print(f"Palavras únicas: {palavras_unicas}")
print(f"Palavra mais frequente: {palavra_mais_frequente} ({maior_frequencia}x)")