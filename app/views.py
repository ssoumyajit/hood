from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("I code, because I am afraid someday i get sick or loose my leg and I cannot dance. Then I really, \
    would need a way out and I know I won't find any coz dance is all I know and love... The love is beyond and the fear, \
     is real, that is why I am preparing myself,with another skill so that I can find a way to express my mind and don't loose.")

