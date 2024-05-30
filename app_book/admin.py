from django.contrib import admin
from app_book.models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

class BookAdmine(admin.ModelAdmin):
    pass
admin.site.register(Books, ProfileAdmin)