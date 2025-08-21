from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('livro_list/', livro_list, name='listar_livros'),
    path('livro_new/', livro_new, name='livro_new'),
    path('livro_edit/<int:pk>/', livro_edit, name='livro_edit'),
    path('livro_remove/<int:pk>/', livro_remove, name='livro_remove'),
]