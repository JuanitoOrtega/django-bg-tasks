from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    image = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Imagen')
    displayname = models.CharField(max_length=20, null=True, blank=True, verbose_name='Nombre a mostrar')
    info = models.TextField(null=True, blank=True, verbose_name='Información')
    newsletter_subscribed = models.BooleanField(default=True, verbose_name='Subscrito al Boletín')
    
    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username 
    
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'
