# Generated by Django 4.2.5 on 2023-09-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_projects"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projects",
            options={"verbose_name": "项目表", "verbose_name_plural": "项目表"},
        ),
        migrations.AlterField(
            model_name="projects",
            name="id",
            field=models.AutoField(
                help_text="id主键描述",
                primary_key=True,
                serialize=False,
                verbose_name="id主键",
            ),
        ),
    ]
