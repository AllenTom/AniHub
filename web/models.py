from django.db import models

# Create your models here.
from mongoengine import Document, StringField


class Animate(Document):
    bangumi_id = StringField(max_length=100)
    name = StringField(max_length=100)
