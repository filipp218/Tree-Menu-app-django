from django.db import models
from django.contrib.auth.models import User



class MenuItem(models.Model):
    title = models.CharField("Название" , max_length = 150, blank=False, help_text="Введите название элемента меню")
    url = models.SlugField(max_length=150, unique=True, help_text="Введите url для элемента меню")
    name_menu = models.CharField("Описание",  max_length = 150, blank=False, null=True,  help_text="Введите названия всего меню")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,  help_text="Выберете родителя меню, если это родитель, то оставьте поле пустым")


    def __str__(self):
        return self.title
