from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    informacoes = models.TextField()
    data_criacao=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
            verbose_name_plural = "Livros"