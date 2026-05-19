from django.shortcuts import render, get_object_or_404
from .models import Interpret


def home(request):

    interpreti = Interpret.objects.all()

    return render(request, 'home.html', {
        'interpreti': interpreti
    })

def detail_interpreta(request, id):

    interpret = get_object_or_404(
        Interpret,
        pk=id
    )

    alba = interpret.diskografie.all()

    turne = interpret.vystoupeni.all()

    return render(request, 'detail.html', {
        'interpret': interpret,
        'alba': alba,
        'turne': turne
    })