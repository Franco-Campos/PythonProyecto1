from django.shortcuts import render, redirect
from .models import Post, Commentary, Category  # Corregido para usar los modelos correctamente
from .forms import PostForm
from .forms import CommentaryForm
from .forms import CategoryForm  # Importación correcta de formularios

# Vista para listar publicaciones (Post)
def post_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        post_list = Post.objects.filter(titulo__icontains=busqueda)
    else:     
        post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', context={"posts": post_list})

# Vista para crear una nueva publicación
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect("blog:post_list")
            else:
                form.add_error(None, "Debes iniciar sesión para crear una publicación")    
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', context={"form": form}) 

# Vista para listar comentarios (Comentario)
def coment_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        coment_list = Commentary.objects.filter(texto__icontains=busqueda)  # Corregido el filtro
    else:     
        coment_list = Commentary.objects.all()
    return render(request, 'blog/coment_list.html', context={"coments": coment_list})

# Vista para crear un nuevo comentario
def coment_create(request):
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            if request.user.is_authenticated:
                comentario.autor = request.user
                comentario.save()
                return redirect("blog:coment_list")
            else:
                form.add_error(None, "Debes iniciar sesión para crear un comentario")
    else:
        form = CommentaryForm()
    return render(request, 'blog/coment_create.html', context={"form": form})

# Vista para listar categorías (Categoria)
def category_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        category_list = Category.objects.filter(nombre__icontains=busqueda)  # Corregido el filtro
    else:     
        category_list = Category.objects.all()
    return render(request, 'blog/category_list.html', context={"categories": category_list})

# Vista para crear una nueva categoría
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            if request.user.is_authenticated:
                categoria.autor = request.user
                categoria.save()
                return redirect("blog:category_list")
            else:
                form.add_error(None, "Debes iniciar sesión para crear una categoría")
    else:
        form = CategoryForm()
    return render(request, 'blog/category_create.html', context={"form": form})
