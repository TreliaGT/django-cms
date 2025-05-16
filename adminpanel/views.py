from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser, Role
from .forms import UserEditForm ,  AddUserForm

@login_required
def dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'adminpanel/user_list.html', {'users': users})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'adminpanel/edit_user.html', {'form': form})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_list')  # adjust to your URL name
    else:
        form = AddUserForm()
    return render(request, 'adminpanel/add_user.html', {'form': form})