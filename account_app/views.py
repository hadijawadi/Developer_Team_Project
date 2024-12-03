from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from.forms import UserProfileForm
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from django.http import HttpResponse


#for sending email to user when user is registering 
def test_email(request):
    subject = 'Test Email from Django'
    message = 'This is a test email to confirm your email setup in Django.'
    from_email = 'Hadijawadi1385@gmail.com'  # Replace with your email address
    recipient_list = ['1978javadi@gmail.com']  # Replace with the recipient's email address

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Failed to send email: {e}')


# for comopleting user data 
@login_required(login_url='account_app:register_user')
def create_profile(request):
    form = UserProfileForm()   
    if request.method == 'POST':
        user_profile= UserProfileForm(request.POST, request.FILES)
        if user_profile.is_valid():
            if user_profile is not None:
                user_profile = form.save(commit=False)  # Don't save to the database yet
                user_profile.user = request.user # Set the user to the current logged-in user
                
                user_profile.save()
               
                return HttpResponse('Your Profile completed')
    
    return render(request,'account_app/pages/profile.htm',context= {"form":form})



# for registering user username and password 
def register_user(request):
    if request.method == 'POST':
         form = CustomUserCreationForm(data= request.POST)
         if form.is_valid():
             new_user = form.save()
             user_email = form.cleaned_data['email']  # Access the email from cleaned_data

              # Send the welcome email
             send_mail(
                'Thank You for Registering ',
                'Welcome! Thank you for registering on our platform. We are excited to have you. developerTeam ',
                'hadijawadi1385@gmail.com',
                [user_email],
                fail_silently=False,
              )
             login(request,new_user)
             return redirect('/')
    form =CustomUserCreationForm()
    context= {
        'form':form
    }
    return render(request,'account_app/pages/register.htm',context)



# for loging out the user 
@login_required(login_url='account_app:register_user')
def logout_user(request):
    user_log = request.user
    print(user_log)
    logout(request)
    return redirect('home_view')
    
# write code for logining user 

def login_user(request):
    if request.method == 'POST':
        username  = request.POST['username']
        print(username)
        password  = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('home_view')
        else:
            return render(request,'account_app/pages/login.htm',{'error':'Invalid username or password'})
    return render(request,'account_app/pages/login.htm')

#  fogetting user password

def forget_password(request):
    pass