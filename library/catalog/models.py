from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):

    name = models.CharField(
        max_length=30, help_text='Insira um gênero (Ex.: Ficção Científica)')

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"pk": self.pk})


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, help_text='Insira uma breve descrição do livro')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='Identificação ISBN <a href="https://www.isbn-international.org/content/what-isbn">(Saber mais)</a>')
    genre = models.ManyToManyField(Genre, help_text='Selecione um gênero pra esse livro')
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def display_genre(self):
        return ','.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Chave individual do livro')
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=20)
    due_back = models.DateField(null=True, blank=True)
    
    loan_status = (
        ('m', 'Manutenção'),
        ('e', 'Em uso'),
        ('d', 'Disponível'),
        ('r', 'Reservado'),
    )
    
    status = models.CharField(
        max_length =1,
        choices = loan_status,
        blank=True,
        default='m',
        help_text='disponibilidade',
    )

    class Meta:
        verbose_name = "BookInstance"
        verbose_name_plural = "BookInstances"
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

    def get_absolute_url(self):
        return reverse("bookInstance_detail", kwargs={"pk": self.pk})

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})

class Language(models.Model):

    name = models.CharField(max_length=20, help_text='Qual o idioma original do livro?')

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Language_detail", kwargs={"pk": self.pk})
