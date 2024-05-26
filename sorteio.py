import random
from collections import Counter

# Função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Função para gerar números da sequência de Fibonacci até um limite
def numeros_fibonacci(limite):
    fibs = [1, 2]
    while True:
        proximo_fib = fibs[-1] + fibs[-2]
        if proximo_fib > limite:
            break
        fibs.append(proximo_fib)
    return fibs

# Função para contar repetições consecutivas de um número
def contar_repeticoes_consecutivas(numeros, num):
    contagem = 0
    max_contagem = 0
    for n in numeros:
        if n == num:
            contagem += 1
            if contagem > max_contagem:
                max_contagem = contagem
        else:
            contagem = 0
    return max_contagem

# Função para ler o histórico dos sorteios
def ler_historico_sorteios(nome_arquivo, num_ultimos_sorteios):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()[-num_ultimos_sorteios:]
    numeros = [int(num) for linha in linhas for num in linha.split()[2:]]
    return numeros

# Função para obter os números mais frequentes, respeitando o limite de repetições consecutivas
def obter_numeros_mais_frequentes(numeros, num_mais_frequentes, max_repeticoes_consecutivas):
    frequencia = Counter(numeros)
    mais_comuns = frequencia.most_common()
    numeros_selecionados = []
    
    for num, _ in mais_comuns:
        if len(numeros_selecionados) >= num_mais_frequentes:
            break
        if contar_repeticoes_consecutivas(numeros, num) <= max_repeticoes_consecutivas:
            numeros_selecionados.append(num)
    
    return numeros_selecionados

# Função para gerar um sorteio
def gerar_sorteio(quantidade, min_pares, min_impares, min_primos, min_div3, min_div5, numeros_borda, min_borda, fibs, min_fibonacci, min_soma, max_soma, ultimo_sorteio, min_repeticoes, numeros_frequentes, sorteios_validos, max_numeros_iguais):
    while True:
        numeros_restantes = list(set(range(1, 26)) - set(numeros_frequentes))
        sorteio_base = random.sample(numeros_restantes, quantidade - len(numeros_frequentes))
        sorteio = sorteio_base + numeros_frequentes
        
        # Verifica se o novo sorteio não é muito semelhante aos sorteios anteriores
        if any(sum(1 for num in sorteio if num in sorteio_anterior) > max_numeros_iguais for sorteio_anterior in sorteios_validos):
            continue  # Pula para a próxima geração de sorteio se for muito semelhante
        
        # Verifica os critérios
        contagem_pares = sum(1 for x in sorteio if x % 2 == 0)
        contagem_impares = sum(1 for x in sorteio if x % 2 != 0)
        contagem_primos = sum(1 for x in sorteio if eh_primo(x))
        contagem_div3 = sum(1 for x in sorteio if x % 3 == 0)
        contagem_div5 = sum(1 for x in sorteio if x % 5 == 0)
        contagem_borda = sum(1 for x in sorteio if x in numeros_borda)
        contagem_fibonacci = sum(1 for x in sorteio if x in fibs)
        soma_total = sum(sorteio)
        contagem_repeticoes = sum(1 for x in sorteio if x in ultimo_sorteio)
        
        if (contagem_pares >= min_pares and contagem_impares >= min_impares and contagem_primos >= min_primos and 
            contagem_div3 >= min_div3 and contagem_div5 >= min_div5 and contagem_borda >= min_borda and
            contagem_fibonacci >= min_fibonacci and min_soma <= soma_total <= max_soma and contagem_repeticoes >= min_repeticoes):
            return sorteio

# Função para contar quantos números do sorteio estão no resultado esperado
def contar_acertos(sorteio, resultado_esperado):
    return sum(1 for x in sorteio if x in resultado_esperado)

# Função principal
def main():
    quantidade = 15
    min_pares = 5
    min_impares = 7
    min_primos = 3
    min_div3 = 3
    min_div5 = 2
    limite_de_sorteios = 500
    numeros_borda = [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25]
    min_borda = 8
    limite_fibonacci = 25
    fibs = numeros_fibonacci(limite_fibonacci)
    min_fibonacci = 3
    min_soma = 198
    max_soma = 208
    min_repeticoes = 8
    quantidade_de_sorteios_historico = 10
    quantidade_de_numeros_que_mais_sairam_nos_ultimos_sorteios = 7
    max_repeticoes_consecutivas = 5
    
    sorteios_validos = []
    max_numeros_iguais = 13
    
    nome_arquivo = 'historico_sorteios.txt'    
    resultado_esperado = [7, 6, 14, 19, 13, 3, 21, 23, 1, 24, 16, 17, 9, 20, 10]

    custo_sorteio = 2.5
    premio = {11: 6, 12: 12, 13: 30, 14: 1450, 15: 1500000}

    numeros_do_historico = ler_historico_sorteios(nome_arquivo, quantidade_de_sorteios_historico)    
    numeros_frequentes = obter_numeros_mais_frequentes(numeros_do_historico, quantidade_de_numeros_que_mais_sairam_nos_ultimos_sorteios, max_repeticoes_consecutivas)
    ultimo_sorteio = ler_historico_sorteios(nome_arquivo, 1)  # Lê o último sorteio especificamente

    total_sorteios = 0
    custo_total = 0
    resultado = 0
    acertos = Counter()
    premios = Counter()
    
    while total_sorteios < limite_de_sorteios:
        sorteio = gerar_sorteio(quantidade, min_pares, min_impares, min_primos, min_div3, min_div5, numeros_borda, min_borda, fibs, min_fibonacci, min_soma, max_soma, ultimo_sorteio, min_repeticoes, numeros_frequentes, sorteios_validos, max_numeros_iguais)
        if sorteio:
            sorteios_validos.append(sorteio)  # Armazena cada sorteio válido para comparação futura
            acertos_no_sorteio = contar_acertos(sorteio, resultado_esperado)
            total_sorteios += 1
            custo_total += custo_sorteio
        
        if acertos_no_sorteio >= 11:  # Conta apenas acertos de 11 ou mais
            acertos[acertos_no_sorteio] += 1
            premios[acertos_no_sorteio] += premio[acertos_no_sorteio]
        
        if acertos_no_sorteio >= 11:
            print(f"Sorteio num: {total_sorteios}º com {acertos_no_sorteio} acertos: {sorteio}")
    
    # Imprime os resultados
    print(f"\nTotal de sorteios: {total_sorteios}, Custo total: ${custo_total}")
    for k in sorted(acertos.keys()):
        print(f"Acertos {k}: {acertos[k]} vezes, Total prêmios: ${premios[k]}")
    
    print(f"Total de todos os prêmios: ${sum(premios.values())}")
    
    resultado = (sum(premios.values()) - custo_total)
    print(f"\nResultado = {resultado}")

if __name__ == "__main__":
    main()
