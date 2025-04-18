# Generated by Django 5.2 on 2025-04-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhatApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment_tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('acbs', models.PositiveBigIntegerField()),
                ('mio', models.PositiveBigIntegerField()),
                ('ssi', models.PositiveBigIntegerField(blank=True)),
                ('dragon', models.PositiveBigIntegerField()),
                ('cash', models.PositiveBigIntegerField()),
                ('total_investment', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Invesments',
            new_name='Investments',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='cash',
            field=models.PositiveBigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='credit',
            field=models.PositiveBigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='description',
            field=models.TextField(blank=True, verbose_name=255),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='digital',
            field=models.PositiveBigIntegerField(blank=True),
        ),
    ]
