# Generated by Django 4.1.7 on 2023-03-25 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0019_remove_livros_emprestado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimos',
            options={'verbose_name': 'Emprestimo'},
        ),
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Livro'},
        ),
        migrations.RemoveField(
            model_name='emprestimos',
            name='emprestado',
        ),
        migrations.AddField(
            model_name='emprestimos',
            name='titulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros'),
        ),
    ]
