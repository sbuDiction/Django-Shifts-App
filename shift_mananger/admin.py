from django.contrib import admin
from .models import Person, Shift, User, Days, Workers

# Register your models here.
# admin.site.register(Person)
admin.site.register(Shift)

class ShiftInline(admin.TabularInline):
    model = Shift
    extra = 7


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name','last_name',]}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})
    ]

    inlines = [ShiftInline]

    list_display = ('first_name', 'pub_date', 'was_published_recently',)

    list_filter = ['pub_date']

    search_fields = ['first_name']


admin.site.register(Person, PersonAdmin)
