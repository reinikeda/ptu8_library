from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect


User = get_user_model()

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_error = False
        if len(password1) == 0 or password1 != password2:
            is_error = True
            messages.error(request, "Password do not match or were not entered.")
        if len(username) == 0 or User.objects.filter(username=username).exists():
            is_error = True
            messages.error(request, "Username already taken or was not entered.")
        if len(email) == 0 or User.objects.filter(email=email).exists():
            is_error = True
            messages.error(request, "User with this email already exists, or email was not entered.")
        if not is_error:            
            try:
                User.objects.create_user(username=username, email=email, password=password1)
            except Exception as e:
                is_error = True
                messages.error(request, str(e))
        if not is_error:
            messages.success(request, f'user {username} has been succesfully registered. You can log in now.')
            return redirect(reverse_lazy('login'))
    return render(request, 'user_profile/register.html')
