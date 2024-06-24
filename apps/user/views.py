from django.views.generic.edit import FormView
from django.views import generic,View
from django.contrib import messages
from django.contrib.auth import get_user_model,authenticate, login as auth_login
from django.shortcuts import render, redirect

from apps.user import forms

User = get_user_model()




class UserUpdateView(generic.UpdateView):
    model = User
    form_class = forms.UserUpdateForm
    template_name = 'user/update.html'
    success_url = '/'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'users'
    


class RegistrationView(View):
    form_class = forms.RegistrationForm
    template_name = 'user/register.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password_1 = cleaned_data['password_1']
            try:
                user = User.objects.create(
                    username=username,
                    nickname=cleaned_data['nickname'],
                    avatar=cleaned_data['avatar'],
                    bio=cleaned_data['bio']
                )
                user.set_password(password_1)
                user.save()
                user = authenticate(username=username, password=password_1)
                auth_login(request, user)
                return redirect('index')
            except Exception as e:
                messages.error(request, f'Error: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
        
        return render(request, self.template_name, {'form': form})




class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = forms.LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, 'Invalid login or password')
            return self.form_invalid(form)



