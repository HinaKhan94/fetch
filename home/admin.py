from django.contrib import admin
from .models import Messages

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = (
         'name', 'email', 'message'
    )
    search_fields = ['name', 'submission_date', 'message']

admin.site.register(Messages, MessageAdmin)