from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', register_view),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('homepage/', homepage_view),
    path('logout/', LogoutView.as_view(template_name='logout.html')),
]+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
