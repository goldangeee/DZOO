from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
# def index(request):
#     _context = {'check':False}
#     if request.session.get('access_token'):
#         _context['check'] = True
#     return render(request,'login/index.html',_context)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            print("인증성공")
            login(request,user)
        else:
            print("인증실패")
    return render(request,"login/login.html")


# def kakaoLoginLogic(request):
#     _restApiKey = '' # 입력필요