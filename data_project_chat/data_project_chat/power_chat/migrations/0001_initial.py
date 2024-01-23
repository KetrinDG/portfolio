# Generated by Django 4.2.1 on 2023-11-19 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("chats", "0003_request_chat"),
    ]

    operations = [
        migrations.CreateModel(
            name="PowerChat",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=512)),
                ("answer", models.CharField(max_length=512, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="power_chat",
                        to="chats.userprofile",
                    ),
                ),
            ],
        ),
    ]
