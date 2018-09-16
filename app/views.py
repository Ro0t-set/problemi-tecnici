# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Aula,Problema
from .forms import PubbicaProblema, NoteProblema

from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
import datetime
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.template.loader import render_to_string
from django.http import Http404
from django.contrib import messages

@login_required(login_url='/login/')
def home(request):
    successtext = ''
    if request.method == "POST":
        form = PubbicaProblema(request.POST)
        if form.is_valid():

            problema = form.save(commit=False)
            problema.autore = request.user
            problema.published_date = timezone.now()
            problema.save()
            successtext = '<div class="alert alert-success"><strong>Operazione completata con successo!</strong> La sua richiesta è stata accettata</div>'

            #invio della mail (solo di prova per evitare errori in eventuale connessione ad internet assente)
            try:
                subject, from_email, to = 'Problema Tecnico', 'problemitecnicigalilei@gmail.com', 'problemitecnicigalilei@gmail.com'
                text_content = '456'
                html_content =  ( str(form) )
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except:
                pass

    else:
        form = PubbicaProblema()
    return render(request, 'home.html', {'form' : form, 'success': successtext})

@login_required(login_url='/login/')
def problemi(request):
    problemi = Problema.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'problemi.html', {'problemi' : problemi })


@login_required(login_url='/login/')
def problema_edit(request, problema_id):
    problema = get_object_or_404(Problema, id=problema_id)

    notesuccesstext = ''

    if  'NoteProblema' in request.POST:
        form = NoteProblema(request.POST, instance=problema)
        if form.is_valid():
            problema.save()
            print("ma che cazz")
            notesuccesstext = '<div class="alert alert-success"><strong>Operazione completata con successo!</strong> La tua nota è stata salvata</div>'
        else:
            notesuccesstext = '<div class="alert alert-warning"><strong>Operazione non completata!</strong> La tua nota non è stata salvata</div>'
    else:
        form = NoteProblema(instance=problema)

    if  'In Attesa' in request.POST:
        problema.risoluzione= 1
        problema.save()
        return redirect('problemi')
    elif  'Riparato!' in request.POST:
        problema.risoluzione= 2
        problema.save()
        return redirect('problemi')
    elif  'Rimandato' in request.POST:
        problema.risoluzione= 3
        problema.save()
        return redirect('problemi')




    return render(request, 'problema_edit.html', {'problema':problema, 'form':form, 'notesuccess': notesuccesstext})

def info(request):
    return render(request, 'info.html', {})
