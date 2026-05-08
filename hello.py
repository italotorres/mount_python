#!/usr/bin/env python3
# Comentário de linha
"""Hello World Multi Linguas

Dependend da lingua configurada no ambiente o programam exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente ex:
   export LANG=pt_BR

Execução:
   python3 hello.py
            ou
   ./hello.py

"""
__version__ = "0.1.2"
__author__ = "Italo Torres"
__license__ = "Unlicense"
import os
# Dunder significa "Underline" duplo, no fim e no inicio da variavel
current_language = os.getenv("LANG", "en_US")[:5]
# snake case(Todas as letras em minusculo); Pascal case (alguma letra em maiusculo nos textos em menusculo)


msg = {
        "en_US": "Hello, World!",
        "pt_BR": "Olá, Mundo!",
        "it_IT": "Ciao, Mondo!",
        "es_SP": "Hola, Mundo!",
        "fr_FR": "Bonjour, Monde",

        }

print(msg[current_language]) # Comentário de final de linha

"""Comentario
multi
linhas
"""
