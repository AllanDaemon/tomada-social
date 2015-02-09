from django import forms
from models import *

class ContaForm(forms.Form):
	nome = forms.CharField(max_length=50)
	usuario = forms.CharField(max_length=30)
	senha = forms.CharField(max_length=30)	
	email = forms.CharField(max_length=30)

	def __init__(self, *args, **kwargs):
		self.instance = kwargs.pop('instance', None)
		super(ContaForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['nome'].initial = self.instance.nome
			self.fields['usuario'].initial = self.instance.usuario
			self.fields['senha'].initial = self.instance.senha
			self.fields['email'].initial = self.instance.email


	def save(self, commit=True):
		conta = self.instance if self.instance else Conta()
		conta.nome = self.cleaned_data['nome']
		conta.usuario = self.cleaned_data['usuario']
		conta.senha = self.cleaned_data['senha']
		conta.email = self.cleaned_data['email']
		if commit:
			conta.save()

		return conta

class LoginForm(forms.Form):
    
    usuario = forms.CharField(label=(u"Usuario ou email"))
    senha = forms.CharField(label=(u"Senha"), widget=forms.PasswordInput(render_value=False))
    	
    def __init__(self, *args, **kwargs):
		self.instance = kwargs.pop('instance', None)
		super(LoginForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['senha'].initial = self.instance.senha
			self.fields['usuario'].initial = self.instance.usuario

    def login(self, request):
    	usuario = Conta.objects.filter(usuario=username, senha=password)
    	print usuario
    	if len(usuario) > 0:
    		return True

    	return False