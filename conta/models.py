from datetime import datetime
from mongoengine import *
from mongoengine.django.auth import User
from django.core.urlresolvers import reverse
import mongoengine.fields

# Create your models here.

class Conta(Document):
    nome = StringField(max_length=50)
    usuario = StringField(max_length=30)
    senha = StringField(max_length=30)
    email = EmailField(max_length=30)
    UUID = UUIDField()

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        return super(Conta, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('conta-detail', args=[self.id])

    def get_edit_url(self):
        return reverse('conta-update', args=[self.id])

    def get_delete_url(self):
        return reverse('conta-delete', args=[self.id])  