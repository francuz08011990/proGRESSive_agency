from django.shortcuts import render
from .models import Country, Vacancy, CallRequest


def get_all_vacancies(request):
    template_name = 'vacancy/vacancies.html'
    country_list = Country.objects.all()
    context = {'countries': country_list}

    return render(request, template_name, context)


def vacancy_detail(request, pk):
    template_name = 'vacancy/single-page.html'
    vacancy = Vacancy.objects.get(id=pk)
    data = {'vacancy': vacancy}

    return render(request, template_name, data)


def create_back_call(request):
    data = {}
    user_data = request.POST

    try:
        if 'callBack' in user_data:
            CallRequest.objects.create(
                name=user_data['name'],
                phone_number=user_data['phone']
            )
        else:
            CallRequest.objects.create(
                name=user_data['name'],
                phone_number=user_data['phone'],
                reason='Страховка'
            )
    except:
        data['error'] = 'Что то пошло не так!'
    else:
        data['message'] = 'В ближайшее время мы Вам перезвоним.'
    return render(request, 'vacancy/index.html', data)
