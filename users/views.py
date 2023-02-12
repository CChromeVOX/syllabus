from django.shortcuts import render
from .models import *
from .forms import SyllabusForm
from django.http import HttpResponseRedirect


def add_page(request):
    submitted = False
    if request.method == 'POST':
        form = SyllabusForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.instructor = request.user
            f.status = Status.objects.get(type="Отправлено")
            f.save()
            return HttpResponseRedirect('/users/add_page/')

    else:
        form = SyllabusForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_page.html', {'form': form, 'submitted': submitted, 'user': request.user})
