from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser, Role , Source
from .forms import UserEditForm ,  AddUserForm  , SourceForm

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
            return redirect('adminapp:user_list')
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
            return redirect('adminapp:user_list')  # adjust to your URL name
    else:
        form = AddUserForm()
    return render(request, 'adminpanel/add_user.html', {'form': form})


# List all sources
@login_required
def source_list(request):
    sources = Source.objects.all()
    return render(request, 'settings/source_list.html', {'sources': sources})

# Add a new source
@login_required
def source_add(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:source_list')
    else:
        form = SourceForm()
    return render(request, 'settings/source_form.html', {'form': form})

# Delete a source
@login_required
def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        source.delete()
        return redirect('adminapp:source_list')
    return render(request, 'settings/source_confirm_delete.html', {'source': source})