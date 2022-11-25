# Geek-University

Repositório com o objetivo de registrar os conteúdos absorvidos na plataforma Geek University.

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

# Etapas publicação do projeto
    - Mudar o modo DEBUG para 'False';
    - ALLOWED_HOSTS: Configurar o dominio do site neste campo;
    - Instalar as bibliotecas whitenoise e gunicorn;
        whitenoise: Django por padrão não gerencia arquivos estaticos em produção, então essa biblioteca tem essa função;
        gunicorn: Executa os comandos para rodar a aplicação;
    - No arquivo settings, adicionar o campo 'whitenoise.middleware.WhiteNoiseMiddleware';
    - No arquivo settings, configurar o STATIC_ROOT;
    - Gerar o arquivo requirements.txt;
    
    - Para publicar no heroku é preciso criar um arquivo runtime.txt e adicionar a versão do python nele;
        runtime.txt --> python-0.0.0
    - Criar arquivo Procfile e adicionar o comando gunicorn nele;
        Procfile --> web: gunicorn django_basico.wsgi --log-file -
    - Executar o comando heroku login para fazer a autenticação;
    - Executar o comando heroku create django-basico.jlf --buildpack heroku/python;