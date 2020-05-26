from django.contrib import admin
from .models import Category,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 
    list_display = ('title', 'autor', 'published', 'post_categories') # Mostrar columnas
    ordering = ('autor', 'published') # Forma de ordenar
    search_fields = ('title', 'content', 'autor__username', 'categories__name') # Realizar busqueda
    date_hierarchy = ('published') # Publicacion del contenido de una mejor forma
    list_filter = ('autor__username', 'categories__name')  # Filtros de busqueda

    # Mostrar categorias
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)