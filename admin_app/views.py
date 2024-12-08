import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from VGA import urls

# Welcome Page View
def WelcomePage(request):
    return render(request, 'admin_app/WelcomePage.html')

# Project Home Page View
def projecthomepage(request):
    return render(request, 'admin_app/ProjectHomePage.html')

# User Project Home Page View
def userprojecthomepage(request):
    return render(request, 'user_app/UserProjectHomePage.html')

# Seller Page View
def seller(request):
    return render(request, 'seller_app/sellerhomepage.html')

# Login View
def Login(request):
    return render(request, 'admin_app/Login.html')

# Register View
def Register(request):
    return render(request, 'admin_app/Register.html')

# User Registration Logic
def UserRegisterPageCall(request):
    return render(request, 'admin_app/Register.html')

def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'admin_app/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'admin_app/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return redirect('UserLoginPageCall')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'admin_app/Register.html')
    else:
        return render(request, 'admin_app/Register.html')


# User Login Page Call
def UserLoginPageCall(request):
    return render(request, 'admin_app/Login.html')

# User Login Logic
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in

            # Check the length of the username for redirection logic
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('user_app:userprojecthomepage')  # Replace with your student homepage URL name
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('projecthomepage')  # Replace with your faculty homepage URL name
            elif len(username) == 5:
                # Redirect to SellerHomePage
                messages.success(request, 'Login successful as seller!')
                return redirect('sellerhomepage')  # Replace with your seller homepage URL name
            else:
                # Group-based redirection logic
                if user.groups.filter(name='User').exists():
                    messages.success(request, 'Login successful as User!')
                    return redirect('UserProjectHomePage')
                elif user.groups.filter(name='Admin').exists():
                    messages.success(request, 'Login successful as Admin!')
                    return redirect('projecthomepage')
                elif user.groups.filter(name='Seller').exists():
                    messages.success(request, 'Login successful as Seller!')
                    return redirect('sellerhomepage')
                else:
                    # If no group matches
                    messages.error(request, 'Role not assigned to user.')
                    return render(request, 'admin_app/Login.html')

        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'admin_app/Login.html')
    else:
        return render(request, 'admin_app/Login.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('WelcomePage')  # Redirect to a page after logout, e.g., the homepage

def seller_homepage(request):
    return render(request,'seller_app/sellerhomepage.html',)

def taskreminder(request):
    return render(request, 'user_app/taskreminder.html')

def gardenplanning(request):
    return render(request, 'user_app/garden_planning.html')

def planttracker(request):
    return render(request, 'user_app/planttracker.html')


def gardeningtips(request):
    return render(request, 'user_app/gardening_tips.html')

def chatbot(request):
    return render(request, 'user_app/chatbot.html')

def forum(request):
    return render(request, 'user_app/forum.html')

