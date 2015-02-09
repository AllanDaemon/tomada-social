from django.shortcuts import render, render_to_response
from mongoengine.django.shortcuts import get_document_or_404

from django.template import RequestContext
from models import Account
from django.http import HttpResponseRedirect


def myuser_login_required(f):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
                if 'userid' not in request.session.keys():
                        return HttpResponseRedirect("/account/login")
                return f(request, *args, **kwargs)
        wrap.__doc__=f.__doc__
        wrap.__name__=f.__name__
        return wrap

@myuser_login_required
def create(request):
    if request.method == 'POST':
        # save new account
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        account = Account()
        account.name = name
        account.username = username
        account.password = password
        account.email = email
        account.save()
      
    return render_to_response('account/account_create.html',
                              context_instance=RequestContext(request))

def list(request):
    # Get all accounts from DB
    accounts = Account.objects
    return render_to_response('account/account_list.html', {'account_list': accounts},
                              context_instance=RequestContext(request))

def edit(request, account_id):
    account = get_document_or_404(Account, pk=account_id)
    if request.method == 'POST':
        # update field values and save to mongo
        account.name = request.POST['name']
        account.username = request.POST['username']
        account.password = request.POST['password']
        account.email = request.POST['email']
        account.save()
        template = 'account/account_list.html'
        params = {'account_list': Account.objects} 

    elif request.method == 'GET':
        template = 'account/account_edit.html'
        params = {'account':account}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request, account_id):
    account = get_document_or_404(Account, id=account_id)

    account.delete() 
    template = 'account/account_list.html'
    params = {'account_list': Account.objects} 

    return render_to_response(template, params, context_instance=RequestContext(request))


def login(request):
    request.session['userid'] = 'teste'
    if request.session.get('login'):
        return HttpResponseRedirect('/')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        usuario = Account.objects.filter(username=username, password=password)
        if len(usuario)>0:
            request.session['userid'] = str(usuario.objects.username)
            return HttpResponseRedirect('/')
        

    request.session['userid'] = False    
    return HttpResponseRedirect('/conta/login/')