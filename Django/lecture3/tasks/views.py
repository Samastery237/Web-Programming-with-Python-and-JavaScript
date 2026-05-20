from django.shortcuts import render

task = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "task": task
    })


def add(request):
    if request.method == "POST":
        task.append(request.POST["task"])
        return render(request, "tasks/index.html", {
            "tasks": task
        })
    return render(request, "tasks/add.html")