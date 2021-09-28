# Generated by Django 3.1.3 on 2021-01-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_requestedbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Öğrenci İsmi', max_length=100, verbose_name='Öğrenci Adı')),
                ('surname', models.CharField(help_text='Öğrenci Soyadı', max_length=100, verbose_name='Öğrenci Soyadı')),
                ('student_num', models.CharField(help_text='Öğrenci Numarası', max_length=20, verbose_name='Öğrenci Numarası')),
                ('contact_num', models.CharField(help_text='iletişim Numarası', max_length=20, verbose_name='İletişim Numarası')),
            ],
            options={
                'verbose_name_plural': 'Student Info',
                'ordering': ['id'],
            },
        ),
    ]
