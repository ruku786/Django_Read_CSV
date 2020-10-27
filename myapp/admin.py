from django.contrib import admin
from .models import Person, Person_detail


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','email','location']


@admin.register(Person_detail)
class Person_detailAdmin(admin.ModelAdmin):
    list_display = ['address', 'birth_date', 'phone', ]

#admin.site.register(Person)
#admin.site.register(Person_detail)

# Register your models here.
