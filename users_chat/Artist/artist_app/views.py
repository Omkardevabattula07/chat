# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django_ratelimit.decorators import ratelimit
from django.http import HttpResponseForbidden
@ratelimit(key='ip', rate='5/m', method='GET', block=True)
def base_art(request):
    if getattr(request, 'limited', False):
        return HttpResponseForbidden("Too many requests. Please try again after a minute.")
    return render(request, 'base_artist.html')


def register_art(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        bio = request.POST.get('bio')
        profile_pic = request.FILES.get('profile_pic')
        security_answer = request.POST.get('security_answer')

        # Validate inputs
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('register_art')

        if password != password_check:
            messages.error(request, 'Passwords do not match.')
            return redirect('register_art')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register_art')

        # Create User and Profile
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(
            user=user,
            bio=bio,
            profile_pic=profile_pic,
            security_answer=security_answer
        )
        messages.success(request, 'Registration successful! Wait for admin approval.')
        return redirect('login_art')

    return render(request, 'register_artist.html')


def login_art(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        security_answer = request.POST.get('security_answer')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return redirect('login_art')

        # Superuser Login
        if user.is_superuser:
            if user.check_password(password):
                login(request, user)
                return redirect('superuser_art')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login_art')

        # Normal User Login
        if not user.profile.is_approved:
            messages.error(request, 'Your account is not approved yet.')
            return redirect('login_art')

        if not user.check_password(password):
            messages.error(request, 'Invalid username or password.')
            return redirect('login_art')

        if user.profile.security_answer != security_answer:
            messages.error(request, 'Invalid security answer.')
            return redirect('login_art')

        login(request, user)
        return redirect('user_art')

    return render(request, 'login_artist.html')


@login_required
def superuser_art(request):
    if not request.user.is_superuser:
        return redirect('login_art')

    # Pending and Approved Users
    pending_users = UserProfile.objects.filter(is_approved=False)
    approved_users = UserProfile.objects.filter(is_approved=True)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user_profile = get_object_or_404(UserProfile, user_id=user_id)

        if action == 'approve':
            user_profile.is_approved = True
            user_profile.save()
            messages.success(request, f"User '{user_profile.user.username}' approved.")
        elif action == 'delete':
            user_profile.user.delete()
            messages.success(request, f"User '{user_profile.user.username}' deleted.")

        return redirect('superuser_art')

    return render(request, 'superuser_artist.html', {
        'pending_users': pending_users,
        'approved_users': approved_users,
    })



@login_required
def user_art(request):
    if request.user.is_superuser:
        return redirect('superuser_art')
    """
    View for the user page.
    Displays all approved users except the superuser.
    """
    # Fetch all approved users excluding the superuser
    approved_users = UserProfile.objects.filter(is_approved=True).exclude(user__is_superuser=True)
    
    context = {
        'approved_users': approved_users,
    }
    return render(request, 'user_artist.html', context)


@login_required
def chat_art(request, user_id):
    
    user = get_object_or_404(User, id=user_id)
    
    return render(request, 'chat_artist.html', {'chat_user': user})


@login_required
def logout_art(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)
    return redirect('login_art')  # Replace 'login' with the name of your login URL