# Generated by Django 4.1.7 on 2023-04-01 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0046_livros_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
        ),
    ]