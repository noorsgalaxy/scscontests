from django.shortcuts import render,redirect

# Create your views here.
from .models import Contests
from ..scs_user.models import UserInfo
from allauth.socialaccount.models import SocialAccount


def contests_list(request):
    objects = Contests.objects.all()
    contests_items = []
    for c in objects:
        if request.user.is_authenticated():
            if c.userinfo_set.filter(user=SocialAccount.objects.get(user_id=request.user.id)).exists():
                contests_items.append((c,True))
            else:
                contests_items.append((c,False))
        else:
            contests_items.append((c,False))
    context = {
        'contests_list':contests_items,
    }
    return render(request,'contests/contests_list.html',context)


def register(request,cid):
    id = int(request.GET.get('cid'))
    user = SocialAccount.objects.get(user_id=request.user.id)
    user_info = UserInfo.objects.get_or_create(user=user)[0]
    contest = Contests.objects.get(id=id)
    user_info.save()
    user_info.contest_registered.add(contest)
    return redirect('/contests/v/?cid='+ str(id))


def contests_view(request,cid):
    id = int(request.GET.get('cid'))
    contest = Contests.objects.get(id=id)
    participants = contest.userinfo_set.all()
    if request.user.is_authenticated():
        is_registered = contest.userinfo_set.filter(user=SocialAccount.objects.get(user_id=request.user.id)).exists()
    else:
        is_registered = False
    return render(request,'contests/contests_view.html',{
        'participants':participants,
        'contest':contest,
        'is_registered':is_registered
    })