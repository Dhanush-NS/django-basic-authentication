from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Signup successful')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        # Bind the form to the POST data
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Get the authenticated user
            user = form.get_user()
            # Log the user in
            login(request, user)
            # Show a success message
            messages.success(request, 'Logged in successfully!')
            # Debugging: Print logged-in user's username
            if request.user.is_authenticated:
                print(f"Logged-in user: {request.user.username}")
            # Redirect to the home page
            return redirect('home')
    else:
        # Display an empty login form for GET requests
        form = AuthenticationForm()
    # Render the login page with the form
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')  # Redirect to login or another page