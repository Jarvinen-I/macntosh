from django.shortcuts import render, redirect

from .forms import CustomerForm
from .models import Customer


def index(request):
    return render(request, 'web/index.html')


def contact_view(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('/contact/')

    return render(request, 'web/contact.html', {'form': form})
