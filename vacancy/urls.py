from django.urls import path

from .views import get_all_vacancies, vacancy_detail

app_name = 'vacancy'

urlpatterns = [
    path('', get_all_vacancies, name='vacancies'),
    path('vacancy/<int:pk>', vacancy_detail, name='vacancy')
]
