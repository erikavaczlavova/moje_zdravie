from django.contrib import admin

# Register your models here.

from projekt.models import *
admin.site.register(Test)
admin.site.register(Vaccine)
admin.site.register(User)
admin.site.register(Passport)
