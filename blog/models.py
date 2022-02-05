from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class AuthorManager(BaseUserManager):
    def create_user(self, email,age, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            age=age,
        )

        user.set_password(password)
        print(user.password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,age, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            age=age,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class Author(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    age = models.IntegerField()
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AuthorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['age']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        print('IS ADMIN',self.is_admin)
        return self.is_admin





'''
class Author(AbstractUser):
    age = models.IntegerField()
    
'''


class Article(models.Model):
    title = models.CharField(max_length=51)
    text = models.TextField()
    image = models.ImageField(upload_to='static/')
    publication = models.DateField()
    author = models.ManyToManyField(Author)
















