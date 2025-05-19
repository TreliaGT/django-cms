from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
@login_required
def navigation_list(request):
    return render(request, 'page.html')


@login_required
def media_list(request):
    return render(request, 'page.html')


@login_required
def posttype_list(request):
    return render(request, 'page.html')

@login_required
def page_list(request):
    return render(request, 'page.html')