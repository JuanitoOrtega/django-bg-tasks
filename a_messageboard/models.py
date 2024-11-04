from django.db import models
from django.contrib.auth.models import User


class MessageBoard(models.Model):
    subscribers = models.ManyToManyField(User, related_name='messageboard', blank=True, verbose_name="Subscriptores")
    
    class Meta:
        verbose_name = "Subscriptor"
        verbose_name_plural = "Subscriptores"
    
    def __str__(self):
        return str(self.id)
    
    
class Message(models.Model):
    messageboard = models.ForeignKey(MessageBoard, on_delete=models.CASCADE, related_name="messages", verbose_name="Mensaje")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages", verbose_name="Autor")
    body = models.CharField(max_length=2000, verbose_name="Cuerpo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    
    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['-created']
        
    def __str__(self):
        return self.author.username