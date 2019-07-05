# Generated by Django 2.2.3 on 2019-07-05 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='imagem_artigo')),
                ('autor', models.CharField(max_length=50)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artigos', to='categoria.Categoria')),
            ],
        ),
    ]
