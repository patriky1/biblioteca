# Generated by Django 4.1.7 on 2023-03-18 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0010_turma_livros_turma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='nome_turma',
        ),
        migrations.AddField(
            model_name='turma',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
        migrations.AlterField(
            model_name='livros',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.turma'),
        ),
    ]