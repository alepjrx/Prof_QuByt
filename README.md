EM CONSTRUÇÃO

**** Prof QuByt - Chatbot de estudos ****
---
---
 O Prof. QuByt é um chatbot de linha de comando feito em Python para auxiliar nos estudos em programação.
 
Funcionalidades:
 - Tópicos como variáveis, loops e etc.
 - Sistema de progresso
 - Quizzes
 - Tudo salvo localmente em arquivos .json

Objetivo:
Projeto que serve como ferramenta de estudo e portfólio inicial.

---

Estrutura do projeto:

prof-qubyt/ 
├── qubyt/
│ ├── init.py
│ ├── main.py
│ ├── knowledge_base.py
│ ├── progress.py
│ ├── quiz.py
│ └── utils.py (em breve)
├── data/
│ ├── init.py
│ └── progress.json
├── README.md
└── requirements.txt

---

Como rodar:

1 - Clone o repositório:


git clone https://github.com/alepjrx/prof-qubyt.git

cd prof-qubyt


2 - Crie e ative um ambiente virtual:

python -m venv venv

source venv/bin/activate #linux/macOS

venv\Scripts\activate

3 - Instale as dependências:

pip install -r requirements.txt

4 - Rode o bot:

python -m qubyt.main