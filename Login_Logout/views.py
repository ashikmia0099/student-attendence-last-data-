from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import User, Sponsor, Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse

from django.conf import settings

User = get_user_model() 



# এখানে আমি একজন ইউজার রেজিস্টার করার জন্য ভিউস এর কোড করসি 


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import Sponsor, Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

User = get_user_model()



def Register(request):
    ref_code = request.GET.get('ref_code')
    form = RegisterForm(request.POST or None)
    recommended_by_profile = None  

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()

            if ref_code:
                try:
                    sponsor = Sponsor.objects.get(code=ref_code)
                    instance.sponsor.recommended_by = sponsor.user
                    
                    instance.sponsor.save()
                
                except Sponsor.DoesNotExist:
                    pass

            # Check if Sponsor already exists
          
            messages.success(request, 'Account registered successfully')
            return redirect('Registerpage')
        
        else:
            form.save()
            messages.error(request, 'Registration failed. Please correct the errors.')
    
    return render(request, 'register.html', {'form': form})




# এখানে আমি Refferal Code Generate  কোড করসি

def Refferal_code_generate(request, *args, **kwargs):
    
    code = str(kwargs.get('ref_code'))
    
    
    try:
        profile = Sponsor.objects.get(code = code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
        
    except:
        pass
    
    print(request.session.get_expiry_date())
    
    
   
        
    return render(request,'refferal.html', )




# এখানে আমি একজন ইউজার login করার জন্য ভিউস এর কোড করসি

def LoginView(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(email = email, password = password)
            
            if user is not None:
                login(request,user)
                messages.success(request, f' welcome {user.first_name} {user.last_name} !!')
                return redirect('myclass')
            
            else:
                messages.success(request,'Loggin info incorrect')
                
    else:
        form = AuthenticationForm()
        
    return render(request,'login.html', {'form':form} )


# এখানে আমি একজন ইউজার Logout করার জন্য ভিউস এর কোড করসি


@login_required
def LogoutView(request):
    user = request.user
    logout(request)
    messages.success(request, f'{user.first_name} {user.last_name} is successfully logged out.')
    return redirect('loginpage')
 


# এখানে আমি একজন ইউজার এর profile এর  কোড করসি

def view_Student_Profile(request):
    return render(request,'profile.html')




def ReffaralLinkView(request):
    
    base_url = settings.BASE_URL
    
    user_sponsor = request.user.sponsor
    refferal_code = user_sponsor.code
    
    
    refferal_link = f"{base_url}/Login-Logout/Register/?ref_code={refferal_code}"
    
    return render(request, 'refferal.html', {'ref': refferal_link})