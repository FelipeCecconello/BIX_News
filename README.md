<h1 align="center">
     <a href="https://github.com/FelipeCecconello/BIX_News/" alt="repositorio"> Teste técnico BIX </a>
</h1>


## 💻 Sobre o teste
  O teste trata-se de um pequeno sistema de notícias usando Python e o frameword Django para o desenvolvimento.
  O projeto foi dividido em três apps Django, o "core" onde estão estão as configurações centrais do projeto, o "news" onde os modelos estão configurados,
  e o app "home" onde estão as views, os templates das páginas, urls e os arquivos estáticos.
  
  ---

## ⚙️ Funcionalidade

- [x] Utilizando o Django Admin é possível:
  - [x] criar e editar notícias
  - [x] criar e editar comentarios
  - [x] definir se as notícias serão postadas ou não
  - [x] apagar o cache
  - [x] criar e editar usuários

- [x] Os usuários tem acesso ao site, onde podem:
  - [x] navegar pelas páginas e notícias para ler os seus conteúdos
  - [x] deixar comentários em posts
  - [x] enviar um email para o "suporte" através de uma task celery

---

## 🎨 Template

O template utiliza HTML, CSS, JavaScript e Bootstrap

---

## 🚀 Como executar o projeto

O projeto utiliza o banco de dados SQLite, é necessario ter o armazenador de dados Redis instalado localmente para utilizar o serviço celery
pode ser baixado para Windows no link https://github.com/tporadowski/redis/releases

#### 🧭 Rodando a aplicação

```bash

# Clone este repositório

# Crie um ambiente virtual
$ python3 -m venv nome_da_venv

# Execute o script para iniciar a venv
$ ./pasta_da_venv/Scripts/activate

# Instale todos os pacotes do arquivo requirements.txt
$ pip install -r requirements.txt

# Execute a aplicação
$ python manage.py runserver

# A aplicação será aberta na porta:8000 - acesse http://127.0.0.1:8000

# Para acessar o django admin acesse http://127.0.0.1:8000/admin/
# O superuser "Felipe" com a senha "123" já está criado

# Para utilizar o serviço celery abra o redis-cli.exe localmente
# inicie o serviço celery
$ celery -A core.celery worker --pool=solo -l info

# O email será enviado para os emails dos usuarios cadastrados no sistema
```

---

