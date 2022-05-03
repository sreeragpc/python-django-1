from django.shortcuts import render
from .models import cards
# Create your views here.


def dummy(request):
    test1 = cards()

    test1.name = 'Elephant'
    test1.para = 'Elephants are the largest existing land animals. Three living species are currently recognised: the African bush elephant, the African forest elephant, and the Asian elephant. They are an informal grouping within the proboscidean family Elephantidae.'
    
    test2=cards()

    test2.name = 'Lion'
    test2.para = 'The lion is a large cat of the genus Panthera native to Africa and India. It has a muscular, deep-chested body, short, rounded head, round ears, and a hairy tuft at the end of its tail.adult male lions are larger than females and have a prominent mane'

    test3=cards()
    test3.name = 'Tiger'
    test3.para ='The tiger is the largest living cat species and a member of the genus Panthera. It is most recognisable for its dark vertical stripes on orange fur with a white underside. An apex predator, it primarily preys on ungulates such as deer and wild boar.'
    
    cardst =[test1, test2, test3] 


    return render(request, 'dummy.html', {'cardst' : cardst})

