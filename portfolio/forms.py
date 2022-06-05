from django.forms import ModelForm
from django import forms
from .models import Post
from .models import Quizz
from .models import Pessoa
from .models import Projetos
from .models import Formacao
from .models import Cadeiras
from .models import Noticias
from .models import Tecnologias
from .models import TrabalhosFinaisDeCurso


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        # ferramentas
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao...'}),
        }

        help_texts = {
            'autor': '↔ Insira neste campo o nome do autor',
            'titulo': '↔ Insira neste campo um titulo desejável',
            'descricao': '↔ Insira neste campo uma descrição a seu gosto',
            'link': '↔ Insira, somente se desejar, um link'
        }

        labels = {
            'autor': 'Autor',
            'titulo': 'Título',
            'descricao': 'Descrição',
            'link': 'Link que deseja inserir',
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome'}),
        }

        labels = {

            'nome': 'Qual o seu nome?',

            'pergunta1': 'Em que ano foi criado o HTML?',  # Em que ano foi criado o HTML (1991)

            'pergunta2': 'Em que ano foi criado o CSS?',  # Em que ano foi criado o CSS (1994)

            'pergunta3': 'Em que ano foi criado o Python?',  # Em que ano foi criado o Python (1989)

            'pergunta4': 'O que é o Django?',  # O que é o Django? (framework)

            'pergunta5': 'Em que ano foi criado o Django?',  # Em que ano foi criado o Django? (2005)

        }

        help_texts = {
        }


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome'}),
        }

        labels = {

            'nome': 'Qual o seu nome?',

            'link_linkedin': 'Se desejar, insira o seu link do linkedIn',

        }

        help_texts = {
        }


class ProjetosForm(ModelForm):
    class Meta:
        model = Projetos
        fields = '__all__'

        widgets = {
        }

        labels = {

            'imagem': 'Insira uma foto do seu projeto',

            'descricao': 'Insira a descrição do projeto',

            'cadeira': 'Qual a cadeira pertecente ao projeto',

            'ano_realizacao': 'Indique o ano de realização do projeto',

            'participantes': 'Participantes:',

            'link_github': 'Link do GitHub do projeto',

        }

        help_texts = {
        }


class FormacaoForm(ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

        widgets = {
            'semestre': forms.NumberInput(attrs={'min': '1', 'max': '2'}),
        }

        labels = {

            'nome_da_cadeira': 'Insira o nome da cadeira',

            'semestre': 'Insira o semestre da cadeira',

            'ects': 'Indique quantos ECTS vale a cadeira',

            'avaliacao': 'Indique a sua opinião sobre a cadeira',

            'total_ects': 'Indique o total de ECTS do semestre',

            'link_cadeira': 'Indique o link da cadeira',


        }

        help_texts = {
            'avaliacao': 'Utilize entre 1 a 5 (★)',
        }


class CadeirasForm(ModelForm):
    class Meta:
        model = Cadeiras
        fields = '__all__'

        widgets = {
        }

        labels = {

            'ano': 'Insira o ano da cadeira',

            'cadeiras': 'Insira as cadeiras que pretende',

            'total_ects': 'Indique o total de ECTS do semestre',

        }

        help_texts = {
            'total_ects': 'Soma de todos os ECTS deste semestre',
        }


class NoticiasForm(ModelForm):
    class Meta:
        model = Noticias
        fields = '__all__'

        widgets = {
        }

        labels = {

            'titulo': 'Insira o titulo da noticia',

            'descricao': 'Insira o texto da noticia',

            'imagem': 'Insira a imagem da noticia',

            'link_noticia': 'Insira o link da noticia',

        }

        help_texts = {
        }


class TecnologiasForm(ModelForm):
    class Meta:
        model = Tecnologias
        fields = '__all__'

        widgets = {
        }

        labels = {

            'nome': 'Insira o nome completo da tecnologia',

            'acronimo': 'Insira o acronimo',

            'ano_criacao': 'Insira a data de criação da tecnologia',

            'criador': 'Insira o criador',

            'logotipo': 'Insira o logotipo',

            'link_oficial': 'Insira o link da pagina oficial',

            'descricao': 'Insira uma pequena descricao',

        }

        help_texts = {

        }

class TrabalhosFinaisDeCursoForm(ModelForm):
    class Meta:
        model = TrabalhosFinaisDeCurso
        fields = '__all__'

        # ferramentas
        widgets = {
        }

        labels = {
            'autores': 'Autor(es)',
            'orientadores': 'orientadores',
            'ano': 'Ano de criação do trabalho',
            'titulo': 'Título',
            'resumo': 'Insira um pequeno resumo',
            'imagem': 'Insira uma imagem do trabalho',
            'relatorio': 'Insira o link do relatorio',
            'link_github': 'Insira o link do github',
        }

        help_texts = {
        }