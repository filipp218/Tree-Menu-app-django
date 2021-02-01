Tree menu

Приложение, которое реализовывает древовидное меню с помощью templatetag

Шаги, чтобы воспользоваться:
1. Добавьте приложение "yum" в settings.py в INSTALLED_APPS 
2. Загрузите в шаблон templatetag — {% load main_menu %}
3. Передайте в функцию название меню и request.path Пример: — {% draw_menu "NameMenu" request.path %}
