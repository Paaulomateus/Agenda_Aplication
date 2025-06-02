Iniciar projeto Trabalho Django

```
criei o ambiente virtual
    python -m venv venv(coloquei o nome venv mesmo)
ativando o ambiente virtual
    venv\Scripts\activate
instalando o django
    pip install django
startando o django
    django-admin startproject projetoFacul . 

python manage.py startapp contact

```

configurando o git
tem que ter o git instalado 

```

git config --global user.name 'Paulo Mateus'
git config --global user.email 'paulo.fiden96@gmail.com'
git config --global init.defaultBranch main
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```

Migrando a base de dados do Django

toda vez que alterar o model usa o makemigrations
```
python manage.py makemigrations
python manage.py runserver
python manage.py migrate
```

``` Criando e modificando a senha um super usuário```

``` 
python manage.py createsuperuser
python manage.py changepassword USARNAME

```

``` python
# import modulo
from contact.models import Contact
# cria um contato
# retorna um contato
contact = Contact(**fields)
contact.save()
# cria um contato não lazy
# retorna um cantato
contact = Contact.objects.create(**fields)
# seleciona um contato com id
# retorna o contato
contact = Contact.objects.ge(fk=10)
# Edita o contato
# retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name1 = 'Novo valor 2'
contact.save()
# apaga o contato
# depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# seleciona todos os contatos ordenando por id DESC
# retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySelect[]
contacts = Contact.objects.filter(**filters).order_by('-id')
```