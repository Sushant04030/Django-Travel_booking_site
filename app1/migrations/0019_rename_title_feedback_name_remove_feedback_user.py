# Generated by Django 4.1.4 on 2023-07-02 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_alter_feedback_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]