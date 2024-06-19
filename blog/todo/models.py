from django.db import models
from userauth.models import User


class ToDoList(models.Model):
    title = models.CharField('Title task', max_length=250)
    is_complete = models.BooleanField('Completed', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title