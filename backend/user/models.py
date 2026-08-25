
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, user_name, email, password, first_name, last_name, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        if not user_name:
            raise ValueError(_('You must provide an user name'))

        email = self.normalize_email(email)
        user = self.model(user_name=user_name, email=email,
                          first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_name, email, password, first_name, last_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        # Check if otherfields are set
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(user_name, email, password, first_name, last_name, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(verbose_name='User Name', max_length=255, unique=True)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    password = models.CharField(verbose_name='Password', max_length=255)

    first_name = models.CharField(verbose_name='First Name',max_length=255)
    last_name = models.CharField(verbose_name='Last Name', max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def clean(self):
        pass
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'