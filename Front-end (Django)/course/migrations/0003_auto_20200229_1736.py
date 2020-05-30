# Generated by Django 3.0.1 on 2020-02-29 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200211_1915'),
        ('course', '0002_subject_number_of_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marks',
            name='Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.StudentInfo'),
        ),
    ]
