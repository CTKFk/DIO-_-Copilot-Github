import re

def validar_bandeira_cartao(numero_cartao):
    numero_cartao = numero_cartao.replace(" ", "")  # Remove espaços em branco
    bandeiras = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Enroute": r"^(2014|2149)\d{11}$",
        "Aura": r"^50[0-9]{14,17}$",
        "Hipercard": r"^606282\d{10}(\d{3})?$",
        "Voyager": r"^8699[0-9]{11}$"
    }

    for bandeira, padrao in bandeiras.items():
        if re.match(padrao, numero_cartao):
            return bandeira
    return "Bandeira desconhecida"

if __name__ == "__main__":
    numero_cartao = input("Digite o número do cartão: ")
    bandeira = validar_bandeira_cartao(numero_cartao)
    print(f"A bandeira do cartão é: {bandeira}")

# # Exemplo de uso
# numero_cartao = "3836 249232 5394"
# bandeira = validar_bandeira_cartao(numero_cartao)
# print(f"A bandeira do cartão é: {bandeira}")
