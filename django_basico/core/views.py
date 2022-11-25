from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web Django Framework',
        'outro': 'Django é massa',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def erro404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def erro500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)