# Generated by Django 4.2.7 on 2023-12-16 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_remove_thefriends_lise_thefriends_is_online_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament_8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semifinal1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semifinal1', to='users.user')),
                ('semifinal2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semifinal2', to='users.user')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user11', to='users.user')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user22', to='users.user')),
                ('user3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user33', to='users.user')),
                ('user4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user44', to='users.user')),
                ('user5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user55', to='users.user')),
                ('user6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user66', to='users.user')),
                ('user7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user77', to='users.user')),
                ('user8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user88', to='users.user')),
                ('winner1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner11', to='users.user')),
                ('winner2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner22', to='users.user')),
                ('winner3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner33', to='users.user')),
                ('winner4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner44', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament_4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='users.user')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='users.user')),
                ('user3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user3', to='users.user')),
                ('user4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user4', to='users.user')),
                ('winner1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner1', to='users.user')),
                ('winner2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner2', to='users.user')),
            ],
        ),
    ]