# Generated by Django 4.1.7 on 2023-04-01 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0045_remove_emprestimos_categoria_livros_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
