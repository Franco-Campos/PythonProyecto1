from django.contrib import admin

# Register your models here.

from .models import Post, Commentary, Category

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "estado", "fecha_publicacion"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    search_fields = ["nombre"]
    ordering = ["nombre"]

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["texto", "post", "autor", "fecha_creacion"]
    list_filter = ["post", "autor"]
    search_fields = ["texto"]
    ordering = ["-fecha_creacion"]