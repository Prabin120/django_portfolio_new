from django.shortcuts import render
from .models import Feedback

def index(request):
    import django
    print(django.__path__)
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Feedback.objects.create(name = name, email = email, message = message)
    return render(request,"index.html")