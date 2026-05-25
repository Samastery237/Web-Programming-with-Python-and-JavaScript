from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label='Task', max_length=100)
    priority = forms.IntegerField(label='Priority', min_value=1, max_value=5, required=False)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] 
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data["task"]
            request.session["tasks"] += [new_task]
            return HttpResponseRedirect(reverse("tasks:index"))
    else:
        return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })

        
    return render(request, "tasks/add.html", {
        "form": form
    })