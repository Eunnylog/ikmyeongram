# Generated by Django 4.2 on 2023-04-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'my_comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=45, verbose_name='글제목')),
                ('post_content', models.TextField(verbose_name='글내용')),
                ('post_img', models.FileField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_id', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'my_posting',
            },
        ),
    ]
