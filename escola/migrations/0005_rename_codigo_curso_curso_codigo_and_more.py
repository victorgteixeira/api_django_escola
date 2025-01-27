# Generated by Django 5.0.3 on 2024-11-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_alter_curso_codigo_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='codigo_curso',
            new_name='codigo',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='ativo',
        ),
        migrations.AlterField(
            model_name='estudante',
            name='celular',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
