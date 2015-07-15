from django.contrib.auth import login, authenticate, logout

def logIn(request, username, password):
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
