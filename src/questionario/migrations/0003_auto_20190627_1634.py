# Generated by Django 2.2 on 2019-06-27 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionario', '0002_auto_20190514_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='pontos',
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='questionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perguntas', to='questionario.Questionario'),
        ),
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField()),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionario.Pergunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
