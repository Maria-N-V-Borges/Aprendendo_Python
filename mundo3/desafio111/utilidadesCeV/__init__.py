"""
🧠 Por que o arquivo __init__.py existe?

Ele diz ao Python: “isso aqui é um pacote”

Sem ele:

- Python pode não reconhecer a pasta como pacote
- import utilidadesCeV pode falhar (principalmente em versões antigas)
"""

"""
🤔 Mas por que ele está vazio?

Porque:

- você não precisa colocar código nele agora
- ele já cumpre seu papel só existindo

📌 Pense assim:

O __init__.py é como a placa de identificação da pasta
"""

"""
🔧 Quando o __init__.py NÃO fica vazio?

- Em projetos maiores, ele pode:
- importar módulos automaticamente
- definir o que pode ser acessado
- inicializar configurações

Exemplo avançado:

from .moeda import resumo
"""
