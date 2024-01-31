from django.shortcuts import render
from .forms import Register_form
from .models import Books_model
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User Registered Successfully")
        else:
            return HttpResponse("User is not Registered!")
    else:
        form = Register_form()
        return render(request, 'register.html', {'form': form})


class Book_detail(DetailView):
    model = Books_model
    template_name = 'details.html'
    context_object_name = 'Book'


class Book_list(ListView):
    model = Books_model
    fields = '__all__'
    template_name = 'homepage.html'
    context_object_name = 'Book'


@login_required(login_url='/login/')
def homepage_view(request):
    return render(request, 'homepage.html')
