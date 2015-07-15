from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, UpdateView
from django.contrib.auth import login, authenticate, logout
from braces.views import LoginRequiredMixin

from .forms import UserRegisterForm, LoginForm
from .models import User
from apps.inventario.models import Producto
from .funtions import logIn

def userlogin(request):
	if request.method == 'POST':
		if 'register_form' in request.POST:
			user_register = UserRegisterForm(request.POST)
			if user_register.is_valid():
				User.objects.create_user(username=user_register.cleaned_data['username'], email=user_register.cleaned_data['email'], password=user_register.cleaned_data['password'])
				logIn(request, user_register.cleaned_data['username'], user_register.cleaned_data['password'])
				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				logIn(request, login_form.cleaned_data['username'], login_form.cleaned_data['password'])
				return redirect('/')
			else:
				user_register = UserRegisterForm()
				# return render(request, 'users/login.html', {'user_register' : user_register, 'login_form' : login_form})
				# login_form = LoginForm()
	else:
		if request.user.is_authenticated():
			# return redirect('/')
			messagePermissios = True
			producto = Producto.objects.all()
			return render(request, "inventario.html", {'producto' : producto, 'permiso' : messagePermissios})
			# return render(request, 'inventario.html', {'permiso' : messagePermissios})
		else:
			user_register = UserRegisterForm()
			login_form = LoginForm()

	return render(request, 'users/login.html', {'user_register' : user_register, 'login_form' : login_form})

def LogOut(request):
	logout(request)
	return redirect('/')

class UserPerfilView(LoginRequiredMixin, FormView):

	template_name = 'users/userperfil.html'
	login_url = reverse_lazy('/login/')
	form_class = LoginForm
	success_url = reverse_lazy('user_profile')
