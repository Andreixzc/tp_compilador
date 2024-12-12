# Gerador de Control Flow Graphs (CFG)

Este projeto gera Control Flow Graphs (CFGs) para programas C em diferentes níveis de otimização usando LLVM.

## Versões Utilizadas

- **Sistema Operacional:** Ubuntu 24.04.1 LTS
- **Clang:** Ubuntu clang version 18.1.3 (1ubuntu1)
- **LLVM:** Ubuntu LLVM version 18.1.3
- **Python:** 3.12.3

## Instalação de Dependências

Para instalar as dependências necessárias, execute os seguintes comandos:

```bash
sudo apt update
sudo apt install clang llvm python3 graphviz
```

Verifique as instalações com:

```bash
clang --version
llvm-config --version
python3 --version
dot -V
```

## Como Executar

### Para um programa específico:

Use o script `gen_cfg.py`:

```bash
python3 gen_cfg.py <caminho_do_arquivo.c>
```

Exemplo:

```bash
python3 gen_cfg.py Test.c
```

### Para todos os algoritmos na pasta src:

Use o script `gen_cfg_all.py`:

```bash
python3 gen_cfg_all.py src
```

Este script processará todos os arquivos .c encontrados na pasta `src` e suas subpastas.

## Estrutura do Projeto

- `gen_cfg.py`: Gera CFG para um programa C específico
- `gen_cfg_all.py`: Gera CFGs para todos os algoritmos na pasta `src`
- `src/`: Diretório contendo os arquivos fonte C a serem processados

## Saída

Os CFGs gerados serão salvos na pasta `output/` no formato PNG, organizados por arquivo fonte e nível de otimização.

## Notas Adicionais

- Certifique-se de que todos os arquivos C na pasta `src` estão compilando corretamente antes de executar os scripts
- Os níveis de otimização gerados são O0, O1, O2 e O3