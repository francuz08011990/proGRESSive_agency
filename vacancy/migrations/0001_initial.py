# Generated by Django 2.2.8 on 2019-12-14 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('call_back', models.BooleanField(default=False, verbose_name='Перезонил')),
            ],
            options={
                'verbose_name_plural': 'Заявки',
                'verbose_name': 'Заявка',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название страны')),
            ],
            options={
                'verbose_name_plural': 'Страны',
                'verbose_name': 'Страна',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('additional_information', models.TextField(max_length=2000, verbose_name='Дополнительная информация')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('male', 'мужчины'), ('female', 'женщины'), ('male/female', 'мужчины/женщины')], default='male', max_length=100, verbose_name='Пол')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('residence', models.CharField(max_length=200, verbose_name='Проживание')),
                ('working_hours', models.CharField(max_length=200, verbose_name='Рабочие часы')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.Country', verbose_name='Страна')),
            ],
            options={
                'verbose_name_plural': 'Вакансии',
                'verbose_name': 'Вакансия',
            },
        ),
    ]
