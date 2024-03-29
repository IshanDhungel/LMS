# Generated by Django 3.2.7 on 2024-01-26 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200412_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.studentextra'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='issuedbook',
            unique_together={('enrollment', 'isbn')},
        ),
    ]
