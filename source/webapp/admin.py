from django.contrib import admin

from django.contrib import admin
from webapp.models import Poll, Choise

class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question','created_at']
    exclude = []
    readonly_fields = ['created_at']


class ChoiseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text']
    exclude = []


admin.site.register(Poll, PollAdmin)
admin.site.register(Choise, ChoiseAdmin)
