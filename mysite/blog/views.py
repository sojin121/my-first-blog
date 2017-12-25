from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>hello world!!</h1>')
    #return render(request, 'blog/default.html', {})