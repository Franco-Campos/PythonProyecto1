from django import forms
from .models import Post
from .models import Commentary 
from .models import Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "estado"]
        
class CommentaryForm(forms.ModelForm):
    class Meta:
        model= Commentary
        fields = ["texto"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields = ["nombre", "descripcion"]
