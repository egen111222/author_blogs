from django.contrib.auth import authenticate 
from django.contrib.auth import login as log_user

from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView # дозволяє отримувати
                                                 # генеровані функції
from .forms import UserForm
from django.shortcuts import redirect

from django.contrib.auth import logout

from blog.models import Author


class Create_User(CreateView):
    model = Author # що будемо створювати
    fields = ['email','password','age']
    template_name = 'create.html' # сторінка з формою
    success_url = '/thanks/' # після успошного додавання
    def form_success(self):
        def form_valid(self, form):
            form.password = Author.set_password(form.password)


def login(request):
    if request.method == "POST": # якщо запит був надісланицй з форми
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None: # якщо коритсувач Є 
            log_user(request , user)
            return redirect('/')
    return render(request,'create.html',context={'form':UserForm})


def log_out(request):
    logout(request)
    return redirect('login')





