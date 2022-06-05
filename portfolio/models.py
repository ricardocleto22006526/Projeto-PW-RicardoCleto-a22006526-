from django.db import models


# Create your models here.


class Post(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=400)
    link = models.URLField(max_length=200, blank=True)

    # imagem = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.autor} no {self.data}, adicionou um {self.titulo} com a{self.descricao} e com link {self.link}"


class Quizz(models.Model):
    nome = models.CharField(max_length=50)
    pergunta1 = models.IntegerField(default=0)  # Em que ano foi criado o HTML (1991)
    pergunta2 = models.IntegerField(default=0)  # Em que ano foi criado o CSS (1994)
    pergunta3 = models.IntegerField(default=0)  # Em que ano foi criado o Python (1989)
    pergunta4 = models.CharField(max_length=50)  # O que é o Django? (framework)
    pergunta5 = models.IntegerField(default=0)  # Em que ano foi criado o Django? (2005)

    def __str__(self):
        return f"{self.nome}"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    link_linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome}"


class Projetos(models.Model):
    nome_do_projeto = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='media/', null=True)
    descricao = models.CharField(max_length=500)
    cadeira = models.CharField(max_length=100)
    ano_realizacao = models.IntegerField(default=0)
    participantes = models.ManyToManyField(Pessoa)
    link_github = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome_do_projeto}"


class Cadeiras(models.Model):
    nome_da_cadeira = models.CharField(max_length=100)
    semestre = models.IntegerField(default=1)
    ects = models.IntegerField(default=0)
    avaliacao = models.CharField(max_length=100, blank=True)
    link_cadeira = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome_da_cadeira}"


class Formacao(models.Model):
    ano = models.IntegerField(default=0)
    cadeiras = models.ManyToManyField(Cadeiras)
    total_ects = models.CharField(max_length=100)

    def __str__(self):
        return f"O {self.ano} ano tem {self.total_ects} ECTS"


class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400)
    imagem = models.ImageField(upload_to='media/', null=True)
    link_noticia = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"Noticia: {self.titulo}"


class Tecnologias(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=20)
    ano_criacao = models.IntegerField(default=0)
    criador = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='media/', null=True)
    link_oficial = models.URLField(max_length=200, blank=True)
    descricao = models.CharField(max_length=400)

    def __str__(self):
        return f"Tecnologia: {self.nome}"


class TrabalhosFinaisDeCurso(models.Model):
    autores = models.ManyToManyField(Pessoa, related_name='autores')
    orientadores = models.ManyToManyField(Pessoa, related_name='orientadores')
    ano = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100)
    resumo = models.CharField(max_length=400)
    imagem = models.ImageField(upload_to='media/', null=True)
    relatorio = models.URLField(max_length=200, blank=True)
    link_github = models.URLField(max_length=200, blank=True)
    link_video = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"Trabalho Final de Curso: {self.titulo}"
