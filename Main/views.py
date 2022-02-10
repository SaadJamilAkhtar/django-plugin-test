from django.shortcuts import render


def index(request):
    if request.POST:
        print(request.POST.get("plugin"))
    return render(request, 'index.html')
