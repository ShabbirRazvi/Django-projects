from django.http import HttpResponse
from django.shortcuts import render
from .models import Register_model
from .forms import RegistrationForm
# Create your views here.


def register_views(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registered Successfully")
        else:
            return HttpResponse("Failed to register")
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
