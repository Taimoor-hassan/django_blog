# Generated by Django 3.2.6 on 2021-08-31 10:17

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=100)),
                ('content', froala_editor.fields.FroalaField()),
                ('image', models.ImageField(upload_to='Category/')),
                ('url', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=100)),
                ('conten', froala_editor.fields.FroalaField()),
                ('image', models.ImageField(upload_to='Posts/')),
                ('url', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
