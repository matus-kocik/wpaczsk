from django.views.generic import TemplateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from media.models import Image
from content.models import Article


    
class ListOfMembersView(TemplateView):
    template_name = "account/list_of_members.html"

class RegisterView(View):
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, 'main/home.html', {
            'register_form': form,
            'login_form': CustomAuthenticationForm(),
            "home_page_card_images": Image.objects.filter(card_item=True, template_name="home"),
            "home_page_card_articles": Article.objects.all().order_by("-publication_date")[:3],
        })


class LoginView(View):
    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Úspešne si sa prihlásil, {user.first_name}!')
            return redirect('home')
        return render(request, 'main/home.html', {
            'login_form': form,
            'register_form': CustomUserCreationForm(),
            "home_page_card_images": Image.objects.filter(card_item=True, template_name="home"),
            "home_page_card_articles": Article.objects.all().order_by("-publication_date")[:3],
        })


