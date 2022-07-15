from django.shortcuts import render
from twitter.models import Twitter


def pagina_inicial(request):
    tweets = Twitter.objects.all()
    context = {'tweets' : tweets}
    return render(request, "twitter/pagina_inicial.html", context)