from django.shortcuts import render,redirect,HttpResponse
from allauth.socialaccount.models import SocialAccount
from .models import UserInfo
import json
# Create your views here.


def myprofile(request):
    contest_registered = []
    user = SocialAccount.objects.get(user_id=request.user.id)

    if request.method == "POST":
        user_info = UserInfo.objects.get(user = user)
        user_info.branch = request.POST['branch']
        user_info.college = request.POST['college']
        user_info.about = request.POST['about']
        user_info.save()
        return HttpResponse(
            json.dumps(True),
            content_type="application/json"
        )

    if request.user.is_authenticated():
        user_info,created = UserInfo.objects.get_or_create(user = user)
        if created:
            username = user.extra_data['email']
            user_info.email = username
            username = username[:username.index('@')]
            user_info.username = username
            user_info.save()
        contest_registered = user_info.contest_registered.all()

        u = SocialAccount.objects.all();
        for i in u:
            ui = UserInfo.objects.get(user = i)
            ui.email = i.extra_data['email']
            ui.save()
        return render(request,'scs_user/user_profile.html',{
            'contest_registered':contest_registered,
            'user_info':user_info
        })


    else:
        return redirect('/home/')



def visituser(request,user):
    if request.user.is_authenticated():
        ruser = SocialAccount.objects.get(user_id=request.user.id)
        ruser_info = UserInfo.objects.get(user = ruser)
        contests = []
        if user == ruser_info.username:
            return redirect('/user/profile')
        else:
            try:
                user_info = UserInfo.objects.get(username = user)
                contest_registered = user_info.contest_registered.all()

                for c in contest_registered:
                    if c.userinfo_set.filter(user=ruser).exists():
                        contests.append((c,True))
                    else:
                        contests.append((c,False))
            except Exception as e:
                print e

                return redirect('/home/')
        print contests
        return render(request,'scs_user/visit_user.html',{
            'contests':contests,
            'user_info':user_info,
            'social':user_info.user
        })


    else:
        return redirect('/home/')