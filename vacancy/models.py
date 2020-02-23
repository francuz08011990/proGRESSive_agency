from django.db import models


class Country(models.Model):
    title = models.CharField('Название страны', max_length=200)

    class Meta:
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    MALE = 'Мужчины'
    FEMALE = 'Женщины'
    MALE_FEMALE = 'Мужчины/Женщины'
    GENDER_CHOICES = (
        (MALE, 'Мужчины'),
        (FEMALE, 'Женщины'),
        (MALE_FEMALE, 'Мужчины/Женщины')
    )

    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.CASCADE, related_name='vacancies')
    title = models.CharField('Заголовок', max_length=200)
    city = models.CharField('Город', max_length=200)
    description = models.TextField('Описание', max_length=2000)
    additional_information = models.TextField('Дополнительная информация', max_length=2000)
    age = models.CharField('Возраст', max_length=100)
    gender = models.CharField('Пол', choices=GENDER_CHOICES, max_length=100, default=MALE)
    salary = models.CharField('Зарплата', max_length=100)
    residence = models.CharField('Проживание', max_length=200)
    working_hours = models.CharField('Рабочие часы', max_length=200)
    image = models.ImageField('Фото вакансии', upload_to='vacancy_images', blank=True, null=True)

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class CallRequest(models.Model):
    WORK = 'Pабота'
    INSURANCE = 'Страховка'
    REASON_CHOICES = (
        (WORK, 'Работа'),
        (INSURANCE, 'Страховка')
    )
    name = models.CharField('Имя', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=50)
    call_back = models.BooleanField('Перезвонил', default=False)
    reason = models.CharField('Причина заявки', choices=REASON_CHOICES, max_length=100, default=WORK)

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки на обратный звонок'

    def __str__(self):
        return self.name + ' ({0})'.format(self.phone_number)
