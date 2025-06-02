Agenda
# Agenda_Aplication
# 📒 Agenda de Contatos (Projeto Final)

  Este projeto é uma agenda de contatos que permite realizar as operações básicas de um CRUD: Criar, Listar, Editar e Excluir contatos. Foi desenvolvido como parte de um trabalho acadêmico, com o objetivo de praticar conceitos de desenvolvimento web utilizando Django e FastAPI.
  
  ## 🔧 Tecnologias Utilizadas
  
    - Django – Framework web principal utilizado para o backend e estrutura do projeto;
    - FastAPI – Utilizado para expor APIs rápidas e assíncronas;
    - SQLite – Banco de dados utilizado (padrão do Django);
    - HTML/CSS – Utilizado na estrutura e estilização frontend do projeto.
  
  ## 🚀 Funcionalidades
  
    - ✅ Cadastrar novos contatos;
    - ✅ Listar todos os contatos cadastrados;
    - ✅ Editar dados de um contato;
    - ✅ Excluir contatos;
    - ✅ API com FastAPI para manipulação de dados via requisições HTTP (GET, POST, PUT, DELETE).
  
  ## 🧑‍💻 Participantes
  
    - Luan Henrique da Costa Alves;
    - Mathews Vinicius de Oliveira;
    - Paulo Mateus Farias Carreiro.
  
  Este projeto foi desenvolvido com fins educacionais, com o objetivo de aplicar conhecimentos de back-end e construção de APIs RESTful com Django e FastAPI.

  ## ▶️ Como Executar o projeto

    - Clone o repositório e acesse a pasta:
    - git clone https://github.com/Paaulomateus/Agenda_Aplication.git
    - cd Agenda_Aplication

    - Crie e ative um ambiente virtual:
    - python -m venv venv
    - source venv/bin/activate (ou venv\Scripts\activate no Windows)

    - Instale as dependências:
    - pip install -r requirements.txt

    - Aplique as migrações:
    - python manage.py migrate

    - Inicie o servidor Django:
    - python manage.py runserver

    - (Se aplicável) Inicie a API FastAPI:
    - uvicorn api:app --reload
