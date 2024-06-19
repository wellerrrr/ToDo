from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateField(auto_now=True)

    groups = models.ManyToManyField(Group, related_name='user_set', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username