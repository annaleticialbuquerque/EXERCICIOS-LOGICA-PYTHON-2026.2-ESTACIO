# Substituição e formatação

texto = "Olá, Ana!"
print("replace():", texto.replace("Ana", "Maria"))

print("format():", "Meu nome é {}.".format("Ana"))

dados = {"nome": "Ana"}
print("format_map():", "Meu nome é {nome}.".format_map(dados))

texto_tab = "Nome:\tAna"
print("expandtabs():", texto_tab.expandtabs(8))

tabela = str.maketrans("abc", "123")
print("translate():", "abc".translate(tabela))
