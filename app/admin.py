from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Genero, Livro

#
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1  
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome',)
    inlines = [LivroInline] 
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome',)
    inlines = [LivroInline] 
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [LivroInline] 

admin.site.register(Cidade)
admin.site.register(Leitor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Genero, GeneroAdmin)


admin.site.register(Livro)