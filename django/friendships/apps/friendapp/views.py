from django.shortcuts import render
from .models import Users, Friendships
# Create your views here.
def index(req):
    friendships = Users.objects.filter(usersfriend__friend__id=2)
    print friendships.query
    context = {'friendships':friendships}
    return render(req, "friendapp/index.html", context)