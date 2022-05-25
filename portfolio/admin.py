from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Quizz
from .models import Pessoa
from .models import Projetos
from .models import Formacao
from .models import Cadeiras
from .models import Noticias
from .models import Tecnologias


class ProjetosHorizontal(admin.ModelAdmin):
    filter_horizontal = ('participantes',)


class CadeirasHorizontal(admin.ModelAdmin):
    filter_horizontal = ('cadeiras',)


admin.site.register(Post)
admin.site.register(Quizz)
admin.site.register(Pessoa)
admin.site.register(Projetos, ProjetosHorizontal)
admin.site.register(Formacao, CadeirasHorizontal)
admin.site.register(Cadeiras)
admin.site.register(Noticias)
admin.site.register(Tecnologias)
