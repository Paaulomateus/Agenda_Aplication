from django.shortcuts import render
from contact.forms import RegisterForms
from django.contrib import messages


def register(request):
    form = RegisterForms()

    messages.info(request, '')

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            form.save()
            
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
