# Manipulação de espaços e caracteres

texto = "   Python   "

print("Original:", repr(texto))
print("strip():", repr(texto.strip()))
print("lstrip():", repr(texto.lstrip()))
print("rstrip():", repr(texto.rstrip()))

arquivo = "teste.txt"

print("removeprefix():", arquivo.removeprefix("teste"))
print("removesuffix():", arquivo.removesuffix(".txt"))
