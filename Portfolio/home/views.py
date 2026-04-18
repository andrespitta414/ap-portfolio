from django.shortcuts import render
from django.http import JsonResponse
from templates import *
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # TODO: send email
        return JsonResponse({'status': 'received'})
    return render(request, 'contact.html')