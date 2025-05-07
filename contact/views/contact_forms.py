from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from contact.forms import ContactForms
from django.core.exceptions import ValidationError
from django.urls import reverse
from contact.models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST': 
        form= ContactForms(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action':form_action,  
        }
        
        if form.is_valid():
            contact = form.save(commit=False)
            contact.proprietario = request.user
            contact.save()
            # return redirect('contact:update', Contact_id=contact.pk)
            return redirect('contact:update', contact_id=contact.pk)


        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForms(),
        'form_action':form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, proprietario= request.user)
    form_action = reverse('contact:update', kwargs={'contact_id': contact_id})
    # form_action = reverse('contact:update', args=(contact_id))


    if request.method == 'POST': 
        form= ContactForms(request.POST, request.FILES ,instance=contact)
        context = {
            'form': form,
            'form_action':form_action,  
        }
        
        if form.is_valid():
            contact = form.save()
            # return redirect('contact:update', Contact_id=contact.pk)
            return redirect('contact:update', contact_id=contact.pk)


        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForms(instance=contact),
        'form_action':form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, 
        pk=contact_id, 
        show=True,
        proprietario=request.user
        )
    
    confirmation = request.POST.get('confirmation','no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(request, 
                'contact/contact.html',
                {'contact':contact, 
                 'confirmation':confirmation
                }
            )