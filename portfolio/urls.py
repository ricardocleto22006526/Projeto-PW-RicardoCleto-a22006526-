from django.urls import path
from . import views

app_name = 'portfolio'
name = 'home'

urlpatterns = [
    path('', views.home_view),
    path('about', views.about_view, name='sobre'),
    path('apresentacao', views.apresentacao_view, name='apresentação'),
    path('competencias', views.competencias_view, name='competencias'),
    path('formacao', views.formacao_view, name='formação'),
    path('home', views.home_view, name='home'),
    path('index', views.index_view, name='index'),
    path('projetos', views.projetos_view, name='projetos'),
    path('blog', views.blog_view, name='blog'),
    path('nova', views.view_novo_post, name='nova'),
    path('edita/<int:post_id>', views.view_editar_post, name='edita'),
    path('apaga/<int:post_id>', views.view_apaga_post, name='apaga'),
    path('quizz', views.quizz_view, name='quizz'),
    path('programacaoWeb', views.programacaoWeb_view, name='programacaoWeb'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('apiEEI', views.API_EEI_view, name='apiEEI'),
]
