from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.urls import reverse

# Create your views here.
from .forms import PostForm
from .models import Post
from .models import Quizz
from .forms import Projetos
from .forms import QuizzForm
from .forms import Formacao
from .forms import Noticias
from .forms import Tecnologias


from .funcoesQuizz import desenha_grafico_resultados


def about_view(request):
    return render(request, 'portfolio/about.html')


def apresentacao_view(request):
    return render(request, 'portfolio/apresentação.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_view(request):
    context = {'formacao': Formacao.objects.all(), 'cadeiras': Formacao.cadeiras}

    return render(request, 'portfolio/formação.html', context)


def home_view(request):
    agora = datetime.datetime.now()

    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)


def index_view(request):
    return render(request, 'portfolio/layout.html')


def programacaoWeb_view(request):
    context = {'noticias': Noticias.objects.all(), 'tecnologias': Tecnologias.objects.all()}

    return render(request, 'portfolio/programacaoWeb.html', context)


def projetos_view(request):
    context = {'projetos': Projetos.objects.all(), 'pessoa': Projetos.participantes}

    return render(request, 'portfolio/projetos.html', context)


def blog_view(request):
    context = {'post': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)


# PÁGINA DO QUIZZ
def quizz_view(request):
    desenha_grafico_resultados(Quizz.objects.all())

    form = QuizzForm(request.POST, use_required_attribute=False)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)

    context = {
        'form': form,
    }

    return render(request, 'portfolio/quizz.html', context)


# PÁGINAS DO BLOG
def view_novo_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/nova.html', context)


def view_editar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


def view_apaga_post(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))
