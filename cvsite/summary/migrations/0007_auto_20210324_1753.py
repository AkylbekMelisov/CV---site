# Generated by Django 3.1.7 on 2021-03-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0006_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('C1', 'C1'), ('C2', 'C2')], default='A1', max_length=50),
        ),
    ]
