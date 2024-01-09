from django.contrib import admin

# Register your models here.
from wizchat.models import Chat, Message

admin.site.register(Message)
admin.site.register(Chat)