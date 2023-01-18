from django.shortcuts import render

from django.shortcuts import render
from .models import Place, Team


def demo(request):
   obj=Place.objects.all()
   per=Team.objects.all()
   return render(request,"index.html",{'result':obj,'out':per})


