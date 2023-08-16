from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
# Create your views here.

# homepage
def Home(request):
    return render(request, 'blogger/index.html')

def Post(request):
    return render(request, 'blogger/post.html')

def About(request):
    return render(request, 'blogger/about.html')

def Contact(request):
    return render(request, 'blogger/contact.html')

# signUp user
def SignUp(request):
      render(request, 'blogger/signup.html',{})    
# def SignUp(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit = False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         user = authenticate(username = username,
#                             password = password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('home')
#     context = {
#         'form':form,
#     }
#     return render(request, 'blogger/signup.html', context)

# login user
def Login(request):
    render(request, 'blogger/login.html',{})
# def Login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username,
#                             password = password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 return render(request, 'blogger/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'blogger/login.html', {'error_message': 'Invalid! login. Please try again'})
#     return render(request, 'blogger/login.html')

# Logout user
def Logout(request):
	logout(request)
	return redirect("login")