from django.shortcuts import render
from .models import Country, Vacancy, CallRequest


def get_all_vacancies(request):
    template_name = 'vacancy/vacancies.html'
    country_list = Country.objects.all()
    context = {'countries': country_list}

    return render(request, template_name, context)


def vacancy_detail(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    data = {'vacancy': vacancy}

    return render(request, 'vacancy/single-page.html', data)


def create_back_call(request):
    data = {}
    user_data = request.POST

    try:
        CallRequest.objects.create(
            name=user_data['name'],
            phone_number=user_data['phone']
        )
    except:
        data['error'] = 'Что то пошло не так!'
    else:
        data['message'] = 'Спасибо, в ближайшее время мы Вам перезвоним'
    return render(request, 'vacancy/index.html', data)
