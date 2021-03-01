from django.urls import path
from .views import IndexView, LivroListView, LivroDetailView, LivroCreateView, ReservaListView, ReservaDetailView, ReservaCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('biblioteca/', LivroListView.as_view(), name='biblioteca'),
    path('biblioteca/<int:pk>', LivroDetailView.as_view(), name='livro'),
    path('biblioteca/cadastrar', LivroCreateView.as_view(), name='cadastrar_livro'),
    path('reservas/', ReservaListView.as_view(), name='reservas'),
    path('reservas/<int:pk>', ReservaDetailView.as_view(), name='reserva'),
    path('reservas/cadastrar', ReservaCreateView.as_view(), name='cadastrar_reserva'),
]
