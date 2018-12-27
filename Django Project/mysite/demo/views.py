from django.shortcuts import render
from demo.models import LoginUser
from random import randint

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get('https://api.github.com/users?since=0')
    api = json.loads(api_request.content.decode('utf-8'))
    if not 'userName' in request.session:
        return render(request, 'home.html', {'api': api, 'check': '123'})
    else:
        info = LoginUser.objects.get(account=request.session['account'])
        return render(request, 'home.html', {'api': api, 'info': info})

def user(request):
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get('https://api.github.com/users/'+user)
        username = json.loads(user_request.content.decode('utf-8'))
        if not 'userName' in request.session:
            return render(request, 'user.html', {'user': user, 'username': username, 'check': '123'})
        else:
            info = LoginUser.objects.get(account=request.session['account'])
            return render(request, 'user.html', {'user': user, 'username': username, 'info': info})
    else:
        notfound = '请在搜索框内输入想要搜索的人名...'
        if not 'userName' in request.session:
            return render(request, 'user.html', {'notfound': notfound, 'check': '123'})
        else:
            info = LoginUser.objects.get(account=request.session['account'])
            return render(request, 'user.html', {'notfound': notfound, 'info': info})

def logindo(request):
    login_account = request.POST['account']
    login_password = request.POST['password']
    try:
        v = LoginUser.objects.get(account=login_account)
        print(v.name, v.account, v.password)
        if login_account == v.account and login_password == v.password:
            request.session['userName'] = v.name
            request.session['account'] = v.account
            request.session['password'] = v.password
            request.FILES['img'] = v.img
            import requests
            import json
            api_request = requests.get('https://api.github.com/users?since=0')
            api = json.loads(api_request.content.decode('utf-8'))
            info = v
            return render(request, 'home.html', {'api': api, 'info': info})
        else:
            mes = '用户或密码错误!'
            return render(request, 'login.html', {'mes': mes, 'check':'123'}) 
    except:
        mes = '用户不存在!'
        return render(request, 'login.html', {'mes': mes, 'check':'123'})

def loginout(request):
    try:
        request.session.flush()
        return_info = '您已成功退出登陆...'
        return render(request, 'login.html', {'quit': return_info, 'check':'123'})
    except:
        return_info = '您还未登陆登陆...'
        return render(request, 'login.html', {'wrong': return_info, 'check':'123'})

def login(request):
    if not 'userName' in request.session:
        return render(request, 'login.html', {'check': '123'})
    else:
        info = LoginUser.objects.get(account=request.session['account'])
        return render(request, 'login.html', {'info': info})

def regiterdo(request):
    regiter_name = request.POST['userName']
    regiter_password = request.POST['password']
    while True:
        regiter_account = randint(10000, 100000)
        try:
            LoginUser.objects.get(account=regiter_account)
        except:
            break
    regiter_img = 'img/pnte.png'
    new = LoginUser(name=regiter_name, password=regiter_password, account=regiter_account, img=regiter_img)
    new.save()
    request.session['userName'] = regiter_name
    request.session['account'] = regiter_account
    request.session['password'] = regiter_password
    request.FILES['img'] = regiter_img
    import requests
    import json
    api_request = requests.get('https://api.github.com/users?since=0')
    api = json.loads(api_request.content.decode('utf-8'))
    info = LoginUser.objects.get(account=request.session['account'])
    return render(request, 'home.html', {'api': api, 'info': info})

def regiterout(request):
    try:
        regiter_name = request.session['userName']
        regiter_account = request.session['account']
        print(regiter_account)
        print(regiter_name)
        LoginUser.objects.filter(account=regiter_account).delete()
        request.session.flush()
        return render(request, 'regiter.html', {'delete': '', 'check':'123'})
    except:
        return_info = '您还未登陆...'
        return render(request, 'login.html', {'wrong': return_info, 'check':'123'})

def regiter(request):
    if not 'userName' in request.session:
        return render(request, 'regiter.html', {'check': '123'})
    else:
        info = LoginUser.objects.get(account=request.session['account'])
        return render(request, 'regiter.html', {'info': info})

def host(request):
    info = LoginUser.objects.get(account=request.session['account'])
    return render(request, 'host.html', {'info': info})

def change(request):
    info = LoginUser.objects.get(account=request.session['account'])
    return render(request, 'change.html', {'info': info})

def changedo(request):
    change_name = request.POST['userName']
    change_img = request.FILES['img']
    Account = request.session['account']
    new = LoginUser.objects.get(account=Account)
    if change_name == '' and change_img == '':
        info = LoginUser.objects.get(account=Account)
        return render(request, 'host.html', {'info': info})
    else:
        if change_img == '':
            new.name = change_name
            new.save()
            info = LoginUser.objects.get(account=Account)
            return render(request, 'host.html', {'info': info})
        elif change_name == '':
            new.img = change_img
            new.save()
            info = LoginUser.objects.get(account=Account)
            return render(request, 'host.html', {'info': info})
        else:
            new.name = change_name
            new.img = change_img
            new.save()
            info = LoginUser.objects.get(account=Account)
            return render(request, 'host.html', {'info': info})

def upload(request):
    info = LoginUser.objects.get(account=request.session['account'])
    return render(request, 'upload.html', {'info': info})

def uploaddo(request):
    obj = request.FILES.get('data')
    info = LoginUser.objects.get(account=request.session['account'])
    info.data = obj
    print(obj.name)
    info.save()
    return render(request, 'upload.html', {'info': info})