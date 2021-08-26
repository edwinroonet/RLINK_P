# Generated by Django 3.1.1 on 2021-08-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sg_user',
            fields=[
                ('u_no', models.AutoField(primary_key=True, serialize=False, verbose_name=10)),
                ('u_name', models.CharField(max_length=50, null=True)),
                ('u_email', models.CharField(max_length=100, null=True)),
                ('u_id', models.CharField(max_length=100, null=True)),
                ('u_passwd', models.CharField(max_length=255, null=True)),
                ('u_tel', models.CharField(max_length=50, null=True)),
                ('u_addr1', models.CharField(max_length=255, null=True)),
                ('u_addr2', models.CharField(max_length=255, null=True)),
                ('u_addr3', models.CharField(max_length=255, null=True)),
                ('u_agree', models.IntegerField(null=True)),
                ('u_auth', models.CharField(max_length=100, null=True)),
                ('u_kind', models.CharField(max_length=20, null=True)),
                ('u_type', models.CharField(max_length=10, null=True)),
                ('u_manager', models.CharField(max_length=20, null=True)),
                ('u_access', models.IntegerField(null=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=1)),
                ('is_authenticated', models.BooleanField(default=1)),
                ('chatid', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'sg_user',
            },
        ),
    ]