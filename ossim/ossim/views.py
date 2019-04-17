from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


def index(request):
    return render(request, 'ossim/index.html')

def wiki(request):
    return render(request, 'mat/wiki.html')

def pr(request):
    return render(request, 'mat/wikipagerep.html')

def ds(request):
    return render(request, 'mat/wikidisk.html')

def ba(request):
    return render(request, 'mat/wikiba.html')

def fa(request):
    return render(request, 'mat/wikifa.html')

def mvt(request):
    return render(request, 'mat/wikimvt.html')

def mft(request):
    return render(request, 'mat/wikimft.html')

def ps(request):
    return render(request, 'mat/wikiprocscd.html')

def soc(request):
    return render(request, 'mat/wikisoc.html')

def sync(request):
    return render(request, 'mat/wikisync.html')

def matindex(request):
    return render(request, 'mat/teamindex.html')


