from django.views import View
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomerUserCreateForm, CustomerUserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class UserRegisterView(View):
    def get(self, request):
        create_form = CustomerUserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, 'users/register.html', context=context)

    def post(self, request):
        form = CustomerUserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            # user.set_password(form.cleaned_data['password'])
            user.save()
            # messages.success(request, 'Registration successful!')
            return redirect('users:login')
        else:
            context = {
                'form': form
            }
            return render(request, 'users/register.html', context=context)


class CustomUserLogin(View):
    def get(self, request):
        login_form = AuthenticationForm
        context = {
            'form': login_form
        }
        return render(request, 'users/register.html', context=context)

    def post(self, request):
        data = AuthenticationForm(data=request.POST)
        if data.is_valid():
            user = data.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'form': data})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'landing_page.html')


class ProfileView(View):
    def get(self,request):
        return render(request, 'users/profile.html', {'user':request.user})


class ProfileUpdateView(View):
    def get(self, request):
        update_form = CustomerUserUpdateForm(instance=request.user)
        context = {
            'update_form': update_form
        }
        return render(request, 'users/profile_update.html', context=context)

    def post(self,request):
        update_form = CustomerUserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
            )
        if update_form.is_valid():
            update_form.save()
            return redirect('users:profile')
        else:
            return render(request, 'users/profile_update.html', {'update_form': update_form})