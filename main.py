# base da url = https://bytebank.com/cambio
# parametro da url = moedaOrigem=real&moedaDestino=dolar&quantidade=100

# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
# print(url)

# #################################################

# url = "https://bytebank.com/cambio?moedaOrigem=real"
# print(url)

# url_base = url[0:19]
# print(url_base)

# url_parametros = url[20:36]
# print(url_parametros)

#################################################


# url = "bytebank.com/cambio?moedaOrigem=real"
# print(url)

# url_base = url[0:19]
# print(url_base)

# url_parametros = url[20:36]
# print(url_parametros)

# print(url)
# "https://bytebank.com/cambio?moedaOrigem=real"

#################################################

# url = "https://bytebank.com/cambio?moedaOrigem=real"
# print(url)

# indice_interrogacao = url.find("?")
# url_base = url[0:indice_interrogacao]
# print(url_base)

# url_parametros = url[indice_interrogacao+1:36]
# print(url_parametros)

#################################################

# url = "https://bytebank.com/cambio?moedaOrigem=real"
# print(url)

# indice_interrogacao = url.find("?")
# url_base = url[:indice_interrogacao]
# print(url_base)

# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)

#################################################

# url = "https://bytebank.com/cambio?moedaOrigem=real"

# indice_interrogacao = url.find("?")
# url_base = url[:indice_interrogacao]
# print(url_base)

# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)

#################################################

# url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

# indice_interrogacao = url.find("?")
# url_base = url[:indice_interrogacao]

# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)

#################################################

# url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

url = ""

# Sanitização da URL
url = url.replace(" ", "")

# validação da url
if url == "":
    raise ValueError("A URL esta vazia")

# Separa base e os parâmetros
# indice_interrogacao = url.find("?")
# url_base = url[:indice_interrogacao]

# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)

# # busca o valor de um parâmetro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
print(indice_valor)
indice_e_comercial = url_parametros.find("&", indice_valor)

if indice_e_comercial == -1:
  valor = url_parametros[indice_valor:]
  print(valor)
else:
  valor = url_parametros[indice_valor:indice_e_comercial]
  print(valor)
