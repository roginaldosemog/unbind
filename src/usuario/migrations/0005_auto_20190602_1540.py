# Generated by Django 2.0.7 on 2019-06-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20190602_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto_usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='scoreTotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
