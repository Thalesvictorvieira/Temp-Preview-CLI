# Skymio CLI ☁️

Aplicação de linha de comando (CLI) escrita em Python para consultar **previsões meteorológicas** diretamente do terminal.

O programa utiliza a API do **WeatherAPI** para fornecer:

* Condições meteorológicas atuais
* Previsão para os próximos dias
* Exibição da data no formato brasileiro
* Exibição do dia da semana

---

# 📌 Funcionalidades

✔ Consulta da **temperatura atual**
✔ Previsão do tempo para **até 3 dias**
✔ Exibição da **cidade pesquisada**
✔ Exibição da **data formatada (DD/MM/AAAA)**
✔ Exibição do **dia da semana em português**
✔ Interface simples via **terminal (CLI)**
✔ Armazenamento automático da chave da API

---

# 🖥️ Exemplo de uso

```text
Qual das opções abaixo você deseja utilizar?
1 - Previsão do tempo atual
2 - Previsão do tempo para os próximos dias
3 - Sair
Digite o número da opção desejada: 1

Digite o nome da cidade para obter a previsão do tempo atual: Belo Horizonte

Cidade: Belo Horizonte
Temperatura: 26 °C
Condição: Parcialmente nublado
```

Exemplo de previsão futura:

```text
Cidade: Belo Horizonte
Data: 18/03/2026
Dia: Terça-feira
Temperatura média: 25 °C
Previsão: Ensolarado
```

---

# ⚙️ Requisitos

* Python 3.10 ou superior
* Biblioteca `requests`

---

# 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/skymio-cli.git
```

Entre na pasta do projeto:

```bash
cd skymio-cli
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# 🚀 Executando o programa

Execute o script:

```bash
python skymio.py
```

Na primeira execução o programa solicitará sua **chave da API**.

---

# 🔑 Obtendo a chave da API

1. Acesse o site da **WeatherAPI**
2. Crie uma conta gratuita
3. Copie sua **API Key**
4. Cole no programa quando solicitado

A chave será salva automaticamente no arquivo:

```text
SaveApiKey.txt
```

---

# 📂 Estrutura do projeto

```text
skymio-cli
│
├── skymio.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# 🛠 Tecnologias utilizadas

* Python
* Biblioteca `requests`
* API WeatherAPI
* Interface CLI (Command Line Interface)

---

# 💡 Melhorias futuras

* Suporte para mais dias de previsão
* Versão com argumentos CLI (ex: `skymio bh 2`)
* Interface com cores no terminal
* Empacotamento como ferramenta instalável via pip

---

# 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

---

# 👨‍💻 Autor

Desenvolvido por **Thales Vieira**

Estudante de Ciência da Computação e desenvolvedor Python.
