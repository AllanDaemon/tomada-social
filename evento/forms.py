from bson import ObjectId
from django import forms
from models import *
from leaflet.forms import widgets

# class PostForm(forms.ModelForm):
# 	title = forms.CharField(max_length=255)
# 	text = forms.CharField(widget=forms.widgets.Textarea())
# 	is_published = forms.BooleanField(required=False)
# 	tags = forms.MultipleChoiceField(
# 		widget=forms.widgets.CheckboxSelectMultiple(), 
# 		required=False)

# 	def __init__(self, *args, **kwargs):
# 		self.instance = kwargs.pop('instance', None)
# 		super(PostForm, self).__init__(*args, **kwargs)
# 		self.fields['tags'].choices = [(tag.id, tag.title) for tag in Tag.objects]
# 		if self.instance:
# 			self.fields['title'].initial = self.instance.title
# 			self.fields['text'].initial = self.instance.text
# 			self.fields['is_published'].initial = self.instance.is_published		
# 			self.fields['tags'].initial = [tag.id for tag in self.instance.tags]


# 	def save(self, commit=True):
# 		post = self.instance if self.instance else Post()
# 		post.title = self.cleaned_data['title']
# 		post.text = self.cleaned_data['text']
# 		post.is_published = self.cleaned_data['is_published']
# 		post.tags = Tag.objects(id__in=self.cleaned_data['tags'])
# 		if commit:
# 			post.save()

# 		return post

class EventoForm(forms.Form):
	titulo = forms.CharField(max_length=255)
	descricao = forms.CharField(widget=forms.widgets.Textarea())
	publicado = forms.BooleanField(required=False)
	local = widgets.LeafletWidget()

	def __init__(self, *args, **kwargs):
		self.instance = kwargs.pop('instance', None)
		super(EventoForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['titulo'].initial = self.instance.titulo
			self.fields['descricao'].initial = self.instance.descricao
			self.fields['publicado'].initial = self.instance.publicado
			#	self.fields['local'].initial = self.instance.local


	def save(self, commit=True):
		evento = self.instance if self.instance else Evento()
		evento.titulo = self.cleaned_data['titulo']
		evento.descricao = self.cleaned_data['descricao']
		evento.publicado = self.cleaned_data['publicado']
	#	evento.local = self.cleaned_data['local']
		if commit:
			evento.save()

		return evento

