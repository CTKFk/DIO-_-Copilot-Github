# data_input = input()

# def converter_para_dia_mes_ano(data_str):
#     ano, dia,mes  = data_str.split("-")
#     return f"{dia}/{mes}/{ano}"

# if "-" in data_input and len(data_input) == 10:
#     print(converter_para_dia_mes_ano(data_input))
# else:
#     print("Formato de data inválido")
# def verificar_anagrama(palavra1, palavra2):
#     palavra1 = palavra1.replace(" ", "").lower()
#     palavra2 = palavra2.replace(" ", "").lower()

#     return sorted(palavra1) == sorted(palavra2)
#   ---------------------------------------------------------------------------------------------------------------------------
# def main():
#     entrada = input().strip()

#     palavras = entrada.split()
    
#     palavra_a, palavra_b = palavras[0], palavras[1]

#     if verificar_anagrama(palavra_a, palavra_b):
#         print("Verdadeiro");
#     else:
#         print("Falso")

# if __name__ == "__main__":
#     main()
#   ---------------------------------------------------------------------------------------------------------------------------
def calcular_moda(lista):
    frequencias = {}
    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    
    maior_frequencia = max(frequencias.values())
    modas = [num for num, freq in frequencias.items() if freq == maior_frequencia]
    
    return modas

entrada = input()
dados = list(map(int, entrada.split()))

modas = calcular_moda(dados)

if len(modas) > 1:
    print(" ".join(map(str, modas)))
else:
    print(modas[0])