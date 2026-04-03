# 1. Dicionario com as palavras e seus significados
meme_dict = {
    "STALKEAR":  "Investigar a vida de alguem online",
    "CRINGE":    "Algo vergonhoso ou constrangedor",
    "VDD":       "Abreviacao da palavra verdade",
    "BISCOITAR": "Postar algo apenas para chamar a atencao",
    "HATER":     "Pessoa que esta constantemente criticando os outros",
    "VLW":       "Abreviacao da palavra valeu",
    "SHIP":      "Torcer para que duas pessoas fiquem juntas",
    "SALTY":     "Pessoa amargurada ou com raiva de algo",
    "DELULU":    "Alguem que vive em uma realidade distorcida",
    "LOWKEY":    "De forma discreta, sem chamar muita atencao",
}

# 2. Saudacao e instrucoes
print("=" * 45)
print("  BEM-VINDO AO DICIONARIO DE GIRIAS!")
print("=" * 45)
print("Aqui voce descobre o significado das")
print("palavras modernas que voce nao entende.")
print("Digite a palavra em LETRAS MAIUSCULAS.")
print("-" * 45)

# 3. Loop para perguntar 5 palavras
for i in range(1, 6):
    print("\nPesquisa " + str(i) + " de 5")

    # 4. Obter a solicitacao do usuario
    word = input("Digite uma palavra moderna: ").upper()

    # 5. Processar e retornar a explicacao
    if word in meme_dict.keys():
        print("Significado de " + word + ": " + meme_dict[word])
    else:
        print("A palavra '" + word + "' nao foi encontrada no dicionario.")

# 6. Mensagem de encerramento
print("\n" + "=" * 45)
print("  Obrigado por usar o Dicionario de Girias!")
print("  Ate a proxima! VLW!")
print("=" * 45)
