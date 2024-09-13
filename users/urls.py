from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('annonces/create/', views.create_annonce, name='create_annonce'),
    path('annonces/<int:annonce_id>/edit/', views.edit_annonce, name='edit_annonce'),
    path('annonces/<int:annonce_id>/delete/', views.delete_annonce, name='delete_annonce'),
    path('commande/create/', views.create_commande, name='create_commande'),
    path('commande/edit/<int:commande_id>/', views.edit_commande, name='edit_commande'),
    path('commande/delete/<int:commande_id>/', views.delete_commande, name='delete_commande'),

]
