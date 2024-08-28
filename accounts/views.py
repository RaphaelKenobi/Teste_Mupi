from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.contrib import messages


# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('home')

        else:
            print('invalid registration details')

    return render(request, "registration/register.html", {"form": form})

class LandingView(TemplateView):
    template_name = 'landing.html'
