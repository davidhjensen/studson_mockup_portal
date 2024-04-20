# views.py
from django.shortcuts import render, redirect
from .forms import MockupForm
from .models import Mockup

def create_mockup(request):
    if request.method == 'POST':
        form = MockupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('generate_pdf')
    else:
        form = MockupForm()
    return render(request, 'create_mockup.html', {'form': form})
