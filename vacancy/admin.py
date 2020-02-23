from django.contrib import admin

from .models import Country, Vacancy, CallRequest


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'gender', 'salary', 'residence')
    search_fields = ('title', 'city')
    list_filter = ('country', 'gender', 'salary', 'residence')
    list_display_links = ('title',)
    fieldsets = [
        (None, {'fields': ['title', 'description', 'additional_information', 'image']}),
        ('Требования', {'fields': ['age', 'gender', 'salary', 'residence', 'working_hours']}),
        ('Местоположение', {'fields': ['country', 'city']})
    ]


@admin.register(CallRequest)
class CallRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'reason', 'phone_number', 'call_back')
    search_fields = ('name', 'phone_number')
    list_display_links = ('name',)
