from django.shortcuts import render
from .models import contents
# Create your views here.


def tables(request):
    row1 = contents()
    row1.number = 1
    row1.name1 = 'sreerag'
    row1.name2 = 'shahid'
    row1.name3 = 'niyas'

    row2 = contents()
    row2.number = 2
    row2.name1 = 'badusha'
    row2.name2 = 'jaliba'
    row2.name3 = 'ameen'

    row3 = contents()
    row3.number = 3
    row3.name1 = 'sudev'
    row3.name2 = 'arjun'
    row3.name3 = 'hashik'


    contentst =[row1, row2, row3] 


    return render(request, 'tables.html', {'contentst' : contentst })

