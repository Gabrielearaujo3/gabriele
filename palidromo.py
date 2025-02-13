def eh_palindromo (palavra):

 palavra = palavra.replace("", "").lower()
 return palavra == palavra[::-1]

def encontrar_palindromos (texto):
 palavras = texto.split()
 palindromos = [palavra for palavra in palavras if eh_palindromo (palavra)]
 return palindromos

texto = "Este é um texto sem palindromos."
palindromos = encontrar_palindromos (texto)

if palindromos:
 print("com palidromos:")
 for palindromo in palindromos:
  print(palindromo)
else:
 print("sem palidromos.")