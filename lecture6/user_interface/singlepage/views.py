from django.http import Http404, HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'singlepage/index.html')

def singlepage2(request):
    return render(request, 'singlepage2/index.html')

def section(request,num):
    texts = ["Text1", "Text2", "Text3", "Text4"]
    
    if (1 <= num <= 4):
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("Not found")
