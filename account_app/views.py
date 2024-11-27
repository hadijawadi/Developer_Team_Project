from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate



def register_user(request):
    if request.method == 'POST':
         form = UserCreationForm(data= request.POST)
         if form.is_valid():
             new_user = form.save()
             login(request,new_user)
             return redirect('/')
    form = UserCreationForm()
    context= {
        'form':form
    }
    return render(request,'account_app/pages/register.htm',context)

# for loging out the user 

def logout_user(request):
    # user_log = request.user
    logout(request)
    return redirect('home')
    

def login_user(request):
    if request.method == 'POST':
        username  = request.POST['username']
        print(username)
        password  = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'account_app/pages/login.html',{'error':'Invalid username or password'})
    return render(request,'account_app/pages/login.html')


# from .forms import EditProfileForm
from django.http import HttpResponse

# # def edit_user_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, request.FILES, instance= request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('profile chanages updated')
#     form = EditProfileForm(instance=request.user)
#     print(request.user.username)
# # here in the instance we may have   request.user.profile alos in the above hadi ajvadi 
#     return render(request,'account_app/pages/edit_profile.html',{'form':form})