# Generated by Django 4.2.5 on 2023-09-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="项目描述", max_length=20, verbose_name="项目名称"
                    ),
                ),
                (
                    "leader",
                    models.CharField(
                        help_text="项目负责人描述", max_length=10, verbose_name="项目负责人"
                    ),
                ),
                (
                    "is_execute",
                    models.BooleanField(
                        default=True, help_text="项项目启动描述", verbose_name="是否启动项目"
                    ),
                ),
                (
                    "desc",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="项项目启动描述",
                        null=True,
                        verbose_name="是否启动项目",
                    ),
                ),
                (
                    "creat_time",
                    models.DateTimeField(
                        auto_now_add=True, help_text="创建时间描述", verbose_name="创建时间"
                    ),
                ),
                (
                    "update_time",
                    models.DateTimeField(
                        auto_now=True, help_text="更新时间描述", verbose_name="更新时间"
                    ),
                ),
            ],
            options={
                "db_table": "tb_projects",
            },
        ),
    ]
