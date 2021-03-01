from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Livro(models.Model):

    nome = models.CharField("Nome do Livro", max_length=50)
    autor = models.CharField("Autor", max_length=50)
    copias = models.PositiveIntegerField("Cópias em estoque")

    def __str__(self):
        return self.name

class Reserva(models.Model):

    leitor = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField("Data da Solicitação", default=timezone.now)
    dias_reserva = models.PositiveIntegerField("Dias pra reserva")
    data_aprovacao = models.DateTimeField("Data da Aprovação")
    pedido_aprovado = models.BooleanField("Pedido Aprovado", default=False)

    def __str__(self):
        return self.livro + " - " + data_solicitacao

    def save(self, *args, **kwargs):
        if self.pedido_aprovado:
            self.data_aprovacao = timezone.now

        super().save(*args, **kwargs)

