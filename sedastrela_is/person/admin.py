from django.contrib import admin

from sedastrela_is.person.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'nick_name',
        'phone',
        'email',
        'mother_phone',
        'mother_email',
        'father_phone',
        'father_email',
    )


admin.site.register(Person, PersonAdmin)

