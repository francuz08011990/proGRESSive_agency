# Generated by Django 2.2.8 on 2020-02-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0003_auto_20200125_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='callrequest',
            options={'verbose_name': 'Заявку', 'verbose_name_plural': 'Заявки на обратный звонок'},
        ),
        migrations.AddField(
            model_name='callrequest',
            name='reason',
            field=models.CharField(choices=[('Pабота', 'Работа'), ('Страховка', 'Страховка')], default='Pабота', max_length=100, verbose_name=''),
        ),
    ]
