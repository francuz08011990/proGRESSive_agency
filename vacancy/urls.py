from django.urls import path
from django.views.generic import TemplateView

from .views import get_all_vacancies, vacancy_detail

app_name = 'vacancy'

urlpatterns = [
    path('', TemplateView.as_view(template_name='vacancy/index.html'), name='index'),
    path('vacancies', get_all_vacancies, name='vacancies'),
    path('vacancy/<int:pk>', vacancy_detail, name='vacancy')
]
