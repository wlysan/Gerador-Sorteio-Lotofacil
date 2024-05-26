# Gerador de Sorteios Lotofacil

Este projeto é um gerador de sorteios que seleciona números de acordo com critérios específicos e verifica se há correspondência com um resultado esperado.
Ele pode ser adaptado tanto para gerar uma lista de jogos, tanto quanto para simular um lista de jogos e checar qual teria sido o resultado referente o esperado.

## Requisitos

- Python 3.x
- Biblioteca `collections` (incluída na biblioteca padrão do Python)

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um arquivo `historico_sorteios.txt` na raiz do projeto com o histórico de sorteios.

3. Execute o script:
    ```bash
    python sorteio.py
    ```

## Estrutura do Código

### Funções

#### `eh_primo(n)`
Verifica se um número é primo.
- **Parâmetro:** `n` (int) - número a ser verificado.
- **Retorno:** `True` se o número for primo, caso contrário, `False`.

#### `numeros_fibonacci(limite)`
Gera números da sequência de Fibonacci até um limite.
- **Parâmetro:** `limite` (int) - valor máximo para os números de Fibonacci.
- **Retorno:** Lista de números de Fibonacci até o limite.

#### `contar_repeticoes_consecutivas(numeros, num)`
Conta repetições consecutivas de um número em uma lista.
- **Parâmetros:** 
  - `numeros` (list) - lista de números.
  - `num` (int) - número a ser contado.
- **Retorno:** Maior número de repetições consecutivas de `num` na lista.

#### `ler_historico_sorteios(nome_arquivo, num_ultimos_sorteios)`
Lê o histórico dos sorteios de um arquivo.
- **Parâmetros:**
  - `nome_arquivo` (str) - nome do arquivo que contém o histórico.
  - `num_ultimos_sorteios` (int) - número de sorteios a serem lidos do final do arquivo.
- **Retorno:** Lista de números dos sorteios.

#### `obter_numeros_mais_frequentes(numeros, num_mais_frequentes, max_repeticoes_consecutivas)`
Obtém os números mais frequentes respeitando um limite de repetições consecutivas.
- **Parâmetros:**
  - `numeros` (list) - lista de números.
  - `num_mais_frequentes` (int) - quantidade de números mais frequentes a serem retornados.
  - `max_repeticoes_consecutivas` (int) - limite máximo de repetições consecutivas permitido.
- **Retorno:** Lista de números mais frequentes respeitando o limite de repetições consecutivas.

#### `gerar_sorteio(quantidade, min_pares, min_impares, min_primos, min_div3, min_div5, numeros_borda, min_borda, fibs, min_fibonacci, min_soma, max_soma, ultimo_sorteio, min_repeticoes, numeros_frequentes, sorteios_validos, max_numeros_iguais)`
Gera um sorteio de números de acordo com critérios específicos, lembrando que critérios muito travados ou mal definidos podem dificultar ou não gerar a quantidade limite de sorteios estipulada.
- **Parâmetros:**
  - `quantidade` (int) - quantidade de números no sorteio.
  - `min_pares` (int) - número mínimo de números pares.
  - `min_impares` (int) - número mínimo de números ímpares.
  - `min_primos` (int) - número mínimo de números primos.
  - `min_div3` (int) - número mínimo de números divisíveis por 3.
  - `min_div5` (int) - número mínimo de números divisíveis por 5.
  - `numeros_borda` (list) - lista de números considerados de borda.
  - `min_borda` (int) - número mínimo de números de borda.
  - `fibs` (list) - lista de números de Fibonacci.
  - `min_fibonacci` (int) - número mínimo de números de Fibonacci.
  - `min_soma` (int) - soma mínima dos números do sorteio.
  - `max_soma` (int) - soma máxima dos números do sorteio.
  - `ultimo_sorteio` (list) - lista dos números do último sorteio.
  - `min_repeticoes` (int) - número mínimo de números que devem se repetir do último sorteio.
  - `numeros_frequentes` (list) - lista de números mais frequentes.
  - `sorteios_validos` (list) - lista de sorteios válidos anteriores.
  - `max_numeros_iguais` (int) - número máximo de números iguais permitidos em relação aos sorteios anteriores.
- **Retorno:** Lista de números do sorteio que atendem aos critérios especificados.

#### `contar_acertos(sorteio, resultado_esperado)`
Conta quantos números do sorteio estão no resultado esperado.
- **Parâmetros:**
  - `sorteio` (list) - lista de números do sorteio.
  - `resultado_esperado` (list) - lista de números do resultado esperado.
- **Retorno:** Número de acertos.

### Variáveis

#### `quantidade`
Quantidade de números no sorteio.

#### `min_pares`
Número mínimo de números pares.

#### `min_impares`
Número mínimo de números ímpares.

#### `min_primos`
Número mínimo de números primos.

#### `min_div3`
Número mínimo de números divisíveis por 3.

#### `min_div5`
Número mínimo de números divisíveis por 5.

#### `limite_de_sorteios`
Número máximo de sorteios a serem gerados.

#### `numeros_borda`
Lista de números considerados de borda.

#### `min_borda`
Número mínimo de números de borda.

#### `limite_fibonacci`
Limite máximo para os números de Fibonacci.

#### `fibs`
Lista de números de Fibonacci até o limite especificado.

#### `min_fibonacci`
Número mínimo de números de Fibonacci.

#### `min_soma`
Soma mínima dos números do sorteio.

#### `max_soma`
Soma máxima dos números do sorteio.

#### `min_repeticoes`
Número mínimo de números que devem se repetir do último sorteio.

#### `quantidade_de_sorteios_historico`
Número de sorteios a serem lidos do histórico.

#### `quantidade_de_numeros_que_mais_sairam_nos_ultimos_sorteios`
Quantidade de números mais frequentes a serem retornados.

#### `max_repeticoes_consecutivas`
Limite máximo de repetições consecutivas permitido.

#### `sorteios_validos`
Lista de sorteios válidos anteriores.

#### `max_numeros_iguais`
Número máximo de números iguais permitidos em relação aos sorteios anteriores.

#### `nome_arquivo`
Nome do arquivo que contém o histórico de sorteios.

#### `resultado_esperado`
Lista de números do resultado esperado.

#### `custo_sorteio`
Custo de cada sorteio.

#### `premio`
Dicionário contendo a premiação para diferentes números de acertos.

## Exemplo de Uso

O código lê um histórico de sorteios, seleciona os números mais frequentes respeitando um limite de repetições consecutivas, e gera novos sorteios que atendem a diversos critérios. Os sorteios são comparados com um resultado esperado e os acertos são contados.

O resultado final inclui o número de sorteios realizados, o custo total, e os prêmios ganhos, se houver.

## Resultados

O script imprime os sorteios válidos, o número de acertos e o resultado financeiro baseado no custo dos sorteios e nos prêmios ganhos.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos recursos. Faça um fork do projeto, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.
