from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .models import Color,Round
import random
from django.db.models import Sum,Avg

from .funcs import get_pieges
from django.contrib.auth import authenticate, login, models,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated:



        if request.method == "POST":
            listchoice=[]


            choice=request.POST
            dictround={'totalroundscore':0}
            counter=0
            for k,v in choice.items():
                if k.isnumeric():
                    dictround['ans%i'%counter]=k
                    anscolor=Color.objects.get(id=k)
                    choicecolor=Color.objects.get(id=v)
                    dictround['choice%i'%counter]=v
                    dictround['score%i'%counter]=1-((anscolor.r-choicecolor.r)**2+(anscolor.g-choicecolor.g)**2+(anscolor.b-choicecolor.b)**2)/1000
                    dictround['totalroundscore']+=dictround['score%i'%counter]
                    counter += 1

            r=Round(date=timezone.now(),ans1=dictround['ans0'],ans2=dictround['ans1'],ans3=dictround['ans2'],choice1=dictround['choice0'],choice2=dictround['choice1'],choice3=dictround['choice2'],score=dictround['totalroundscore'],user_id=request.user.id)
            r.save()

            # context for display
            template = loader.get_template( 'sitecouleurs/answers.html' )
            listavailable=[Color.objects.get(id=dictround['ans0']),Color.objects.get(id=dictround['ans1']),Color.objects.get(id=dictround['ans2'])]
            user_answers= [Color.objects.get(id=dictround['choice0']),Color.objects.get(id=dictround['choice1']),Color.objects.get(id=dictround['choice2'])]
            zipped=zip(listavailable,user_answers)
            totalscore=Round.objects.filter(user_id=request.user.id).aggregate(Sum('score'))["score__sum"]
            average=Round.objects.filter(user_id=request.user.id).aggregate(Avg('score'))["score__avg"]

            context = {
                'zipped': zipped,
                "roundscore":dictround['totalroundscore'],
                'totalscore': totalscore,
                "average":average

            }
            return HttpResponse( template.render( context, request ) )



        colorlist=Color.objects.order_by('id')
        randomcolor=colorlist[random.randint(1,len(colorlist))]
        truecolor=randomcolor.name
        pieges=get_pieges(randomcolor,colorlist,12,2)
        listavailable=[randomcolor]
        for i in pieges:
            listavailable.append(i)
        # random.shuffle(listavailable)
        shuffled=listavailable[:]
        random.shuffle(shuffled)
        template=loader.get_template('sitecouleurs/index.html')

        context = {
            'randomcolor':randomcolor,
            'truecolor': truecolor,
            'listavailable':listavailable,
            'shuffled': shuffled,
        }
        return HttpResponse(template.render(context,request))
    else :
        return HttpResponseRedirect( '/couleurs/login/' )






def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        u = User.objects.create_user( username, email, password, first_name=fname, last_name=lname )
        u.save()

        return HttpResponse(
            "Registration complete! Please head over to the <a href='/login/'>login page</a> to start using your website." )

    return render( request, "sitecouleurs/register.html", {} )


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password )
        if user is not None:
            if user.is_authenticated:
                login( request, user )
                return HttpResponseRedirect( '/couleurs/' )
            else:
                return HttpResponse( "This user is not active. Please contact support@company.com" )
        else:
            return HttpResponseRedirect( '/couleurs/login/' )
    return render( request, "sitecouleurs/login.html", {} )


def Logout(request):
    logout( request )
    return HttpResponseRedirect( '/couleurs/login/' )



def userpage(request,user_id):
    return HttpResponse("C'est l'utilistateur %s"%user_id)

def welcome(request,user_id):
    response='Bienvenue %s'
    return HttpResponse(response %user_id)

def begin (request, user_id):
    return HttpResponse("Début du jeu pour l'utilisateur %s" %user_id)
