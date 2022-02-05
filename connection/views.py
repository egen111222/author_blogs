from django.shortcuts import render
from django.http import HttpResponse
from .models import Social
from .models import MenuItem
from .models import Message
from django.shortcuts import redirect
from .middleware import check_menu_items
from django.views.generic.edit import CreateView

menu = MenuItem.objects.all()
social = Social.objects.all()

class CreateMessage(CreateView):
    template_name = 'create.html'
    model = Message
    success_url = '/thanks'


def get_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        message = Message(name = name,email=email,message=message)
        message.save()
        return redirect('thanks')
    return redirect('main_page')


@check_menu_items
def thanks(request):
    return render(request,'thanks.html')







