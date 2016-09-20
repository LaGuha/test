from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def auth(request):
	if not request.user.is_authenticated():
		error=""
		if request.method == "POST":
			form=PostForm(request.POST)
			if form.is_valid():
				username = request.POST['username']
				password = request.POST['password']
				user = authenticate(username=username, password=password)
				if request.POST.get('reg'):
					var=User(username=username)
					var.save()
					var = User.objects.get(username=username)
					var.set_password(password)
					var.save()
					return redirect('bookshop.views.main')
				elif user is not None:			
					if user.is_active:
						login(request, user)
						return redirect('bookshop.views.main')
				else:
					form=PostForm()
					error="wrong"		
		else:
			form = PostForm()
		return render(request, 'bookshop/auth.html',{'form': form, 'error':error})
	else:
		return redirect('bookshop.views.main')
def main(request):
	return render(request, 'bookshop/main.html',{})