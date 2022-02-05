from django import forms
from .models import Article
from .models import Author
from django_registration.forms import RegistrationForm

class DateInput(forms.DateInput):
    input_type = "date"
    

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {'publication':DateInput()}

    def save(self, commit=True):
        """ Save user and create a pro account """
        instance = super(ArticleForm, self).save(commit=False)
        if commit:
            instance.save() # створення статті і заливка її до бази даних
            instance.author.add(Author.objects.get(id=1))  # додання даних до поля
        return instance


class AuthorForm(RegistrationForm):
    class Meta:
        model = Author
        fields = ['email','age','password']



    

