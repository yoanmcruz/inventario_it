from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class CustomUser(AbstractUser, PermissionsMixin):
    # Por ahora no se añaden campos personalizados.
    # Esta clase se usa para tener un modelo de usuario extensible.
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'