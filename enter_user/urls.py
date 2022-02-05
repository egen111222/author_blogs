from django.urls import path
from .views import Create_User
from .views import login
from .views import log_out


urlpatterns = [
    path('create_user/',Create_User.as_view()),
    path('login/',  login,   name='login'),
    path('logout/', log_out, name='logout'),
]
