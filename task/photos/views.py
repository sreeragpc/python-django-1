from django.shortcuts import render
from .models import pics
# Create your views here.


def photos(request):
    c1 = pics()
    c1.name = 'Iceland'
    c1.pic= 'a.jpg'

    c2 = pics()
    c2.name = 'Finland'
    c2.pic= 'b.jpg'

    c3 = pics()
    c3.name = 'Norway'
    c3.pic= 'c.jpg'



    picst =[c1, c2, c3] 
    print(c1.pic)
    

    return render(request, 'photos.html', {'picst' : picst })