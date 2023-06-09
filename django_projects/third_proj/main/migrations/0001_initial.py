# Generated by Django 4.2.1 on 2023-05-30 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('article', models.IntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Notebook',
                'verbose_name_plural': 'Notebooks',
            },
        ),
    ]
