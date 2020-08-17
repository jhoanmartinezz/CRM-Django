from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator_test(view_func): #==> home is view_func
        def wrapper(request, *args, **kwargs):
            group = None
            print("workin", allowed_roles)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Your are not authorized to view this page")
        return wrapper
    return decorator_test

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "customer":
            return redirect("user")
        if group == "admin":
            return view_function(request, *args, **kwargs)
    return wrapper_function
