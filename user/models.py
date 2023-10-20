from django.db import models
from group.models import Group


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
