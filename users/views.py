from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, UserProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Annonce, Commande
from .forms import AnnonceForm, CommandeForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})




@login_required
def dashboard(request):
    annonces = Annonce.objects.filter(owner=request.user)
    commandes = Commande.objects.filter(buyer=request.user)
    return render(request, 'users/dashboard.html', {'annonces': annonces, 'commandes': commandes})

@login_required
def create_annonce(request):
    if request.method == 'POST':
        form = AnnonceForm(request.POST)
        if form.is_valid():
            annonce = form.save(commit=False)
            annonce.owner = request.user
            annonce.save()
            return redirect('dashboard')
    else:
        form = AnnonceForm()
    return render(request, 'users/create_annonce.html', {'form': form})

@login_required
def edit_annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id, owner=request.user)
    if request.method == 'POST':
        form = AnnonceForm(request.POST, instance=annonce)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AnnonceForm(instance=annonce)
    return render(request, 'users/edit_annonce.html', {'form': form})

@login_required
def delete_annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id, owner=request.user)
    annonce.delete()
    return redirect('dashboard')



@login_required
def create_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            commande.buyer = request.user
            commande.save()
            return redirect('dashboard')
    else:
        form = CommandeForm()
    return render(request, 'users/create_commande.html', {'form': form})

@login_required
def edit_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id, buyer=request.user)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'users/edit_commande.html', {'form': form})

@login_required
def delete_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id, buyer=request.user)
    commande.delete()
    return redirect('dashboard')
