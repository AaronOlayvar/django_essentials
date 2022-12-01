from django.contrib import admin
from . import models
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display =('title',)  #this changed the name from 'Notes object (1)' changing it to the title i inputted in the admin page

admin.site.register(models.Notes, NotesAdmin)

# this displays the models in admin site