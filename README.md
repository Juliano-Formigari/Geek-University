# Geek-University

Repositório com o objetivo de registrar os conteúdos absorvidos na plataforma Geek University.

# To see
    - Explorar funcionalidade do SHELL, juntamente com as bibliotecas;
        python manage.py shell
            from django.db import models
            dir(models)
            help(models)
# Comandos
    - python -m venv venv;
        Ativar o ambiente virtual com o comando: source venv/Scripts/activate;
    - pip install Django;
    - pip freeze > requirements.txt;
    - django-admin startproject firstproject .;
    - django-admin startapp core;
    - python manage.py createsuperuser;

    - python manage.py - Comando para visualizar as opções disponíveis;
    - python manage.py help migrate - Comando para visualizar as opções disponíveis no comando migrate;
    - python manage.py shell - Comando para exibir mais informações detalhadas no terminal;
    - pip install whitenoise gunicorn;
    - pip install django-bootstrap4;
    - pip install PyMySQL;
    - pip install MySQL;
    - pip install django-stdimage;
    - pip install dj_database_url - Utilizado para passar as configurações default do banco de dados para o heroku;
    - pip install psycopg2-binary - Driver de conexão para o banco de dados;
    - pip install dj-static
    - pip uninstall whitenoise - Comando para remover uma biblioteca instalada;
    - pip install django-adminlte2:
        No INSTALLED_APPS adicionar os dois app abaixo:
            'django_adminlte'
            'django_adminlte_theme'

    - python manage.py test;
    - pip install model_mommy;
    - pip install coverage;
        Dentro da raiz do projeto criar um arquivo chamado '.coveragerc'
            Adicionar dentro do arquivo o comando abaixo:
                [run]
                source = .
    - coverage run manage.py test;
    - coverage report;
    - coverage html;
    - rm -rf htmlcov - Comando para remover um diretório;
    - python -m http.server - Comando para visualizar o coverage;
    - pip install textblob

# Etapas publicação do projeto
    - Mudar o modo DEBUG para 'False';
    - ALLOWED_HOSTS: Configurar o dominio do site neste campo;
    - Instalar as bibliotecas whitenoise e gunicorn;
        whitenoise: Django por padrão não gerencia arquivos estaticos em produção, então essa biblioteca tem essa função;
        gunicorn: Executa os comandos para rodar a aplicação;
    - No arquivo settings, adicionar o campo 'whitenoise.middleware.WhiteNoiseMiddleware';
    - No arquivo settings, configurar o STATIC_ROOT e comentar o campo EMAIL_BACK_END;
    - Gerar o arquivo requirements.txt;
    
    - Para publicar no heroku é preciso criar um arquivo runtime.txt e adicionar a versão do python nele;
        runtime.txt --> python-0.0.0
    - Criar arquivo Procfile e adicionar o comando gunicorn nele;
        Procfile --> web: gunicorn django_basico.wsgi --log-file -
    - Executar o comando heroku login para fazer a autenticação;
    - Executar o comando heroku create django-basico.jlf --buildpack heroku/python;

# Etapas de inicialização do projeto
    - Criar um ambiente virtual;
    - Fazer instalação das bibliotecas a serem utilizadas;
    - Criar um projeto e caso tenha sido criado o diretório, utilizar o '.' no final do comando;
    - Criar o app core;
    - Rodar o comando para gerar o requirements;
    - Fazer as devidas configurações no arquivo de settings:
        Diretório STATIC e configurar diretório media para arquivos estaticos;
        Diretório templates;
        Configuração do BD;
        Configuração do idioma e timezone;
        Instalar os apps;
    - Configurar URLs com o diretório media;
    - No arquivo wsgi, configurar o Cling e MediaCling;
    - Configurar o template de logout;
