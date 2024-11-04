from django.contrib import admin
from .models import MessageBoard, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'messageboard', 'author', 'created')
    list_display_links = ['author']
    search_fields = ('messageboard', 'author')
    list_per_page = 25


admin.site.register(MessageBoard)
admin.site.register(Message, MessageAdmin)