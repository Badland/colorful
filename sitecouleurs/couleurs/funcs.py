from .models import Color
from operator import itemgetter
from collections import OrderedDict
import random


def get_pieges(color,colorlist,rangechoix,nbchoix) :
    dicdistances={}
    for i in colorlist:
        dicdistances[i.id]=(i.r-color.r)**2+(i.g-color.g)**2+(i.b-color.b)**2
    sorteddicdistances=OrderedDict( sorted(dicdistances.items(), key=itemgetter(1),))
    possibilitepieges=list(sorteddicdistances)[1:rangechoix]
    possibilitepiegescouleurs=[]
    for i in possibilitepieges:
        color=Color.objects.get(pk=i)
        possibilitepiegescouleurs.append(color)
    pieges=random.sample(possibilitepiegescouleurs,nbchoix)
    return(pieges)











