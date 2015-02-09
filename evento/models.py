from datetime import datetime
from mongoengine import *
from mongoengine.django.auth import User
from django.core.urlresolvers import reverse
import mongoengine.fields

# Create your models here.

class Evento(Document):
	titulo = StringField(max_length=200, required=True)
	descricao = StringField(required=True)
	data_modificacao = DateTimeField(default=datetime.now)
	publicado = BooleanField()
	local = PointField(auto_index=False)

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		return super(Evento, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('evento-detail', args=[self.id])

	def get_edit_url(self):
		return reverse('evento-update', args=[self.id])

	def get_delete_url(self):
		return reverse('evento-delete', args=[self.id])	
 	
 	# meta = {
  #       'indexes': [[("local", "2dsphere"), ("data_modificacao", 1)]]
  #   }
