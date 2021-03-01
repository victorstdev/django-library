from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Livro, Reserva, User
from .forms import CadastrarLivroForm, UpdateLivroForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_livros"] = Livro.objects.count()
        return context

# Livros
class LivroListView(ListView):
    model = Livro
    template_name = "lista_livros.html"
    context_object_name = 'livros'
    paginate_by = 10

class LivroDetailView(DetailView):
    model = Livro
    template_name = "detalhes_livro.html"
    context_object_name = 'livro'

@method_decorator(login_required, name='dispatch')
class LivroCreateView(CreateView):
    model = Livro
    template_name = "cadastrar_livro.html"
    form_class = CadastrarLivroForm
    success_url = reverse_lazy('biblioteca')

@method_decorator(login_required, name='dispatch')    
class LivroUpdateView(UpdateView):
    model = Livro
    template_name = "atualizar_livro.html"
    success_url = reverse_lazy('biblioteca')

# Reservas
@method_decorator(login_required, name='dispatch')
class ReservaListView(ListView):
    model = Reserva
    template_name = "lista_reservas.html"
    context_object_name = 'reservas'

@method_decorator(login_required, name='dispatch')
class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "detalhes_reserva.html"
    context_object_name = 'reserva'

@method_decorator(login_required, name='dispatch')
class ReservaCreateView(CreateView):
    model = Reserva
    template_name = "cadastrar_reserva.html"

