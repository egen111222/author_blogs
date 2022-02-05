"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from connection.views import get_message
from connection.views import thanks
from django_registration.backends.activation.views import RegistrationView
from blog.forms import AuthorForm

urlpatterns = [
    path('',include('blog.urls')),
    #path('accounts/',include('enter_user.urls')),
    path('accounts/register/',
        RegistrationView.as_view(
            form_class=AuthorForm
        ),
        name='django_registration_register',
    ),
    path('admin/', admin.site.urls),
    path('get_message/',get_message,name='get_message'),
    path('thanks/',thanks,name='thanks'),
    path('auth/', include('django.contrib.auth.urls')),

]













