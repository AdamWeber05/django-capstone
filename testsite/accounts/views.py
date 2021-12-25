from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

# Sign up function
# @param: request -> type of request (GET, POST, etc)
# Calls Django default User Creation Form to create a new user
# If the information is valid, save the user and make them log in again
# If information is not valid, redirect to the login page.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            # login(request,user)
            return redirect('../../solookup/') #Links back home
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

# Gets the login page
# @param: request -> type of request (GET, POST, etc)
# If the information (password and username) are valid, log in the user in and redirect to the home page
# Else, return them to the login page
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #What to do on login
            user = form.get_user()
            login(request,user)
            return redirect('../../solookup/') #Links back home for now
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})


# Logout the user
# @param: request -> type of request (GET, POST, etc)
# Log the user out, return them to the homepage that will promopt where to login/signup
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('../../solookup/')


# Reset password
# @param: request -> type of request (GET, POST, etc)
# Currently no functionality
def reset_view(request):
    return render(request, 'accounts/reset.html')

