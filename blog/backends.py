from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
import logging
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password


class AuthorBackends(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.filter(email=username).order_by('id').first()
            if user.check_password(password):
                return user
            return None
        except:
            return None


    def get_user(self, user_id):
        User = get_user_model()
        try:
            print(User.objects.get(pk=user_id))
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
