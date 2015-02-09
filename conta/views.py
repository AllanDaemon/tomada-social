# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import *
from forms import *
from django.http import HttpResponseRedirect

class ContaCreateView(CreateView):
    model = Conta
    form_class = ContaForm

    def get_template_names(self):
        return ["conta/conta_create.html"]

    def get_success_url(self):
        return reverse('evento-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.user = self.request.user
        messages.success(self.request, "Usuario criado.")
        return super(ContaCreateView, self).form_valid(form)    

class ContaListView(ListView):
    model = Conta
    context_object_name = "conta_list"

    def get_template_names(self):
        return ["conta/conta_list.html"]

    def get_queryset(self):
        contas = Conta.objects

        # if 'all_eventos' not in self.request.GET:
        #     eventos = eventos.filter(publico=True)
        return contas

class ContaDetailView(DetailView):
    model = Conta
    context_object_name = "conta"

    def get_template_names(self):
        return ["conta/conta_detail.html"]

    def get_object(self):
        return Conta.objects(id=self.kwargs['pk'])[0]

class ContaUpdateView(UpdateView):
    model = Conta
    form_class = ContaForm
    context_object_name = "conta"

    def get_template_names(self):
        return ["conta/conta_update.html"]

    def get_success_url(self):
        return reverse('conta-list')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Conta atualizado.")
        return super(ContaUpdateView, self).form_valid(form)

    def get_object(self):
        return Conta.objects(id=self.kwargs['pk'])[0]

class ContaDeleteView(DeleteView):
    model = Conta

    def get_success_url(self):
        return reverse('conta-list')

    def get(self, *args, **kwargs):
        """ Skip confirmation page """
        return self.delete(self.request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, "Conta removido.")
        return redirect(self.get_success_url())        

    def get_object(self):
        return Conta.objects(id=self.kwargs['pk'])[0]

class ContaLoginView(FormView):
    model = Conta
    form_class = LoginForm

    def get_template_names(self):
        return ["conta/conta_login.html"]

    def form_valid(self, form):
        if self.request.session.get('login', False):
            print 'logado'

        usuario = form.cleaned_data['usuario']
        senha = form.cleaned_data['senha']
        usuario = Conta.objects.filter(usuario=usuario, senha=senha)
        if len(usuario)>0:
            self.request.session['login'] = True
            return HttpResponseRedirect('/')
        self.request.session['login'] = False
        return HttpResponseRedirect('/conta/login/')

    def get_success_url(self):
        return reverse('evento-list')
