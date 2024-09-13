from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Annonce, Commande
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Votre adresse email'}),
        label='Adresse email'
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Numéro de téléphone'}),
        label='Numéro de téléphone'
    )
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'accept': 'image/*'}),
        label='Photo de profil'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'phone_number', 'profile_picture')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Une utilisateur avec cet email existe déjà.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Le numéro de téléphone ne doit contenir que des chiffres.")
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nom d’utilisateur'})
        self.fields['role'].widget.attrs.update({'class': 'form-select'})
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-control-file'})
        for field in self.fields:
            self.fields[field].help_text = None

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Votre adresse email'}),
        label='Adresse email'
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Numéro de téléphone'}),
        label='Numéro de téléphone'
    )
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'accept': 'image/*'}),
        label='Photo de profil'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'profile_picture']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Une autre utilisateur a déjà utilisé cet email.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Le numéro de téléphone ne doit contenir que des chiffres.")
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nom d’utilisateur'})
        self.fields['username'].help_text = 'Nom d’utilisateur unique'
        self.fields['phone_number'].help_text = 'Votre numéro de téléphone (optionnel)'
        self.fields['profile_picture'].help_text = 'Téléchargez une photo de profil (optionnel)'
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].label = self.fields[field].label or field.capitalize()

        # Special styling for profile picture field
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-control-file'})

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['title', 'description', 'price', 'image']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Le prix doit être supérieur à 0.')
        return price

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['annonce', 'quantity', 'status']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise ValidationError('La quantité doit être supérieure à 0.')
        return quantity
