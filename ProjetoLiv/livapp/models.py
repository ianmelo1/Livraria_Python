from django.db import models

class Livro(models.Model):
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    isbn = models.IntegerField()
    numeroPaginas = models.IntegerField()
    titulo = models.CharField(max_length=100)
    anoPublicacao = models.IntegerField()
    emailEditora = models.EmailField()

    def __str__(self):
        return self.titulo

