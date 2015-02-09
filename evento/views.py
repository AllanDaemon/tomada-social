# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import *
from forms import *

class EventoHomeView(TemplateView):
	template_name = "evento/evento_home.html"


class EventoListView(ListView):
    model = Evento
    context_object_name = "evento_list"

    def get_template_names(self):
        return ["evento/evento_list.html"]

    def get_queryset(self):
        eventos = Evento.objects

        # if 'all_eventos' not in self.request.GET:
        #     eventos = eventos.filter(publico=True)
        return eventos

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm

    def get_template_names(self):
        return ["evento/evento_create.html"]

    def get_success_url(self):
        return reverse('evento-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.user = self.request.user
        messages.success(self.request, "Evento criado.")
        return super(EventoCreateView, self).form_valid(form)	

class EventoDetailView(DetailView):
    model = Evento
    context_object_name = "evento"

    def get_template_names(self):
        return ["evento/evento_detail.html"]

    def get_object(self):
        return Evento.objects(id=self.kwargs['pk'])[0]    

class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    context_object_name = "evento"

    def get_template_names(self):
        return ["evento/evento_update.html"]

    def get_success_url(self):
        return reverse('evento-list')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Evento atualizado.")
        return super(EventoUpdateView, self).form_valid(form)

    def get_object(self):
        return Evento.objects(id=self.kwargs['pk'])[0]

class EventoDeleteView(DeleteView):
    model = Evento

    def get_success_url(self):
        return reverse('evento-list')

    def get(self, *args, **kwargs):
        """ Skip confirmation page """
        return self.delete(self.request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, "Evento removido.")
        return redirect(self.get_success_url())        

    def get_object(self):
        return Evento.objects(id=self.kwargs['pk'])[0]

# class PostDeleteView(DeleteView):
#     model = Post

#     def get_success_url(self):
#         return reverse('post-list')

#     def get(self, *args, **kwargs):
#         """ Skip confirmation page """
#         return self.delete(self.request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.delete()
#         messages.success(self.request, "Post removed.")
#         return redirect(self.get_success_url())        

#     def get_object(self):
#         return Post.objects(id=self.kwargs['pk'])[0]

# class PostUpdateView(UpdateView):
#     model = Post
#     form_class = PostForm
#     context_object_name = "post"

#     def get_template_names(self):
#         return ["evento/post_update.html"]

#     def get_success_url(self):
#         return reverse('post-list')

#     def form_valid(self, form):
#         self.object = form.save()
#         messages.success(self.request, "Post updated.")
#         return super(PostUpdateView, self).form_valid(form)

# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm

#     def get_template_names(self):
#         return ["evento/post_create.html"]

#     def get_success_url(self):
#         return reverse('post-list')

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         messages.success(self.request, "Post created.")
#         return super(PostCreateView, self).form_valid(form)	

# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = "post"

#     def get_template_names(self):
#         return ["evento/post_detail.html"]

#     def get_object(self):
#         return Post.objects(id=self.kwargs['pk'])[0]

# class TagListView(ListView):
#     model = Tag
#     context_object_name = "tag_list"

#     def get_template_names(self):
#         return ["evento/tag_list.html"]

#     def get_queryset(self):
#         return Tag.objects

# class PostListView(ListView):
#     model = Post
#     context_object_name = "post_list"

#     def get_template_names(self):
#         return ["evento/post_list.html"]

#     def get_queryset(self):
#         posts = Post.objects
#         if 'all_posts' not in self.request.GET:
#             posts = posts.filter(is_published=True)
#         tag = self.request.GET.get('tag', None)        
#         if tag:
#             posts = posts.filter(tags=tag)
#         return posts