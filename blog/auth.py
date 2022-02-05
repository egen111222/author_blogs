from django.contrib.auth.backends import BaseBackend
from .models import Author

class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Author.objects.get(username=username)
            if user.check_password(password):
                return user
        except Author.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            user = Author.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except Author.DoesNotExist:
            return None
            
        
