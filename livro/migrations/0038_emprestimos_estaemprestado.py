# Generated by Django 4.1.7 on 2023-03-29 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0037_remove_emprestimos_emprestar'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='estaEmprestado',
            field=models.BooleanField(default=False),
        ),
    ]
